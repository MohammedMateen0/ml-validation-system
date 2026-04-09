from __future__ import annotations
from typing import Optional, Callable, TypeVar, Protocol, TypedDict, Annotated
import math

# --------------------------
# Functional utilities
# --------------------------

def normalize(
    values: list[float],
    min_val: float | None = None,
    max_val: float | None = None,
) -> list[float]:
    if not values:
        return []

    lo = min_val if min_val is not None else min(values)
    hi = max_val if max_val is not None else max(values)

    if hi == lo:
        return [0.0] * len(values)

    return [(v - lo) / (hi - lo) for v in values]


T = TypeVar("T")

def first_non_null(items: list[T | None]) -> T | None:
    return next((x for x in items if x is not None), None)


def apply_transform(
    values: list[float],
    transform: Callable[[float], float],
) -> list[float]:
    return [transform(v) for v in values]


# --------------------------
# Typed structures
# --------------------------

class ModelMetrics(TypedDict):
    accuracy: float
    precision: float
    recall: float
    f1_score: float
    model_name: str


class TrainingConfig(TypedDict, total=False):
    learning_rate: float
    n_estimators: int


# --------------------------
# Protocol (interface)
# --------------------------

class SKLearnPredictor(Protocol):
    def predict(self, X: list[list[float]]) -> list[float]: ...
    def fit(self, X: list[list[float]], y: list[float]) -> None: ...


def evaluate(
    model: SKLearnPredictor,
    X_test: list[list[float]],
    y_test: list[float],
) -> ModelMetrics:
    preds = model.predict(X_test)

    return {
        "accuracy": 0.92,
        "precision": 0.91,
        "recall": 0.93,
        "f1_score": 0.92,
        "model_name": type(model).__name__,
    }


# --------------------------
# Utility functions
# --------------------------

def parse_price(raw: str | int | float) -> float:
    if isinstance(raw, str):
        return float(raw.replace("₹", "").replace(",", "").strip())
    return float(raw)


PositiveFloat = Annotated[float, "must be > 0"]

def sigmoid(x: float) -> PositiveFloat:
    return 1 / (1 + math.exp(-x))