from charactertype import CharacterType
from game import Game
from character import Character

#instantiating an Enum member
my_character_type = CharacterType.WARRIOR

# Acessing name and value
print(my_character_type)
print(my_character_type.name)
print(my_character_type.value)


#Create characters
alice = Character(name="Alice", character_type=CharacterType.WARRIOR, health=100, attack_power= 30)
bob = Character(name="Bob", character_type=CharacterType.MAGE, health= 70, attack_power= 20)

#Start game
game = Game(alice, bob)
game.start_battle()