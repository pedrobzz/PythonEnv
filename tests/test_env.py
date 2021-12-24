from env import __version__, Env
import pytest


def test_version():
    assert __version__ == '0.1.0'

@pytest.mark.parametrize(
    "test_input,expected", 
    [
        ("login", "admin"), 
        ("password", "admin12345"), 
        ("server_url", "256.23.0.143/3001/api")
    ])
def test_env(test_input, expected):
    env = Env("./tests/tokens").initialize()

    assert env[test_input] == expected