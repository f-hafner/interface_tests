
# A prototype for flexibly testing multiple implementations of the same interface

This repository is a barebone package to explore how to implement reusable tests for multiple implementations of the same interface.

The structure is as follows
- `src/mypkg` has multiple modules `module_a`, `module_b`, `module_c`. They all implement the same interface: they contain a class `MyClassX` that has a method `method`.
- Each module has its own test directory, ie `src/mypkg/module_a/tests`. 
- In each module-specific test, we'd like to make it as easy as possible to run standard tests for the implementation of the interface. This is done with 
    ```python
    from mypkg.interface_tests import *
    ```
- `pytest` executes all tests defined in `interface_tests` when it discovers the test file

### Implementation

I built this functionality with pytest fixtures and hooks.
In `src/mypkg/interface_tests.py`
- define all tests for the interface 

To test the interface, each module needs to define 2 things:
- the fixture `nbody_instance`, which returns an instantiated class of the nbody code to test 
- an import `from mypkg.interface_tests import *` inside `module_x/tests/test_some_file.py`

Pytest discovers fixtures from where it is called, and searches conftest files from the directory upwards. Thus, it is important to define the fixture for each code inside their respective code's directory (`src/mypkg/module_a/confest.py`).

The biggest limitation in this approach is when running `pytest` from root, tests will fail for codes that are not implemented. However, this does not seem to conflict with the testing workflow in amuse: invoking tests through `./setup test bhtree` works because it first `cd`s into the `bhtree` directory, and then runs pytest from there. In this case, pytest only runs the local tests.

In addition, this approach allows specifying the `nbody_instance` more flexibly with additional parameters if necessary.

## Installation

To install mypkg from GitHub repository, do:

```console
git clone git@github.com:f-fhafner/mypkg.git
cd mypkg
python -m pip install .
```

### For developers

```console
git clone git@github.com:f-fhafner/mypkg.git
cd mypkg
python -m venv .venv
source .venv/bin/activate
python -m pip install -e .
# run the tests
pytest -v -s
```


## Credits

This package was created with [Copier](https://github.com/copier-org/copier) and the [NLeSC/python-template](https://github.com/NLeSC/python-template).
