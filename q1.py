class Game:
    def __init__(self,name, power, health, coins,level):
        self.name = name
        self.power = power
        self.health = health
        self.coins = coins
        self.level = level

    def show_info(self):
        print(f"Name:{self.name}, Power: {self.power}, Health: {self.health}, Coins: {self.coins}, Level: {self.level}")
        print("--------------------------------------------------")

    def is_alive(self):
        if self.health > 0:
            return True
        else:
            return False

    def attack(self, enemy):
        if self.is_alive():
            enemy.health -= self.power
            print(f"{self.name} attacked {enemy.name} and health of {enemy.name} is now {enemy.health}.")
            print("--------------------------------------------------")
        else:
            print(f"{self.name} is dead and cannot attack.")
            print("--------------------------------------------------")

    def earn_coins(self, amount):
        self.coins += amount
        print(f"{self.name} earned {amount} coins and now has {self.coins} coins.")
        print("--------------------------------------------------")

    def buy_potion(self):
        if self.coins>=20:
            self.coins -= 20
            self.health += 30
            print(f"{self.name} bought a potion and now has {self.health} health and {self.coins} coins.")
            print("--------------------------------------------------")
        else:
            print(f"{self.name} does not have enough coins to buy a potion.")
            print("--------------------------------------------------")

    def level_up(self):
        self.level += 1
        self.power += 5
        print(f"{self.name} leveled up to level {self.level}! Power is now {self.power}.")
        print("--------------------------------------------------")

character1 = Game("Hero", 10, 100, 50, 1)
character2 = Game("Villain", 8, 80, 10, 1)
character1.show_info()
character2.show_info()
character1.attack(character2)
character2.buy_potion()
character2.level_up()
character2.earn_coins(15)
character1.is_alive()
character1.show_info()
character2.show_info()