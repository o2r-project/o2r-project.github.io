all: localdrafts

local:
	bundle exec jekyll serve

localdrafts:
	bundle exec jekyll serve --draft