examine-tarball: package
	cd dist && tar xzf *.tar.gz && cd ..
	tree dist

examine-install:
	./examine-install.sh

install:
	pip install .

clean:
	rm -rf dist *.egg-info .cache
	find . -name __pycache__ | xargs rm -rf
	find . -name '*.pyc' | xargs rm

package: clean
	python setup.py sdist
