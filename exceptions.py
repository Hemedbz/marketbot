class MarketbotException(Exception):
    pass


class OutOfRange(MarketbotException):
    def __init__(self, value):
        super().__init__(f"{value} out of range, please choose a number between 1 and 200")

