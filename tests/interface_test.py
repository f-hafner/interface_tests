
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
    #"""Applies all interface tests to a given class."""
    #def wrapped_test(cls, test_func):
    #    test_func(cls)  # Run the actual test function

    #return wrapped_test



### old
## List all interface test functions
#def test_method_exists(cls):
#    instance = cls()
#    assert hasattr(instance, "method"), "Class must have a 'method' attribute"
#
#def test_method_returns_string(cls):
#    instance = cls()
#    result = instance.method()
#    assert isinstance(result, str), "Method must return a string"
#
#def test_instance_creation(cls):
#    instance = cls()
#    assert instance is not None, "Instance should be created successfully"
#
## Collect all tests in a list
#ALL_INTERFACE_TESTS = [
#    test_method_exists,
#    test_method_returns_string,
#    test_instance_creation,
#]
#
## Function to apply all tests to a given class
#def run_interface_tests(cls):
#    """Applies all interface tests to a given class."""
#    @pytest.mark.parametrize("test_func", ALL_INTERFACE_TESTS)
#    @pytest.mark.parametrize("cls", [cls])  # Pass class to test functions
#    def wrapped_test(cls, test_func):
#        test_func(cls)  # Run the actual test function
#
#    return wrapped_test
#
