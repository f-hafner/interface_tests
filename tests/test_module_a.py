
import pytest
from mypkg.module_a import MyClassA
from mypkg.module_b import MyClassB

from .interface_test import test_interface
from .interface_test import ALL_INTERFACE_TESTS


@pytest.mark.parametrize("cls", [MyClassA, MyClassB])
@pytest.mark.parametrize("test_func", ALL_INTERFACE_TESTS)
def test_interface_wrapper(cls, test_func):
    test_interface(cls, test_func)

# note: this is fine, but requires all of [MyClassA, MyClassB] to 
# be installed in the environment. Thus, it will fail 
# for people contributing only their own code

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
