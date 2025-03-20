

import pytest
#from mypkg.module_a.module_a import MyClassA
#from mypkg.module_b.module_b import MyClassB
#
#@pytest.fixture(params=[MyClassA, MyClassB])
#def Implementation(request):
#    return request.param
#

def test_interface(Implementation, run_interface_tests):
    run_interface_tests(Implementation)

