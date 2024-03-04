# Exercise 1: Write a Python Function

def add_numbers(a: int, b: int) -> int:
    return a + b


# Exercise 2: Write a Python Function with Default Parameters

def greet(name: str, greeting: str = 'Hello') -> str:
    return f"{greeting}, {name}!"

# Exercise 3: Working with Lists and Functions


def filter_even_numbers(ints: list[int]) -> list[int]:
    return [i for i in ints if i % 2 == 0]

# Exercise 4: Error Handling in Functions

def divide_numbers(numerator: int, denominator: int) -> float | str:
    return numerator / denominator if denominator != 0 else "Cannot divide by zero."
