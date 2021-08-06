# Test-publish-my-own-package

A test repo to publish a python package to **PyPI**.

# Requirements and general steps to follow

1. The root directory should contain: 
    - the pacakge folder. Insure to include whithin it a `__init__.py` file
    - `setup.py` file, which is mandatory for **PyPi**)
    - `setup.cfg`
    - `README.md` and a `LICENSE.txt`


2. In `setup.py`, make sure to give the **download_url** and **install_requires**. By clicking on release in the github repostity and following the steps you can get the url of the source code where the package. install_requires contain a list of the package dependencies.

3. run the command `py setup.py sdist` to build a dist folder of the package.

4. `pip install twine` to install a package needed to upload the your package to **PyPI**. Then run `twine upload dist/*` and follow the steps to upload it.

