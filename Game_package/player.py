class Player:
    score = 0
    name = None
    move = None

    def __init__(self, name, score):
        self.name = name
        self.score = int(score)
        print("Hello,", self.name)

    def set_move(self, move):
        self.move = move

    def get_move(self):
        return self.move

    def get_score(self):
        return self.score

    def add_score(self, score):
        self.score += score
