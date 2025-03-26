

import pytest

from mypkg.module_c.module_c import MyClassC

@pytest.fixture()
def instance():
    print("returning MyClassC")
    return MyClassC()

