import logging
from typing import Optional, Any

logger = logging.getLogger(__name__)


class MLPipelineError(Exception):
    """Base class for all pipeline-related errors."""


class DataValidationError(MLPipelineError):
    """Raised when input data fails validation."""

    def __init__(self, column: str, issue: str, samples: Optional[list] = None):
        self.column = column
        self.issue = issue
        self.samples = samples or []
        super().__init__(
            f"Validation failed on '{column}': {issue}. "
            f"Bad samples: {self.samples[:3]}"
        )


class ModelNotFoundError(MLPipelineError):
    """Raised when a requested model is not found."""

    def __init__(self, model_id: str, available: list):
        self.model_id = model_id
        self.available = available
        super().__init__(
            f"Model '{model_id}' not found. Available: {available}"
        )


def load_model(model_id: str, registry: dict) -> dict:
    """Simulates loading a model from a registry."""
    conn = None
    try:
        conn = {"url": "db://...", "open": True}

        if model_id not in registry:
            raise ModelNotFoundError(model_id, list(registry.keys()))

        logger.info(f"Model '{model_id}' loaded successfully")
        return registry[model_id]

    except ModelNotFoundError:
        logger.error(f"Model {model_id!r} missing from registry")
        raise

    except Exception as e:
        raise MLPipelineError("Unexpected error loading model") from e

    finally:
        if conn:
            conn["open"] = False
            logger.debug("DB connection closed")


def connect_to_feature_store(url: str) -> dict:
    """Simulates connection to feature store."""
    try:
        if "invalid" in url:
            raise ConnectionError(f"Cannot reach {url}")
        return {"url": url, "connected": True}
    except ConnectionError as e:
        logger.error(f"Connection failed: {url}")
        raise MLPipelineError(f"Feature store unavailable: {url}") from e


def safe_parse_rating(raw: Any, default: float = 3.0) -> float:
    """Safely parse rating with fallback."""
    try:
        return float(raw)
    except (TypeError, ValueError) as e:
        logger.warning(f"Cannot parse rating {raw!r}: {e}. Using {default}")
        return default


def validate_prediction_input(data: dict[str, list]) -> None:
    """Fail-fast validation for model input."""
    required = ["price", "bedrooms", "locality"]

    for col in required:
        if col not in data:
            raise DataValidationError(col, "required column missing")

        nulls = [i for i, v in enumerate(data[col]) if v is None]
        if nulls:
            raise DataValidationError(col, f"{len(nulls)} null values", nulls)