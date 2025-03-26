


# Define interface tests
def test_method_exists(nbody_instance):
    print("\ncalled test_method_exists")
    assert hasattr(nbody_instance, "method")


def test_method_returns_string(nbody_instance):
    print("\ncalled test_method_returns_string")
    result = nbody_instance.method()
    assert isinstance(result, str), "Method must return a string"

def test_instance_creation(nbody_instance):
    print("\ncalled test_instance_creation")
    assert nbody_instance is not None, "Instance should be created successfully"




