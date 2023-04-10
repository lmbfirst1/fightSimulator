import random
import cowsay

class Player:
    def __init__(self, name, health):
        self.name = name
        self.health = health
        self.attack_zone = None
        self.defend_zone = None

    def choose_attack_zone(self):
        self.attack_zone = input("Выберите зону атаки (1 - голова, 2 - тело, 3 - ноги): ")
        while self.attack_zone not in ["1", "2", "3"]:
            self.attack_zone = input("Выберите зону атаки (1 - голова, 2 - тело, 3 - ноги): ")

    def choose_defend_zone(self):
        self.defend_zone = input("Выберите зону защиты (1 - голова, 2 - тело, 3 - ноги): ")
        while self.defend_zone not in ["1", "2", "3"]:
            self.defend_zone = input("Выберите зону защиты (1 - голова, 2 - тело, 3 - ноги): ")

    def attack(self, opponent):
        if self.attack_zone == opponent.defend_zone:
            opponent.health -= 2
            print(f"{opponent.name} заблокировал атаку, получив 2 единицы урона!")
        else:
            opponent.health -= 5
            print(f"{opponent.name} получил 5 единиц урона!")

    def is_alive(self):
        return self.health > 0

    def reset_health(self):
        self.health = 30


class ComputerPlayer(Player):
    def choose_attack_zone(self):
        self.attack_zone = str(random.randint(1, 3))
        print(f"{self.name} выбрал зону атаки: {self.attack_zone}")

    def choose_defend_zone(self):
        self.defend_zone = str(random.randint(1, 3))
        print(f"{self.name} выбрал зону защиты: {self.defend_zone}")


def main():
    player = Player(input( cowsay.cow("КТО ТЫ, ВОИН ? " ) ), 30)
    opponents = [
        ComputerPlayer("Чупокабра 1", 15),
        ComputerPlayer("Пирожочек 2", 20),
        ComputerPlayer("Главный ППСник 3", 25),
    ]

    for i, opponent in enumerate(opponents, start=1):
        print(f"Раунд {i}. Сражайтесь с {opponent.name}!")
        while player.is_alive() and opponent.is_alive():
            player.choose_attack_zone()
            player.choose_defend_zone()
            opponent.choose_attack_zone()
            opponent.choose_defend_zone()
            player.attack(opponent)
            opponent.attack(player)
            print(f"Вы: {player.health}. {opponent.name}: {opponent.health}")

        if player.is_alive():
            player.reset_health()
            print(cowsay.get_output_string(f"trex","Поздравляю, Воин! Ты победил очережного врага!"))
            #print(f"Поздравляю,{player.name}! ты победил грозного: {opponent.name}")
        else:
            print(f"К сожалению, {opponent.name} одержал победу.")


if __name__ == "__main__":
    main()