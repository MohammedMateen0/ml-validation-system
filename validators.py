class DataValidator:
    def __init__(self, column_name: str, allow_null: bool = False):
        self.column_name = column_name
        self.allow_null = allow_null
        self._errors: list[str] = []

    @property
    def errors(self) -> list[str]:
        return self._errors.copy()

    @property
    def is_valid(self) -> bool:
        return len(self._errors) == 0

    def validate(self, values: list) -> bool:
        self._errors.clear()

        if not self.allow_null and any(v is None for v in values):
            self._errors.append(f"{self.column_name} has null values")

        return self.is_valid

    def __repr__(self) -> str:
        return f"DataValidator(col={self.column_name}, valid={self.is_valid})"


class RatingValidator(DataValidator):
    def __init__(self, column_name: str, min_r: float = 1.0, max_r: float = 5.0):
        super().__init__(column_name, allow_null=True)
        self.min_r = min_r
        self.max_r = max_r

    def validate(self, values: list) -> bool:
        super().validate(values)

        numerics = [v for v in values if isinstance(v, (int, float))]

        if not numerics:
            self._errors.append("No numeric values found")
            return False

        out = [v for v in numerics if not (self.min_r <= v <= self.max_r)]

        if out:
            self._errors.append(
                f"Rating outside [{self.min_r}, {self.max_r}]: {out[:3]}"
            )

        return self.is_valid