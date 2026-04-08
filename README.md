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
    ```
'''
## Day 3 Updates (Exception Handling)

Implemented a structured exception system for ML pipelines.

### Features
- Custom exception hierarchy (`MLPipelineError`)
- Fail-fast validation (`DataValidationError`)
- Model loading errors (`ModelNotFoundError`)
- Exception chaining (`raise ... from e`)
- Graceful fallback (`safe_parse_rating`)

### Concepts Covered
- try / except / else / finally
- custom exceptions
- exception propagation
- logging integration
- fail-fast vs graceful fallback