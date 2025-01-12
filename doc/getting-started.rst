===============
Getting Started
===============
On this page you will find all the information to get started with |Project|.
A basic knowledge of programming in Python is assumed, but nothing more than
that.

Getting Python
--------------
To install |Project|, a working version of Python 3.4 or higher has to be
installed on your computer. We recommend using the `Anaconda Distribution <https://www.continuum.io/downloads>`_
of Python. This Python distribution includes most of the python package
dependencies and the Jupyter Notebook software to run the notebooks. Moreover,
it includes the Graphical User Interface (GUI) Spyder to start scripting in
Python. However, you are free to install any Python distribution you want.

Getting PASTAS
--------------
To get |Project|, there are several options available. The easiest is to use
the Python Package Index (`PyPI <https://pypi.python.org/pypi>`_), where
many official python packages are gathered. To get the latest version of
|Project|, open the Anaconda Prompt, a Windows Command Prompt (also called
command window) or a Mac terminal and type::

  pip install pastas

|Project| will now be installed on your computer, including the packages
necessary for |Project| to work properly (called dependencies in Python
language).

It sometimes occurs that the automatic installation of the
dependencies does not work. A safe method to update another package if you are
using Anaconda is to install a package with the follow command line::

  conda install package

Using PASTAS
------------
To start using PASTAS, open your python GUI (Spyder, PyCharm or any other) to edit
and run a script, or start typing in the IPython console (bottom right in Spyder). See the :ref:`Examples`-section
for some example-code.
  
Updating PASTAS
---------------
If you have already installed |Project|, it is possible to update |Project|
easily. To update, open a Windows command screen or a Mac terminal and type::

  pip install pastas --upgrade

Dependencies
------------
Pastas depends on a number of Python packages, of which all of the necessary are
automatically installed when using the pip install manager. To summarize, the
following packages are necessary for a minimal function installation of
|Project|:

* numpy>=1.15
* matplotlib>=2.0
* pandas>=0.23
* scipy>=1.1

Other optional dependencies include:

* requests (For downloading KNMI data from the web)

