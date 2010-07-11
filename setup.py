from distutils.core import setup

setup(name='inflect_dj',
      version='v0.1.2',
      description="Correctly generate plurals when using Django",
      author='Paul Dyson',
      author_email='pwdyson@yahoo.com',
      url="http://pypi.python.org/pypi/inflect_dj",
      py_modules=['inflect_dj'],
      requires=['inflect'],
      provides=['inflect_dj'],
      keywords = ['plural', 'django'],
      classifiers = [
        "Programming Language :: Python",
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU Affero General Public License v3",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Framework :: Django",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Text Processing :: Linguistic",
        ],
      long_description = open('README.txt').read()
      )
