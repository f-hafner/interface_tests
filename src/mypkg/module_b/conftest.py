

import pytest

from mypkg.module_b.module_b import MyClassB

@pytest.fixture()
def nbody_instance():
    print("returning MyClassB")
    return MyClassB()

