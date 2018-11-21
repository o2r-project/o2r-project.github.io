import requests
import json
import sys
import logging
import os
import pprint
from datetime import datetime
import time

logging.basicConfig(level=logging.INFO)

# configuration
#deposition_url = 'https://sandbox.zenodo.org/api/deposit/depositions/238796' # for testing
deposition_url = 'https://zenodo.org/api/deposit/depositions/1485438'
pdf_file_name = 'o2r_project_website_and_blog.pdf'

token = os.environ['ZENODO_TOKEN']
logging.debug('Token: %s' % (token))

class prettylog():
    def __init__(self, obj):
        self.obj = obj
    def __repr__(self):
        return pprint.pformat(self.obj)

# get the version of the current deposition and compare it with the latest blog post
r_deposition = requests.get('%s?access_token=%s' % (deposition_url, token))
deposition = json.loads(r_deposition.text)
published_version = time.strptime(deposition['metadata']['version'], '%Y-%m-%d')
post_dates = [time.strptime(x[:10], "%Y-%m-%d") for x in os.listdir('_posts')]
newer_posts = [date for date in post_dates if date > published_version]
if(len(newer_posts) < 1):
    logging.info('No newer posts than published version %s' % (time.strftime('%Y-%m-%d', published_version)))
    sys.exit(0)

logging.info('Updating website and blog PDF on Zenodo with %s new post(s): %s' % (len(newer_posts), newer_posts))

# create a new version of the deposition
r_new = requests.post('%s/actions/newversion' % (deposition_url), params = {'access_token': token})
if r_new.status_code != 201:
    logging.critical('Error creating new version: %s', r_new.text)
    sys.exit()
data_new = json.loads(r_new.text)
logging.info('Created new draft:\n%s' % prettylog(data_new))
draft_url = data_new['links']['latest_draft']
logging.info('Created new draft %s' % draft_url)

# get the id of the current file and delete it
r_list = requests.get('%s/files' % (draft_url), params = {'access_token': token})
deposit_contents = json.loads(r_list.text)
pdf_file = [x for x in deposit_contents if x['filename'] == pdf_file_name ][0]
logging.info('Deleting file %s with id %s from %s' % (pdf_file_name, pdf_file['id'], draft_url))
r_delete = requests.delete('%s/files/%s' % (draft_url, pdf_file['id']), params = {'access_token': token})
if r_delete.status_code != 204:
    logging.critical('Error deleting existing file: %s', r_delete.text)
    sys.exit()
r_list = requests.get('%s/files' % (draft_url), params = {'access_token': token})
deposit_contents = json.loads(r_list.text)
logging.info('Deleted file %s, now have %s file(s) left' % (pdf_file['id'], len(deposit_contents)))

# upload updated file
data = {'filename': pdf_file_name}
files = {'file': open(pdf_file_name, 'rb')}
r_upload = requests.post('%s/files?access_token=%s' % (draft_url, token),
                         data = data,
                         files = files)
if r_upload.status_code != 201:
    logging.critical('Error uploading file: %s', r_upload.text)
    sys.exit()
logging.info('Uploaded new file! Response:\n%s', prettylog(json.loads(r_upload.text)))

# update the version string to current date
date_string = datetime.now().strftime('%Y-%m-%d')

data_update = {}
data_update['metadata'] = data_new['metadata']
data_update['metadata']['version'] = date_string

data_test = {
    "metadata": {
        "version": "testonly"
    }
}

# send the metadata update
headers = {"Content-Type": "application/json"}
md_url = '%s?access_token=%s' % (draft_url, token)
logging.info('Will update metadata at %s with:\n %s' % (draft_url, prettylog(data_update)))
r_update = requests.put(md_url,
                        data = json.dumps(data_update),
                        headers = headers)
if r_update.status_code != 200:
    logging.critical('Error updating metadata: %s', r_update.text)
    sys.exit()
logging.info('Updated Metadata!\n%s' % (prettylog(json.loads(r_update.text))))

# publish the updated deposit
#r_publish = requests.post('%s/actions/publish' % (draft_url), params = {'access_token': token})
#if r_publish.status_code != 201:
#    logging.critical('Error publishing new version: %s', r_publish.text)
#    sys.exit()
#logging.info('Publishing response:\n%s' % (prettylog(json.loads(r_publish.text))))
#logging.info('Published! Go to %s' % (json.loads(r_publish.text)['links']['record_html']))