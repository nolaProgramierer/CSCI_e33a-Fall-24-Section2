# This page has python style errors
import datetime
import date

# Lorem ipsum dolor sit amet, consectetur adipiscing elit,
# sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
# Habitant morbi tristique senectus et.
# Felis eget velit aliquet sagittis id consectetur.
def foo(a, b, c):
   x = a ** c
   y = b ** c
   if (x + y) > 400:
      print("It's greater than 400!")
   elif (x + y) < 400:
      print("It's less than 400")
   else:
      print("It's 400")


foo(3, 2, 2)


def bar(x, y):
   return x + y


class AnyClass:
   pass


def foobar(x, y):
   return x * y


def StyleFunction():
   pass


baz = foo
if baz is None:
   pass


if x == 1:
   print("x is 1")


dict = {'key1': 'value1', 'key2': 'value2', 'key3': 2001}
dict['key1'] = dict['hello']


def sample(arg2, arg3):
    return arg2 + arg3
