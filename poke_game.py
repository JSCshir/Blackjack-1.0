import random
import math
from sympy import isprime, nextprime

class Pokemon:

    def __init__(self, hp, skill, atk1, atk2):
        self.hp = hp
        self.skill = skill
        self.atk1 = atk1
        self.atk2 = atk2
        self.lvl = 1
        self.pts = 0

    def atk_f(self, other):
        random_int1 = random.randint(1,4)
        rand_list = []
        for i in range(4):
            rand_list.append(random.randint(1,4))
        if random_int1 in rand_list:
            if self.skill == 'fire' and other.skill == 'ground':
                other.hp -= self.atk1 * 1.25
            elif self.skill == 'water' and other.skill == 'fire':
                other.hp -= self.atk1 * 1.25
            elif self.skill == 'ground' and other.skill == 'lightning':
                other.hp -= self.atk1 * 1.25
            elif self.skill == 'lightning' and other.skill == 'water':
                other.hp -= self.atk1 * 1.25
            elif self.skill == 'ground' and other.skill == 'fire':
                other.hp -= self.atk1 * 0.75
            elif self.skill == 'fire' and other.skill == 'water':
                other.hp -= self.atk1 * 0.75
            elif self.skill == 'lightning' and other.skill == 'ground':
                other.hp -= self.atk1 * 0.75
            elif self.skill == 'water' and other.skill == 'lightning':
                other.hp -= self.atk1 * 0.75
            else: 
                other.hp -= self.atk1
            print('The attack was successful!')
        else:
            print('The attack was unsuccessful!')
            
        if other.hp <= 0:
            print('The opponents pokemon has died!')
            self.pts += 5
            if other.pts <= 5:
                other.pts -= 5
            else:
                other.pts = 0
        else:
            return other.hp

    def atk_s(self, other):
        random_int1 = random.randint(1,4)
        rand_list = []
        for i in range(4):
            rand_list.append(random.randint(1,4))
        if random_int1 in rand_list:
            if self.skill == 'fire' and other.skill == 'ground':
                other.hp -= self.atk2 * 1.25
            elif self.skill == 'water' and other.skill == 'fire':
                other.hp -= self.atk2 * 1.25
            elif self.skill == 'ground' and other.skill == 'lightning':
                other.hp -= self.atk2 * 1.25
            elif self.skill == 'lightning' and other.skill == 'water':
                other.hp -= self.atk2 * 1.25
            elif self.skill == 'ground' and other.skill == 'fire':
                other.hp -= self.atk2 * 0.75
            elif self.skill == 'fire' and other.skill == 'water':
                other.hp -= self.atk2 * 0.75
            elif self.skill == 'lightning' and other.skill == 'ground':
                other.hp -= self.atk2 * 0.75
            elif self.skill == 'water' and other.skill == 'lightning':
                other.hp -= self.atk2 * 0.75
            else: 
                other.hp -= self.atk2
            print('The attack was successful!')
        else:
            print('The attack was unsuccessful!')
            
        if other.hp <= 0:
            print('The opponents pokemon has died!')
            self.pts += 5
            if other.pts <= 5:
                other.pts -= 5
            else:
                other.pts = 0
        else:
            return other.hp

    def NUKE(self, other):
        hint_list = []
        while len(hint_list) < 4:
            num = random.randint(1, 20)
            if not isprime(num) and num not in hint_list:
                hint_list.append(num)
    
        password = [nextprime(num) for num in hint_list]
        print(f"Hint: {hint_list}")
        user_attempt = [int(input(f"Guess: ")) for num in hint_list]
    
        if user_attempt == password:
            other.hp = 0
        else:
            print("Sorry, your guess is incorrect. The correct password is:", password)

        
        if other.hp <= 0:
            print('The opponents pokemon has died!')
            self.pts += 5
            if other.pts <= 5:
                other.pts -= 5
            else:
                other.pts = 0
        else:
            other.hp = other.hp

    def hide(self):
        random_int1 = random.randint(1,4)
        random_int2 = random.randint(1,4)
        if random_int1 == random_int2:
            self.hp *= 1.1
            self.lvl += 1
            return 'Hide was effective!'
        else: 
            return 'Hide was ineffective!'

    def level_up(self):
        if self.pts >= 100:
            self.pts -= 100
            self.hp *= 2
            self.atk_f *= 1.75
            self.atk_s *= 1.5
            self.lvl += 1
            print('You have leveled up!')
        else:
            print('You do not have enough points to level up!')

    def __repr__(self):
        return f'Your pokeman is a {self.skill} type, with {self.hp} hp left! You are curently level {self.lvl}, and {100-self.pts} points away from leveling up!'