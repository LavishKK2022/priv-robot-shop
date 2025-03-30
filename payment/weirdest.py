# This is a valid Python file designed to test Tree-sitter edge cases

import os
import json
import rabbitmq
import some.deeply.nested.module as deep_module
from another.module import some_function as renamed_func
from third.module.sub import *

# Simple function - should match
def simple_func(a, b):
    return a + b

# Decorated function - should match
@classmethod
def class_level_method(cls, value):
    print(value)

# Decorator with arguments - might NOT be matched
@retry(times=3)
def retryable_task():
    print("Trying again...")

# Decorated function using dotted name - might NOT be matched
@utils.decorators.log_execution
def decorated_with_dotted():
    pass

# Function inside a class - tree-sitter may or may not pick depending on query depth
class TestClass:

    def __init__(self):
        self.value = 0

    def instance_method(self, x):
        return x * 2

    @staticmethod
    def static_method(a, b):
        return a - b

    @classmethod
    def from_config(cls, cfg):
        return cls()

    # Nested function - usually not matched unless specifically queried
    def outer_function(self):
        def inner_function(y):
            return y ** 2
        return inner_function(4)

# Lambda assigned to a name - not a function_definition node
square = lambda x: x * x

# Function defined via partial or functools - not matchable by normal queries
from functools import partial

def base_func(a, b):
    return a + b

add_five = partial(base_func, 5)

# Function with unusual parameters (e.g., annotations, *args, **kwargs)
def complex_args(a: int, b: str = "hello", *args, **kwargs) -> bool:
    print(a, b)
    return True

# Try-except wrapped function (technically valid, but may be ignored)
try:
    def conditional_func():
        print("Defined in try block")
except Exception:
    pass
