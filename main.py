import random

class Hangman:
    def __init__(self, word):
        self.word = word.lower()
        self.guessed = []

    def guess(self, letter):
        letter = letter.lower()
        if letter in self.guessed:
            print("You already guessed that letter")
        elif letter in self.word:
            self.guessed.append(letter)
            print("You guessed the letter!")
        else:
            self.guessed.append(letter)
            print("You guessed wrong!")

    def get_status(self):
        print("Guess the word:")
        for char in self.word:
            if char in self.guessed:
                print(char, end="")
            else:
                print("_", end="")
        print('\n')

    def check_if_player_won(self):
        for char in self.word:
            if char not in self.guessed:
                return False
        return True

class Game:
    def __init__(self):
        self.word = self.choose_word()
        self.hanged = Hangman(self.word)

    def choose_word(self):
        word_list = ["apple", "banana", "cherry", "dog", "elephant"]
        return random.choice(word_list)

    def play(self):
        while True:
            self.hanged.get_status()
            letter = input("Guess a letter: ")
            self.hanged.guess(letter)
            if self.hanged.check_if_player_won():
                print("You won!")
                break

if __name__ == "__main__":
    game = Game()
    game.play()
