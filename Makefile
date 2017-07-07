all: localdrafts

local:
	bundle exec jekyll serve

debug:
	bundle exec jekyll serve --draft --verbose

localdrafts:
	bundle exec jekyll serve --draft