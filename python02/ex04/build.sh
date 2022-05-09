pip install --upgrade pip
pip install --upgrade setuptools
pip install wheel
python setup.py sdist
./setup.py bdist_wheel
pip install ./dist/my_minipack-1.0.0.tar.gz
pip install ./dist/my_minipack-1.0.0-py3-none-any.whl
