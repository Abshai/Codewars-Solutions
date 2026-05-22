class Guesser:
    def __init__(self, number, lives):
        self.number = number
        self.lives = lives
  
    def guess(self,n):
        if self.lives <= 0:
            raise Exception("Omae wa mo shindeiru")
        elif n != self.number:
            self.lives -= 1
            return False
        else:
            return True