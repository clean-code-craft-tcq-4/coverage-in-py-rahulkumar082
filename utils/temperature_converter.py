class Temperature_convert:
    def temperature_in_c(self, value, unit):
        unit = unit.lower()
        if (unit != 'c'):
            return (value - 32) * 5/9
        return value
