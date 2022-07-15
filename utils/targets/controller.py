class Target_Controller:
    def __init__(self, breach_type) -> None:
        self.header = 0xfeed
        self.breach_type = breach_type

    def compose_msg(self):
        breach_msg = f"{self.header}, {self.breach_type}"
        return breach_msg
