
import pytest

from mypkg.interface_tests import module_map
from mypkg.interface_tests import ALL_INTERFACE_TESTS


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

def pytest_generate_tests(metafunc):
    # I think the same logic could also be implemented in the run_interface_tests fixture
    if metafunc.function.__name__ == "test_interface":
        calling_module = metafunc.module.__name__
        metafunc.parametrize("Implementation", [module_map[calling_module]])


