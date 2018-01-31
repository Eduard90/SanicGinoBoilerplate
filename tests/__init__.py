import asyncio
from unittest import TestCase


def async_decorator(f):
    def inner_func(self):
        self.loop.run_until_complete(f(self))

    return inner_func


class TestCaseMeta(type):
    def __new__(mcs, name, bases, attrs, **kwargs):
        for name, val in attrs.items():
            if asyncio.iscoroutinefunction(val):
                attrs[name] = async_decorator(val)
        instance = super().__new__(mcs, name, bases, attrs, **kwargs)
        instance.loop = asyncio.get_event_loop()
        return instance


class BaseTestCase(TestCase, metaclass=TestCaseMeta):
    loop = None
