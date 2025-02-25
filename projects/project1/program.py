from Multideck import Multideck
from Game import Game


def main():
    game = Game()
    start_input = input('Do you want to play Bagjack? Enter Yes or No: ').upper()
    if start_input == 'YES':
        game.play_game()
    else:
        print("Have a nice day!")




if __name__ == '__main__':
    main()
