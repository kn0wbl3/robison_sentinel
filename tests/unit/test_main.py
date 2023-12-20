import pytest
from unittest import mock
import robison_sentinel.input.main as main
import os

os.environ["DEBUG_MODE"] = True
os.environ["ROBISON_USERNAME"] = "test"
os.environ["ROBISON_PASSWORD"] = "123"

class Test_get_base_url:
    @pytest.mark.parametrize(
        "debug_mode, expected",
        [
            (True, "http://127.0.0.1:5000")
            (False, "https://myaccount.robisonoil.com")
        ],
    )
    def test_get_base_url(debug_mode, expected):
        assert expected == main.get_base_url(debug_mode)