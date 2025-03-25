
# A prototype for flexibly testing multiple implementations of the same interface

This repository is a barebone package to explore how to implement reusable tests for multiple implementations of the same interface.

The structure is as follows
- `src/mypkg` has multiple modules `module_a`, `module_b`, `module_c`. They all implement the same interface: they contain a class `MyClassX` that has a method `method`.
- Each module has its own test directory, ie `src/mypkg/module_a/tests`. 
- In each module-specific test, we'd like to make it as easy as possible to run standard tests for the implementation of the interface. This is done with 
    ```python
    from mypkg.interface_tests import test_interface
    ```
- `pytest` executes `test_interface` when it discovers the test file
- This led to the following requirements:
    - we need to dynamically determine which module to test from the calling test function alone
    - for any user running the test, they may not have installed all modules that implement the interface. Therefore, we have to dynamically determine which tests to run

### Implementation

I built this functionality with pytest fixtures and hooks.
In `src/mypkg/interface_tests.py`
- define all tests for the interface 
- map from calling functions to modules to be imported and classes to be passed to the test

In `src/mypkg/conftest.py`
- import things defined in `interface_tests.py`
- define fixture `run_interface_tests`, which takes a dynamic implementation_class and runs all tests on that
- `pytest_generate_tests` hook detects the function `test_interface`, and dynamically returns the class to be tested that implements the interface. If the requested module is not importable, the test is skipped.

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
