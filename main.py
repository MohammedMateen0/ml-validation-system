from bank_account import BankAccount
from validators import RatingValidator
import logging
from exceptions import (
    load_model,
    safe_parse_rating,
    validate_prediction_input,
    ModelNotFoundError,
    DataValidationError,
)
from utils import normalize, apply_transform, parse_price

def run_bank_demo():
    acc=BankAccount("Mateen",1000)
    acc.deposit(500)
    acc.withdraw(200)
    print(acc)

def run_validator_demo():
    data=[1,2,3,6,None]
    validator = RatingValidator('rating')
    validator.validate(data)
    print("Valid: ", validator.is_valid)
    print("Error: ",validator.errors)


logging.basicConfig(level=logging.INFO)

registry = {
    "xgb_v1": {"type": "xgboost"},
    "lgb_v1": {"type": "lgbm"},
}


def run_exceptions_demo():
    # Model loading
    try:
        load_model("missing_model", registry)
    except ModelNotFoundError as e:
        print(f"Handled: {e}")

    # Safe parsing
    print(safe_parse_rating("NEW"))
    print(safe_parse_rating("4.5"))

    # Validation
    try:
        validate_prediction_input(
            {"price": [100, None], "bedrooms": [2], "locality": ["HYD"]}
        )
    except DataValidationError as e:
        print(f"Column: {e.column} | Issue: {e.issue}")
def run_utils_demo():
    print(normalize([10, 20, 30]))

    result = apply_transform([1.0, 4.0, 9.0], lambda x: x ** 0.5)
    print(result)

    print(parse_price("₹1,200"))


if __name__=='__main__':
    run_bank_demo()
    run_validator_demo()
    run_exceptions_demo()
    run_utils_demo()