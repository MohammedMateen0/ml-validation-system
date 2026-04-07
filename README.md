# ML Validation System (Week 1 - Day 1)

## Overview
This project demonstrates Object-Oriented Programming (OOP) concepts by building a reusable data validation system.

## Features
- BankAccount class (OOP fundamentals)
- DataValidator base class (abstraction)
- RatingValidator (inheritance + method overriding)
- Clean validation structure

## Concepts Covered
- Classes and objects
- Encapsulation
- Inheritance
- Method overriding
- `super()`
- `@property`
- `__repr__`

## Example

```python
validator = RatingValidator("rating")
data = [1, 2, 3, 6]

validator.validate(data)

print(validator.errors)
```
## Day 2 Updates (Decorators)

Added reusable decorators:
- `@timer` — measures execution time
- `@retry` — retries failed operations

### Concepts Covered
- First-class functions
- Closures
- Decorators
- Decorator factories
- `functools.wraps`

### Example

```python
@timer
def validate(...):
    ...
