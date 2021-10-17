# ascii-docs-tier1 #
A distributed collaborative text editor.

This repository contains server code of the ascii-docs project.

The user interface code lives [here]().

## Requirements ##

 - python 3.9.
 - pip 2x.x. Pip is required to install and manage package dependencies.

## Quick start ##

This project uses [Pipenv](https://pipenv-fork.readthedocs.io/en/latest/)
to manage its dependencies and virtual environment. 
The recommended way to set it up is:

```shell
pipenv sync -d
```

Enter the virtual environment.
```shell
pipenv shell
```

Run development server.
```shell
python -m ascii_docs_t1
```