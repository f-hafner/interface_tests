
import pytest
#from mypkg.module_a.module_a import MyClassA
#from mypkg.module_b.module_b import MyClassB


#from mypkg.module_a.module_a import MyClassA as class_to_be_tested
from my_tests import test_interface


#@pytest.fixture(params=[MyClassA, MyClassB])
#def Implementation(request):
#    return request.param


#def test_interface(Implementation, run_interface_tests):
#    run_interface_tests(Implementation)



#@pytest.mark.parametrize("cls", [MyClassA, MyClassB])
#@pytest.mark.parametrize("test_func", ALL_INTERFACE_TESTS)
#def test_interface_wrapper(Implementation, all_interface_tests):
#    test_interface(Implementation, all_interface_tests)

# note: this is fine, but requires all of [MyClassA, MyClassB] to 
# be installed in the environment. Thus, it will fail 
# for people contributing only their own code

# this is a nice option for the CI that tests all interfaces 

