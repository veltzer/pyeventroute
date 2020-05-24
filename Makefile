.PHONY: all

all:
	@pylint --rcfile=.pylint.rc --reports=n --score=n pyeventroute tests
	@pyflakes pyeventroute tests
	@pytest tests -qq > /dev/null
