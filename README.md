# Test-publish-my-own-package

A test repo to publish a python package to **PyPI**.

# Requirements and general steps to follow

1. The root directory should contain: 
    - the pacakge folder. Insure to include whithin it a `__init__.py` file
    - `setup.py` file, which is mandatory for **PyPi**)
    - `setup.cfg`
    - `README.md` and a `LICENSE.txt`


2. In `setup.py`, make sure to give the **download_url** and **install_requires**. By clicking on release (in the right-hand side panel) and following the steps you can get the URL of the source code where the package is. **install_requires** contains a list of the package dependencies.

3. run the command `py setup.py sdist` to build a dist folder of the package.

4. `pip install twine` to install a package needed to upload your package to **PyPI**. Then run `twine upload dist/*` and follow the steps to upload it.


# Package in action

After successfully publishing the package to PyPI, you can import it whenever and wherever you want by running `pip install test_pacakge_badr_moufad`

### snippets example

```python
# import package
from test_package_badr_moufad.my_class import Person

user = Person(username="Badr MOUFAD")

user.greet() # output: Hi there! Nice to meet you Badr MOUFAD"
```