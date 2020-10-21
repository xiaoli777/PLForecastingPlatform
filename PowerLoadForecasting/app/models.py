class PredictList:
    def __init__(self,date = [], real = [], predict =[], MAPE = 0):
        self.date = date
        self.real = real
        self.predict = predict
        self.MAPE = MAPE

class Weather:
    def __init__(self, date = [], AverSPress =[], LowTemper = [], HighTemper = [], AverTemper =[], LowPress = [], HighPress = [], AverPress =[]):
        self.date = date
        self.AverSPress = AverSPress
        self.LowTemper = LowTemper
        self.HighTemper = HighTemper
        self.AverTemper = AverTemper
        self.LowPress = LowPress
        self.HighPress = HighPress
        self.AverPress = AverPress

class SimilarDays:
    def __init__(self, date = [], sign =[]):
        self.date = date
        self.sign = sign