

import pytest

from mypkg.module_b.module_b import MyClassB

@pytest.fixture()
def instance():
    print("returning MyClassB")
    return MyClassB()

