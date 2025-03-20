import pytest

def test_method_exists(cls):
    print("\ncalled test_method_exists")
    instance = cls()
    assert hasattr(instance, "method")


def test_method_returns_string(cls):
    print("\ncalled test_method_returns_string")
    instance = cls()
    result = instance.method()
    assert isinstance(result, str), "Method must return a string"

def test_instance_creation(cls):
    print("\ncalled test_instance_creation")
    instance = cls()
    assert instance is not None, "Instance should be created successfully"


ALL_INTERFACE_TESTS = [
    test_method_exists,
    test_method_returns_string,
    test_instance_creation,
]


@pytest.fixture()
def interface_test_funcs():
    return ALL_INTERFACE_TESTS

@pytest.fixture()
def run_interface_tests(interface_test_funcs):
    def _run(implementation_class):
        # Instantiate the implementation
        impl = implementation_class

        # Run each test function with the implementation
        for test_func in interface_test_funcs:
            test_func(impl)

    return _run





#@pytest.fixture(params=ALL_INTERFACE_TESTS)
#def all_interface_tests(request):
#    return request.param
#
#@pytest.mark.parametrize("cls", [])  # Pass class to test functions
#@pytest.mark.parametrize("test_func", [])
#def test_interface(cls, test_func):
#    test_func(cls)


