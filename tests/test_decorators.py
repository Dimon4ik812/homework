from src.decorators import log

import os


@log(filename="mylog.txt")
def my_function(x, y):
    if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
        raise TypeError("Both arguments must be numbers")
    return x + y


def setup_function():
    log_file = "mylog.txt"
    if os.path.exists(log_file):
        os.remove(log_file)


def teardown_function():
    log_file = "mylog.txt"
    if os.path.exists(log_file):
        os.remove(log_file)


def test_log_ok():
    my_function(1, 2)
    log_file = "mylog.txt"
    with open(log_file, "r") as file:
        log_content = file.readlines()
    assert log_content[-1] == "my_function ok\n"


def test_log_error():
    my_function(1, "2")
    log_file = "mylog.txt"
    with open(log_file, "r") as file:
        log_content = file.readlines()
    assert log_content[-1].startswith("my_function error")
