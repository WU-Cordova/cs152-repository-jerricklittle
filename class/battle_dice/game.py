import random
from character import Character

class Game:
    """Manages the Dice Battle Game Logic"""
    
    def __init__(self, player1: Character, player2: Character):
        """Initializes a game with two players"""
        self.__player1 = player1
        self.__player2 = player2

    def attack(self, attacker: Character, defender: Character):
        """Performs an attack where the attacker rolls a die to determine damage dealt"""
        damage_factor: int = random.randint(1, 6)
        defender.health -= damage_factor * attacker.attack_power
        print(f"{attacker.name} attacks {defender.name} for {damage_factor} damage!")
        print(f"{defender.name} now has {max(0, defender.health)} health remaining.\n")
    def start_battle(self):
        """Starts a turn based battle between two players"""
        print(f"Battle Start: {self.__player1.name} vs {self.__player2.name}\n")
        turn: int = 0
        
        while self.__player1.health > 0 and self.__player2.health > 0:
            if turn % 2 == 0:
                self.attack(self.__player1, self.__player2)
            else:
                self.attack(self.__player2, self.__player1)
            
            turn += 1
        
        winner: Character = self.__player1 if self.__player1.health > 0 else self.__player2
        print(f"{winner.name} wins the battle!")
    
