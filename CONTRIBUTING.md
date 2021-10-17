# Contributing #

## Writing Code ##

We should rely on the common pythonic practices making our code readable and 
peer-reviewable.

#### Docstrings ####

Python has a well-developed conventions on docstrings; please use them 
with all definitions.

#### Type annotations ####

Type annotations where possible. This makes code more readable and less 
bugprone.

#### Example ####

The following is an example of a function definition with proper docstring 
and type annotation.

```python
def hello_world(name: str) -> str:
    """
    Dummy hello world.
    
    An exemplary hello world function. 
    
    Args:
        name: Hello who now.
    Returns:
        Hello world message.
    """
    return f"hello {name}"
```

Please check for proper annotations with 
[mypy](https://mypy.readthedocs.io/en/stable/introduction.html). This prevents
common bugs related to passing wrong parameters and can save lots of debugging 
effort.

## Formatting ##

Reviewing code consisting of different styles can incur brain damage.
Please format with line length of 80 characters (my screen is small).
```shell
black -l 80 ascii_docs_t1/* tests/*
```

Imports can get messy.. *[isort][https://github.com/PyCQA/isort]* sorts imports 
alphabetically, and groups into sections and by type.
```shell
isort ascii_docs_t1/* tests/*
```