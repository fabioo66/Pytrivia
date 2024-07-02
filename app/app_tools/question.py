class question:
    """ defines an entity that represents a question in PyTrivia"""
    def __init__ (self, number, options, correct_answer, user_answer, key):
        self.number = number 
        self.options = options 
        self.correct_answer = correct_answer 
        self.user_answer = user_answer
        self.key = key