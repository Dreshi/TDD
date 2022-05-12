import pytest


def fizzBuzz(value):
    if isMultiple(value, 3) & isMultiple(value, 5):
        return "FizzBuzz"
    if isMultiple(value, 3):
        return "Fizz"
    elif isMultiple(value, 5):
        return "Buzz"
    return str(value)


def isMultiple( value, mod ):
    return (value % mod) == 0

def checkFizzBuzz(value, expectedRetVal):
    retVal = fizzBuzz(value)
    assert retVal == expectedRetVal


def test_returns1With1PassedIn():
    checkFizzBuzz(1, "1")


def test_returns2With2PassedIn():
    checkFizzBuzz(2, "2")


def test_returnsFizzWhen3PassedIn():
    checkFizzBuzz(3, "Fizz")


def test_returnsBuzzWhen5PassedIn():
    checkFizzBuzz(5, "Buzz")


def test_returnsFizzWhenMultiple3():
    checkFizzBuzz(6, "Fizz")
    checkFizzBuzz(9, "Fizz")


def test_returnsBuzzWhenMultiple5():
    checkFizzBuzz(10, "Buzz")
    checkFizzBuzz(20, "Buzz")


def test_resturnsFizzBuzzWhenMultiple3And5():
    checkFizzBuzz(15, "FizzBuzz")