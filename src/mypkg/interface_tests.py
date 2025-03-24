


def test_interface(Implementation, run_interface_tests):
    run_interface_tests(Implementation)

# Define modules to be tested
from mypkg.module_a.module_a import MyClassA
from mypkg.module_b.module_b import MyClassB

module_map = {
        "test_module_a": MyClassA,
        "test_module_b": MyClassB
        }

# Define interface tests
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

