all: clean serve_drafts

serve:
	bundle exec jekyll serve

debug:
	bundle exec jekyll serve --draft --verbose

serve_drafts:
	bundle exec jekyll serve --draft --unpublished

clean:
	bundle exec jekyll clean;
	rm -f o2r_project_website_and_blog.pdf;
	rm -f o2r_project_website_and_blog_git-repository.zip;

build: clean
	bundle exec jekyll build

save_all_content_to_pdf:
	wkhtmltopdf \
	--outline \
	--javascript-delay 20000 --no-stop-slow-scripts \
	--margin-top 20mm \
	--margin-bottom 20mm \
	--footer-html http://127.0.0.1:4000/public/pdf_footer.html \
	toc http://127.0.0.1:4000/all_content/ o2r_project_website_and_blog.pdf

capture_pdf:
	make serve & ( sleep 5 && make save_all_content_to_pdf ; echo "Captured PDF"; )

capture_zip:
	git archive --format=zip HEAD -o o2r_project_website_and_blog_git-repository.zip

update_zenodo_deposit: build capture_pdf capture_zip
	python3 $(shell pwd)/zenodo_release.py;
	pkill -f jekyll;

.PHONY: update_zenodo_deposit
