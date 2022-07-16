from breach.breach_classification.temperature.classify_temperature_breach import Temperature_Breach
from reference_manual.bms_lookup.lookup_cooling_type import Lookup_cooling_type
from utils.alerter import Alerter
from utils.console_print import Print_On_Console
from utils.temperature_converter import Temperature_convert


class Check_and_Alert(Lookup_cooling_type, Temperature_convert, Alerter, Print_On_Console):
    def __init__(self) -> None:
        super().__init__()
        self.breach_obj_dict = {
            'temperature': Temperature_Breach()
        }

    def typewise_alert(self, cooling_type, alert_target, recepient, bms_factor_arr=['temperature'], value_arr=[None]):
        for index in range(len(bms_factor_arr)):
            factor_type, factor_value = self.tune_values(bms_factor_arr[index], value_arr[index])
            breach_type = self.get_breach_type(cooling_type, factor_type, factor_value)
            msg = self.send_msg(alert_target, breach_type, recepient)
            self.print_msg(msg)
            return msg

    def get_breach_type(self, cooling_type, factor_type, factor_value):
        breach_type = None
        cooling_type = self.get_cooling_type(cooling_type)
        factor_type, factor_value = self.tune_values(factor_type, factor_value)
        breach_type = self.breach_obj_dict[factor_type].get_limits(cooling_type, factor_value)
        return breach_type

    def tune_values(self, factor_type, factor_value):
        dictionary = {
            'temperature': self.temperature_in_c(factor_value, 'c')
        }
        return factor_type, dictionary[factor_type]
