


def test_interface(Implementation, run_interface_tests):
    run_interface_tests(Implementation)

# map files of tests to imports and classes
import_map = {
        "test_module_a": ("mypkg.module_a.module_a", "MyClassA"),
        "test_module_b": ("mypkg.module_b.module_b", "MyClassB"),
        # we can also add unavailable modules
        "test_module_c": ("mypkg.module_c.module_c", "MyClassC"),
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

