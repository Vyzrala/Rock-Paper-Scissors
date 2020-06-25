import random as rand


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


class Game:
    default_beats = {"rock": ["scissors"], "paper": ["rock"], "scissors": ["paper"]}
    default_is_beaten_by = {"rock": ["paper"], "paper": ["scissors"], "scissors": ["rock"]}
    beats = {}
    is_beaten_by = {}
    player = None

    def __init__(self):
        self.computer_choice = None
        self.computer_points = None

    def get_player(self):
        player_name = input("Enter your name: ").capitalize()
        with open('data/rating.txt','r') as ratings:
            for line in ratings:
                if player_name in line.split():
                    self.player = Player(player_name, line.split()[1])
        
        if not self.player:
            self.player = Player(player_name, 0)
        
        self.get_game_scope()

    def get_game_scope(self):
        scope = input("Scope> ")
        if not scope:
            self.beats = self.default_beats
            self.is_beaten_by = self.default_is_beaten_by
        else:
            scope = scope.split(",")
            half = int(len(scope)//2)
            for i in range(len(scope)):
                key = scope[i]
                scope_copy = scope.copy()
                values = scope.copy()
                values.remove(key)
                values.extend(values)
                tmp = values[i:i+half]
                tmp.append(key)
                for x in tmp:
                    scope_copy.remove(x)
                self.create_game_scope(key, values[i:i+half], scope_copy)
    
    def create_game_scope(self, key, beating, is_beaten):
        self.is_beaten_by.update({key: beating})
        self.beats.update({key: is_beaten})

    def computer_turn(self):
        self.computer_choice = rand.choice(list(self.beats.keys()))

    def evaluate_state(self):
        if self.computer_choice == self.player.get_move():
            print("There is a draw ({})".format(self.computer_choice))
            self.player.add_score(50)
        elif self.computer_choice in self.beats[self.player.get_move()]:
            print("Well done. Computer chose {} and failed".format(self.computer_choice))
            self.player.add_score(100)
        elif self.computer_choice in self.is_beaten_by[self.player.get_move()]:
            print("Sorry, but computer chose: {}".format(self.computer_choice))

    def play(self):
        print("Okay, let's start")
        while(True):
            user_input = input("> ").lower()
            if user_input == "!rating":
                print("Your rating:", self.player.get_score())
            elif user_input == "!exit":
                print("Bye!")
                break
            else:
                user_input = user_input
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
    del game

main()

# sample options to play with:
# 1. 
# rock,paper,scissors,lizard,spock
# 2. 
# rock,gun,lightning,devil,dragon,water,air,paper,sponge,wolf,tree,human,snake,scissors,fire