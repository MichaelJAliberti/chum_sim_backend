import pytest

from src.api.utils import copy_class_def


@pytest.mark.parametrize(
    "classname, value",
    [
        [
            "Bar",
            5,
        ],
    ],
)
def test_copy_class_def(classname, value):
    class Foo:
        def __init__(self, val):
            self.val = val

    NewClass = copy_class_def(name=classname, class_def=Foo)
    bar = NewClass(value)

    assert type(bar).__name__ == classname
    assert bar.val == value
