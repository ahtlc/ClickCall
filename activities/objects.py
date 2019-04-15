class Year:
    def __init__(self, year, recieved,answered, unanswered, left,*args, **kwargs):
        self.recieved = recieved
        self.answered = answered
        self.unanswered = unanswered
        self.left = left
        self.year = year