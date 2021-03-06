from distutils.core import setup


setup(
  name = 'test_package_badr_moufad',      
  packages = ['test_package_badr_moufad'],
  version = '0.2',
  license='MIT', 
  description = 'A test repo to publish a python package to PyPI',
  author = 'Badr MOUFAD',
  author_email = 'Badr.MOUFAD@emines.um6p.ma',
  url = 'https://github.com/Badr-MOUFAD/test_package_badr_moufad',
  download_url = 'https://github.com/Badr-MOUFAD/test_package_badr_moufad/archive/refs/tags/v0.2.tar.gz',
  keywords = ['Example', 'test_package'],
  install_requires=[
          'numpy',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
  ],
)