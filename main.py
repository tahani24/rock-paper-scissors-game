"""This program plays a game of
Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""
import random

moves = ['rock', 'paper', 'scissors']
"""The Player class is the parent class
 for all of the Players in this game"""


class Player:
    def __init__(self):
        self.m1 = ''
        self.m2 = ''

    def learn(self, my_move, their_move):
        self.m1 = my_move
        self.m2 = their_move


class rockPlayer(Player):
    def move(self):
        return 'rock'


class randomPlayer(Player):
    def move(self):
        return random.choice(moves)


class reflectPlayer(Player):

    def move(self):
        return self.m2


class cyclePlayer(Player):

    def move(self):
        x = self.m1.lower()
        if x == 'paper':
            return 'scissors'
        elif x == 'scissors':
            return 'rock'
        else:
            return 'paper'


class humanPlayer(Player):

    def move(self):
        while (True):
            m = input("Rock, paper, scissors? ").lower()
            if m in moves:
                return m


class Game:

    score1 = 0
    score2 = 0
    move1 = ''
    move2 = ''

    def __init__(self, p1, p2):

        self.p1 = p1
        self.p2 = p2

    def play_round(self):
        self.move1 = self.p1.move()
        self.move2 = self.p2.move()

        if self.beats(self.move1, self.move2):
            self.score1 += 1
        elif self.beats(self.move2, self.move1):
            self.score2 += 1

        print(f"Player 1: {self.move1}  Player 2: {self.move2}")

        if self.beats(self.move1, self.move2):
            print("you won !")
        elif self.beats(self.move2, self.move1):
            print("you lose !")
        else:
            print("Draw ...")

        print(f"Score: Player One {self.score1}, Player Two {self.score2}")

        self.p1.learn(self.move1, self.move2)
        self.p2.learn(self.move2, self.move1)

    def play_game(self):
        print("Game start!")

        for round in range(4):
            print(f"Round {round}:")
            self.play_round()

        self.winner()
        print(f"final score:player one {self.score1},player tow {self.score2}")
        print("Game over!")

    def winner(self):
        s1 = self.score1
        m1 = self.move1
        s2 = self.score2
        m2 = self.move2

        if s1 > s2:
            return print(f"Congrats! ,you won at move {m1}")
        elif s1 < s2:
            return print(f"you lose! ,player 2 won at move {m2}")
        else:
            return print("No one won or lose !")

    def beats(self, one, two):
        return ((one == 'rock' and two == 'scissors') or
                (one == 'scissors' and two == 'paper') or
                (one == 'paper' and two == 'rock'))


if __name__ == '__main__':
    players = [
        rockPlayer(),
        randomPlayer(),
        reflectPlayer(),
        cyclePlayer()
    ]

    p1 = humanPlayer()
    p2 = random.choice(players)
    game = Game(p1, p2)
    game.play_game()
