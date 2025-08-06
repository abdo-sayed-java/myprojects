# Rules: 
# 1- computer pick random number from 1 to 10: 
# 2- user guess random number. (3 trails)
# 3- if the user guessed the number correctly, he wins. else he will lose
# 4- all the actions will be logged.
import random

class FileLogger:
    def __init__(self, filename):
        self.filename = filename
        
    def log(self, message):
        try: 
            with open(self.filename, 'a', encoding="utf-8") as f: 
                f.write(message + '\n')
        except Exception as e: 
            print(f"💣 Something wrong in Log In: {e}")

            
class GuessNumber:
    def __init__(self, player_name):
        self.player_name = player_name
        self.secret_number = random.randint(1, 10)
        self.attempts = 3
        self.logger = FileLogger("game_log.txt")
    
    def play(self):
        while self.attempts > 0:
            try:
                guessed_number = int(input("Guess a Number between 1 to 10"))
            except ValueError:
                print('🙊 Please Enter a Valid Number')
                continue
        
            self.attempts -=1 
            
            if guessed_number == self.secret_number:
                print('🥳 Congratulations, You Guessed the number Correctly.')
                self.logger.log(f'🥳 {self.player_name} guessed in {3 - self.attempts} tries!') 
                return
            else:
                print(f'Wrong. {self.attempts} attempts left!')
            
        print(f'☠️ GAME OVER. THe Number was {self.secret_number}')
        self.logger.log(f"Ops!🤡 {self.player_name} failed after 3 attempts!")
        
    
if __name__ == '__main__':
    print("Welcome to Summer Training Guess Game!")
    player = input('Enter Your Name: ')
    game = GuessNumber(player)
    game.play()
