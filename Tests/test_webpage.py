from webpage import *
import pytest


def test_check_status():
    with pytest.raises(ResponseException):
        check_status(404)
