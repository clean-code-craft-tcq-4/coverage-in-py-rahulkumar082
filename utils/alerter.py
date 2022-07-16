from utils.targets.controller import Target_Controller
from utils.targets.email import Target_Email


class Alerter:
    def send_msg(self, alert_target, breach_type, recepient=None):
        define_target_msg = {
            "TO_CONTROLLER": Target_Controller(breach_type).compose_msg(),
            "TO_EMAIL": Target_Email(recepient, breach_type).compose_msg()
        }
        return define_target_msg[alert_target]
