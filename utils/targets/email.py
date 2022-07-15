class Target_Email:
    def __init__(self, recepient, breach_type) -> None:
        self.recepient = recepient
        self.breach_type = breach_type

    def compose_msg(self):
        breach_msg = f"""To: {self.recepient}\n
        Hi, the temperature is {(self.breach_type).lower().replace('_',' ')}
        """
        dictionary = {
            "TOO_LOW": breach_msg,
            "TOO_HIGH": breach_msg
        }
        return breach_msg
