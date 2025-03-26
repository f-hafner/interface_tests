

import pytest

from mypkg.module_c.module_c import MyClassC

@pytest.fixture()
def nbody_instance():
    print("returning MyClassC")
    return MyClassC()

