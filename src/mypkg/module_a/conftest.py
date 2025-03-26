
import pytest

from mypkg.module_a.module_a import MyClassA

@pytest.fixture()
def instance():
    print("returning MyClassA")
    return MyClassA()

