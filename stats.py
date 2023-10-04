class Stats():
    def __init__(self):
        self.reset_stats()
        self.run_game = True
        with open("hight_score.txt", "r") as f:
            self.high_score = int(f.readline())
        
        
    def reset_stats(self):
        self.gun_left = 3
        self.score = 0
    
    