from breach.breach_classification.temperature.define_limits import Define_limits
from breach.infer_breach import Infer_breach


class Temperature_Breach(Define_limits):
    def __init__(self) -> None:
        super().__init__()
        self.lower_limit = 0
        self.upper_limit = 0

    def get_limits(self, cooling_type, temperature):
        self.lower_limit, self.upper_limit = self.get_limits_bound(cooling_type)
        infer_breach_obj = Infer_breach(self.lower_limit, self.upper_limit)
        return infer_breach_obj.compare_value_with_limit(temperature)
