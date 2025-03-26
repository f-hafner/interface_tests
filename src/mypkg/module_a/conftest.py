
import pytest

from mypkg.module_a.module_a import MyClassA

@pytest.fixture()
def nbody_instance():
    print("returning MyClassA")
    return MyClassA()

