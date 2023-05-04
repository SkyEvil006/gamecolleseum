from random import randint
from abc import ABC, abstractmethod
from time import sleep
class Hero(ABC):
    def hit(self):
        pass
    def defence(self):
        pass

class Weapon():
    def __init__(self,name,attack):
        self.attack = attack
        self.name = name


class Warrior(Hero):
    def __init__(self,name, hp, attack,weapon, armor, energy):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.weapon = weapon
        self.armor = armor
        self.energy = energy


# Функция атаки класса Warrior, кажда атака отнимает от 20 до 33 едениц выносливости
# когда энергии недостаточно, то воин начинает наносить удары в два раза слабее.
# Сперва атаки отнимают броню у соперника, затем здоровье.
    def hit(self, other):
        if self.energy >= 20:
            attack = self.attack + self.weapon.attack
        elif self.energy <= 19:
            attack = (self.attack + self.weapon.attack) // 2
        if other.armor >= 1:
            other.armor -= attack
            self.energy -= randint(20,33)
            if self.energy <= 19:
                self.energy = 0
            if self.armor <0 :
                self.armor = 0
        elif other.armor < 1:
            other.hp -= attack
            self.energy -= randint(20,33)
            if self.energy <= 19:
                self.energy = 0

    def defence(self,other):
        self.hp += self.armor

class Archer(Hero):
    def __init__(self,name,hp,attack,crit_chance, weapon, armor,energy):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.crit_chance = crit_chance
        self.weapon = weapon
        self.armor = armor
        self.energy = energy

#Функция атаки класса Archer, сделана так же как и функция атаки класса Warrior,
#олтичие функции в том, что у арчера есть возможность нанести критический урон. К сожалению мне не удалось реализовать
#корректное отображение критического удара в консоле, урон всегда отображается как не критичкский, хотя урон
#наностся двойной.


    def hit(self,other):
        check = randint(0,100)
        if check <= self.crit_chance:
            attack = (self.attack + self.weapon.attack) * 2
            print('Критическая атака')
        else:
            if self.energy >= 20:
                attack = self.attack + self.weapon.attack
            elif self.energy <=19:
                attack = (self.attack + self.weapon.attack) // 2
        if other.armor >=1:
            other.armor -= attack
            self.energy -= randint(20,33)
            if self.energy <= 19:
                self.energy = 0
            if self.armor <0 :
                self.armor = 0
        elif other.armor < 1:
            other.hp -= attack
            self.energy -= randint(20,33)
            if self.energy <= 19:
                self.energy = 0





class Battle:
    @staticmethod
    #Функция battle сообщает нам между кем проводится бой, затем проверяет количество здоровья
    #и если оно менее 10 - дает игроку выбор, казнить героя или оставить в живых.
    #так же в функции реализована система боя и отображение её в консоле, так же учтено отображение урона
    #у учетом того есть у героя выносливость или нет. В конце добавлена задержка 0.4 секунды, для постепенного
    #отображения битвы в консоле
    def battle(player_one,player_two):
        print(f'Битва между {player_one.name} и {player_two.name}')
        while True:
            if player_one.hp <=10:
                choise = input(f'{player_two.name} победил! Хотите казнить {player_one.name}? Напишите ДА или НЕТ\n')
                if choise == 'ДА' or 'да' or 'Да':
                    print(f'Жизнь {player_one.name} окончена!')
                    break
                elif choise == 'НЕТ' or 'нет' or 'Нет':
                    print(f'{player_one.name} остался жив и пошел копить силы для нового боя')
                    break
            if player_two.hp <=10:
                choise = input(f'{player_one.name} победил! Хотите казнить {player_two.name}? Напишите ДА или НЕТ\n')
                if choise == 'ДА' or 'да' or 'Да':
                    print(f'Жизнь {player_two.name} окончена!')
                    break
                elif choise == 'НЕТ' or 'нет' or 'Нет':
                    print(f'{player_two.name} остался жив и пошел копить силы для нового боя')
                    break
            who = randint(0,1)
            if who ==0:
                player_one.hit(player_two)
                if player_one.energy >= 20:
                    print(f'{player_one.name} ударил {player_two.name} на {player_one.attack+player_one.weapon.attack} '
                        f'урона, и его HP теперь равно '
                        f'{player_two.hp}, а броня равна {player_two.armor}, выносливость {player_one.name} '
                        f'равна {player_one.energy}')
                elif player_one.energy <= 19:
                    print(f'{player_one.name} ударил {player_two.name} на '
                          f'{(player_one.attack+player_one.weapon.attack) // 2} '
                        f'урона, и его HP теперь равно '
                        f'{player_two.hp}, а броня равна {player_two.armor}, выносливость {player_one.name} '
                        f'равна {player_one.energy}')

            elif who ==1:
                player_two.hit(player_one)
                if player_one.energy >= 20:
                    print(f'{player_two.name} ударил {player_one.name} на {player_two.attack+player_two.weapon.attack} '
                        f'урона, и его HP теперь равно '
                        f'{player_one.hp}, а броня равна {player_one.armor}, выносливость {player_two.name} '
                        f'равна {player_one.energy}')
                elif player_one.energy <= 19:
                    print(f'{player_two.name} ударил {player_one.name} на '
                          f'{(player_two.attack+player_two.weapon.attack) // 2} '
                        f'урона, и его HP теперь равно '
                        f'{player_one.hp}, а броня равна {player_one.armor}, выносливость {player_two.name} '
                        f'равна {player_two.energy}')

            sleep(0.2)


# name, hp, attack,weapon, armor, energy
w1 = Warrior('Arteas', 200,3,Weapon('Damascus', 5),100,100)

# name,hp,attack,crit_chance, weapon, armor,energy
w2 = Archer('Legolas', 100,3,50, Weapon('Draconic bow', 10),100,100)

Battle.battle(w1,w2)