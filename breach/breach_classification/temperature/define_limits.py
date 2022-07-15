class Define_limits:
    def __init__(self) -> None:
        self.dictionary = {
            "PASSIVE_COOLING": {
                "lower_limit": 0,
                "upper_limit": 35
            },
            "HI_ACTIVE_COOLING": {
                "lower_limit": 0,
                "upper_limit": 45
            },
            "MED_ACTIVE_COOLING": {
                "lower_limit": 0,
                "upper_limit": 40
            }
        }

    def get_limits_bound(self, cooling_type):
        bound_dict = self.dictionary[cooling_type]
        return (bound_dict['lower_limit'], bound_dict['upper_limit'])
