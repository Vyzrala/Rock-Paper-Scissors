import random as rand


class Player:
    score = -1
    name = None
    move = None

    def __init__(self, name, score):
        self.name = name
        self.score = int(score)
    
    def set_move(self, move):
        self.move = move

    def get_move(self):
        return self.move
    
    def get_score(self):
        return self.score

    def add_score(self, score):
        self.score += score


class Game:
    beats = {"Rock": "Scissors", "Paper": "Rock", "Scissors": "Paper"}
    is_beaten_by = {"Rock": "Paper", "Paper": "Scissors", "Scissors": "Rock"}
    player = None

    def __init__(self):
        self.computer_choice = None
        self.computer_points = None

    def get_player(self):
        player_name = input("Enter your name: ").capitalize()
        print("Hello", player_name)
        with open('data/rating.txt','r') as ratings:
            for line in ratings:
                if player_name in line.split():
                    self.player = Player(player_name, line.split()[1])
        
        if not self.player:
            self.player = Player(player_name, 0)
    
    def computer_turn(self):
        self.computer_choice = rand.choice(list(self.beats.keys()))

    def evaluate_state(self):
        if self.computer_choice == self.player.get_move():
            print("There is a draw ({})".format(self.computer_choice))
            self.player.add_score(50)
        elif self.computer_choice == self.beats[self.player.get_move()]:
            print("Well done. Computer chose {} and failed".format(self.computer_choice))
            self.player.add_score(100)
        elif self.computer_choice == self.is_beaten_by[self.player.get_move()]:
            print("Sorry, but computer chose: {}".format(self.computer_choice))

    def play(self):
        while(True):
            user_input = input("> ")
            if user_input == "!rating":
                print("Your rating:", self.player.get_score())
            elif user_input == "!exit":
                print("Bye!")
                break
            else:
                user_input = user_input.capitalize()
                if user_input not in list(self.beats.keys()):
                    print("Invalid input.")
                    user_input = None
                    continue
                else:
                    self.player.set_move(user_input)
                    self.computer_turn()
                    self.evaluate_state()
                    

def main():
    game = Game()
    game.get_player()
    game.play()

main()