
import pytest

@pytest.mark.parametrize("cls", [])  # Placeholder, will be overridden in test scripts
def test_method_exists(cls):
    print("\ncalled test_method_exists")
    instance = cls()
    assert hasattr(instance, "method")


@pytest.mark.parametrize("cls", [])  # Placeholder, will be overridden in test scripts
def test_method_returns_string(cls):
    print("\ncalled test_method_returns_string")
    instance = cls()
    result = instance.method()
    assert isinstance(result, str), "Method must return a string"

@pytest.mark.parametrize("cls", [])  # Placeholder, will be overridden in test scripts
def test_instance_creation(cls):
    print("\ncalled test_instance_creation")
    instance = cls()
    assert instance is not None, "Instance should be created successfully"


ALL_INTERFACE_TESTS = [
    test_method_exists,
    test_method_returns_string,
    test_instance_creation,
]



@pytest.mark.parametrize("cls", [])  # Pass class to test functions
@pytest.mark.parametrize("test_func", [])
def test_interface(cls, test_func):
    test_func(cls)


# so this could go into a conftest.py 
# at the level of the library
# it can then be used by any code 

# how do we make it as easy as possible to use the 
# test_interface function 

# TODO: how do we add different parameters to the parameterize, if we need that?
# what do we need? we need to dynamically determine the name of the 


