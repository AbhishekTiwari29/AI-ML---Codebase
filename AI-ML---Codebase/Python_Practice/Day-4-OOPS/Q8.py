class Player:
    count = 0
    def __init__(self,name,level):
        self.name = name
        self.level = level
        Player.count +=1

    def show_player(self):
        print(self.name,self.level)

    def player_count(self):
        print(Player.count)

p1 = Player("Abhishek",50)
p2 = Player("Rohan",20)
p3 = Player("Rohit",40)

p1.show_player()
p2.show_player()
p3.show_player()
p1.player_count()
