
import pytest

from mypkg.interface_tests import import_map
from mypkg.interface_tests import ALL_INTERFACE_TESTS


@pytest.fixture()
def run_interface_tests():
    def _run(implementation_class):
        impl = implementation_class()
        # Run each test function with the implementation
        for test_func in ALL_INTERFACE_TESTS:
            test_func(impl)

    return _run

def pytest_generate_tests(metafunc):
    # I think the same logic could also be implemented in the run_interface_tests fixture
    if metafunc.function.__name__ == "test_interface":
        calling_module = metafunc.module.__name__
        requested_module = import_map[calling_module]
        r_mod, r_cls = requested_module
        implementation = pytest.importorskip(r_mod)
        # this still continues if the module exists
        # but the requested class does not exist
        implementation = getattr(implementation, r_cls, None)
        if implementation:
            metafunc.parametrize("Implementation", [implementation])
        else:
            pytest.skip(f"No class {r_cls} in module {r_mod}")


