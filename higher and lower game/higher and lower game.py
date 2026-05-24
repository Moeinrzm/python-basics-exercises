#higher and lower game
import random 
class Game ():
    def __init__(self):
        self.random_number=random.randint(0,100)
        self.is_running=True
    def check_guess(self,user_guess):
        if user_guess==self.random_number:
            print("you gaused right!!")
            self.is_running=False
        elif user_guess>self.random_number:
            print("your gause is higher than the target")
        else :
            print("your gause is lower than the target")
    def get_user_input(self):
        while True:
            user_guess=input("please enter a integer between 0-100:\t")
            try:
                val=int(user_guess)
                break
            except ValueError :
                print("enter a integer  please!!")
        return val    
game=Game()  
while game.is_running:
    guess = game.get_user_input()
    game.check_guess(guess)