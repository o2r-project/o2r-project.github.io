
import requests
import json
import sys
import logging
import os

logging.basicConfig(level=logging.DEBUG)

# See http://developers.zenodo.org/

token = os.environ['ZENODO_TOKEN']

logging.debug('Token: %s' % (token))
sys.exit(0)

# create a new version of the deposition
r_new = requests.post('https://sandbox.zenodo.org/api/deposit/depositions/238796/actions/newversion', params = {'access_token': token})
if r_new.status_code != 201:
    logging.critical('Error creating new version: %s', r_new.text)
    sys.exit()
data = json.loads(r_new.text)
draft_url = data['links']['latest_draft']
logging.info('Created new draft %s' % draft_url)

# get the id of the current file and delete it
r_list = requests.get('%s/files' % (draft_url), params = {'access_token': token})
deposit_contents = json.loads(r_list.text)
pdf_file = [x for x in deposit_contents if x['filename'] == 'o2r_project_website_and_blog.pdf' ][0]
r_delete = requests.delete('%s/files/%s' % (draft_url, pdf_file['id']), params = {'access_token': token})
if r_delete.status_code != 204:
    logging.critical('Error deleting existing file: %s', r_delete.text)
    sys.exit()
logging.info('Deleted file %s' % pdf_file['id'])

# upload updated file
data = {'filename': 'o2r_project_website_and_blog.pdf'}
files = {'file': open('o2r_project_website_and_blog.pdf', 'rb')}
r_upload = requests.post('%s/files?access_token=%s' % (draft_url, token),
                         data = data,
                         files = files)
if r_upload.status_code != 201:
    logging.critical('Error uploading file: %s', r_upload.text)
    sys.exit()
logging.info('Uploaded new file')

# TODO update the date of the deposit to "now"
# TODO update the version to current date

r_publish = requests.post('%s/actions/publish' % (draft_url), params = {'access_token': token})
if r_upload.status_code != 202:
    logging.critical('Error uploading file: %s', r_upload.text)
    sys.exit()
logging.info('Published!')