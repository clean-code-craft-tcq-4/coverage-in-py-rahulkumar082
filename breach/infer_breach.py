class Infer_breach:
    def __init__(self, lower_limit, upper_limit) -> None:
        self.lower_limit = lower_limit
        self.upper_limit = upper_limit

    def compare_value_with_limit(self, value):
        breach_type = "NORMAL"
        if (self.lower_limit > value):
            breach_type = "TOO_LOW"
        if (self.upper_limit < value):
            breach_type = "TOO_HIGH"
        return breach_type
