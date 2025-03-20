
import pytest
from mypkg.module_a.module_a import MyClassA
from mypkg.module_b.module_b import MyClassB


@pytest.fixture(params=[MyClassA, MyClassB])
def Implementation(request):
    return request.param


def test_module_interface(Implementation, run_interface_tests):
    run_interface_tests(Implementation)



#@pytest.mark.parametrize("cls", [MyClassA, MyClassB])
#@pytest.mark.parametrize("test_func", ALL_INTERFACE_TESTS)
#def test_interface_wrapper(Implementation, all_interface_tests):
#    test_interface(Implementation, all_interface_tests)

# note: this is fine, but requires all of [MyClassA, MyClassB] to 
# be installed in the environment. Thus, it will fail 
# for people contributing only their own code

# this is a nice option for the CI that tests all interfaces 


###############################################
# test individually
#from .interface_test import test_method_exists # import appears as skipping the test_method
#from .interface_test import test_method_returns_string
#from .interface_test import test_instance_creation

#@pytest.mark.parametrize("cls", [MyClassA, MyClassB])
#def test_method_wrapped(cls):
#    test_method_exists(cls)
#    test_method_returns_string(cls)
#    test_instance_creation(cls)
