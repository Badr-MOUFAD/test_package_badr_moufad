# Test-publish-my-own-package

A test repo to publish a python package to **PyPI**.

# Requirements and general steps to follow

1. The root directory should contain: 
    - the pacakge folder. Insure to include whithin it a `__init__.py` file
    - `setup.py` file, which is mandatory for **PyPi**)
    - `setup.cfg`
    - `README.md` and a `LICENSE.txt`


2. In `setup.py`, make sure to give the **download_url** and **install_requires**. By clicking on release (in the right-hand side panel) and following the steps you can get the URL of the source code where the package is. **install_requires** contains a list of the package dependencies.

3. run the command `$ py setup.py sdist` to build a dist folder of the package.

4. `$ pip install twine` to install a package needed to upload your package to **PyPI**. Then run `twine upload dist/*` and follow the steps to upload it.


# Documentation

1. Firstly install `sphinx` by running

    `$ pip install sphinx`

2. Generate the documentation structure by hitting the below command and then follow the dialog

    `$ sphinx-quickstart docs`

3. Hit `$ pip install furo` To use the `Furo` theme, and then change the `conf.py` as follow

    ```python
    # -- Options for HTML output -------------------------------------------------

    # The theme to use for HTML and HTML Help pages.  See the documentation for
    # a list of builtin themes.
    #
    html_theme = 'furo'
    ```

4. Again, add this piece of code to `conf.py` to indicate where to parse docstings

    ```python
    import pathlib
    import sys
    sys.path.insert(0, pathlib.Path(__file__).parents[2].resolve().as_posix())
    ```

5. Add some Sphinx extension and there setups to parse docstrings, and ste

    ```python
        extensions = [
           'sphinx.ext.duration',
           'sphinx.ext.doctest',
           'sphinx.ext.autodoc',
           'sphinx.ext.autosummary',
           # for numpy docstring convention
           'sphinx.ext.napoleon'
        ]

        # setups
        napoleon_numpy_docstring = True
        napoleon_use_param = True
        napoleon_use_admonition_for_examples = True
    ```

### Note:
To build documention, run the command `$ sphinx-build -b html docs/source/ docs/build/html`. Also, whenever you add | change documention files, make sure to re run it before previewing the results.



# Package in action

After successfully publishing the package to PyPI, you can import it whenever and wherever you want by running `pip install test_pacakge_badr_moufad`

### snippets example

```python
# import package
from test_package_badr_moufad.my_class import Person

user = Person(username="Badr MOUFAD")

user.greet() # output: Hi there! Nice to meet you Badr MOUFAD"
```