all: clean localdrafts

local:
	bundle exec jekyll serve

debug:
	bundle exec jekyll serve --draft --verbose

localdrafts:
	bundle exec jekyll serve --draft

clean:
	bundle exec jekyll clean