import pytest
import requests

def f():
    raise SystemExit(1)


def test_raise():
    with pytest.raises(SystemExit):
        f()