import pytest

def test_method_exists(instance):
    print("\ncalled test_method_exists")
    assert hasattr(instance, "method")


def test_method_returns_string(instance):
    print("\ncalled test_method_returns_string")
    result = instance.method()
    assert isinstance(result, str), "Method must return a string"

def test_instance_creation(instance):
    print("\ncalled test_instance_creation")
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
        impl = implementation_class()
        # Run each test function with the implementation
        for test_func in interface_test_funcs:
            test_func(impl)

    return _run


# This should not be necessary
from mypkg.module_a.module_a import MyClassA
from mypkg.module_b.module_b import MyClassB

module_map = {
        "test_module_a": MyClassA,
        "test_module_b": MyClassB
        }

#@pytest.fixture(params=[MyClassA, MyClassB])
#def Implementation(request):
#    return request.param

def pytest_generate_tests(metafunc): # this is called only once
    if metafunc.function.__name__ == "test_interface":
        calling_module = metafunc.module.__name__
        metafunc.parametrize("Implementation", [module_map[calling_module]])
        #mymodule = metafunc.module
        #myvars = vars(mymodule)
        #myvars["MyClassA"] # this is from the module import in test_module_a?
        # metafunc.module gives /path/to/test_module_a
        #print("hello.")



#@pytest.fixture(params=ALL_INTERFACE_TESTS)
#def all_interface_tests(request):
#    return request.param
#
#@pytest.mark.parametrize("cls", [])  # Pass class to test functions
#@pytest.mark.parametrize("test_func", [])
#def test_interface(cls, test_func):
#    test_func(cls)


