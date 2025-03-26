


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




