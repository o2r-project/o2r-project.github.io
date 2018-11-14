all: clean serve_drafts

serve:
	bundle exec jekyll serve

debug:
	bundle exec jekyll serve --draft --verbose

serve_drafts:
	bundle exec jekyll serve --draft

clean:
	bundle exec jekyll clean

build: clean
	bundle exec jekyll build

create_pdf:
	wkhtmltopdf \
	--outline \
	--javascript-delay 10000 --no-stop-slow-scripts \
	--margin-top 20mm \
	--margin-bottom 20mm \
	--footer-html http://127.0.0.1:4000/public/pdf_footer.html \
	toc http://127.0.0.1:4000/all_content/ o2r_project_website_and_blog.pdf

update_pdf_on_zenodo: 
	make serve & (sleep 3 && make create_pdf ; pkill -f jekyll )
	python3 ./zenodo_release_pdf.py
