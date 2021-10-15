# ascii-docs dummy test.
# Stanislav Sotnikov (ssotnikov@ccny.cuny.edu)
# The City College of New York CSC I0220


import uuid

from ascii_docs_t1.__main__ import hello_world


def test_hello_world():
    """
    Dummy test
    """
    random = uuid.uuid4().hex

    assert f"hello {random}" == hello_world(random)
