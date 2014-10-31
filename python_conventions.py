# @package main

# Standard library imports


# Related third party imports


# Local application/library specific imports


# Global variable initialization
GLOBAL_CONSTANT_NAME = 42


def function_name(function_parameter_name):
    local_var_name = function_parameter_name
    print local_var_name

class ExceptionName(Exception):
    def __init__(self, message):
        Exception.__init__(self, message)

class ClassName:
    def __init__(self):
        self.instance_var_name = GLOBAL_CONSTANT_NAME

    def method_name(self):
        raise ExceptionName(self.instance_var_name)

if __name__ == "__main__":
    function_name(GLOBAL_CONSTANT_NAME)

    global_var_name = ClassName()
    global_var_name.method_name()