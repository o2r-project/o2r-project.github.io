all: clean serve_drafts

serve:
	bundle exec jekyll serve

debug:
	bundle exec jekyll serve --draft --verbose

serve_drafts:
	bundle exec jekyll serve --draft

clean:
	bundle exec jekyll clean;
	rm -f o2r_project_website_and_blog.pdf

build: clean
	bundle exec jekyll build

capture_pdf:
	wkhtmltopdf \
	--outline \
	--javascript-delay 10000 --no-stop-slow-scripts \
	--margin-top 20mm \
	--margin-bottom 20mm \
	--footer-html http://127.0.0.1:4000/public/pdf_footer.html \
	toc http://127.0.0.1:4000/all_content/ o2r_project_website_and_blog.pdf

create_pdf: clean
	make serve & ( sleep 10 && make capture_pdf ; echo "Captured PDF"; )

update_pdf_on_zenodo: create_pdf
	python3 ./zenodo_release_pdf.py;
	pkill -f jekyll;

.PHONY: update_pdf_on_zenodo
