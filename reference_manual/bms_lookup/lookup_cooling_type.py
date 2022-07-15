from reference_manual.bms_lookup.lookup import Look_up


class Lookup_cooling_type(Look_up):
    def __init__(self) -> None:
        super().__init__()
        self.battery_characterstics = self.define_cooling_values()

    def get_cooling_type(self, cooling_type):
        return self.battery_characterstics[cooling_type]

    def define_cooling_values(self):
        dictionary = {
            "PASSIVE": "PASSIVE_COOLING",
            "HI_ACTIVE": "HI_ACTIVE_COOLING",
            "MED_ACTIVE": "MED_ACTIVE_COOLING"
        }
        return dictionary
