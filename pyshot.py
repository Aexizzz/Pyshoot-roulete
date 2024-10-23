import random
from itertools import count
from random import choice
from sys import breakpointhook
from time import sleep


class Pyshot:
    clip = []
    lives_player = 4
    dealer_player = 4
    clip_v = [0,1]
    clip_sort = []
    win = 0
    money = 4
    lose = 0
    dd = 0
    skip = 0
    skip_chek = 0
    heal = 0
    damage = 1
    dd_dealer = 0
    skip_dealer = 0
    skip_chek_dealer = 0
    heal_dealer = 0
    damage_dealer = 1
    def gen(self):
        for i in range(random.randint(2, 10)):
            self.clip.append(random.choice(self.clip_v))
    def doubledamage(self):
        self.damage = 2
    def new_game(self):
        self.clip = []
        self.lives_player = 4
        self.dealer_player = 4
        self.clip_sort = []
    def heal_box(self):
        self.lives_player+=1
        self.heal-=1
    def static(self):
        print("\n" * 10)
        print(f"STATISTIC:\nYOU WIN: {self.win}\nYOU LOSE: {self.lose}\nMONEY: {self.money}\nDOUBLE DAMAGE: {self.dd}\nHEAL BOX: {self.heal}\nSKIP DEALER SHOOT: {self.skip}")
    def shop(self):
        print("\n" * 10)
        choice = input("SHOP:\n1)DOUBLE DAMAGE --- 3 wins\n2)SKIP SHOOT DEALER --- 2 wins\n3)HEAL BOX --- 2 wins")
        if choice == "1" and self.money>2:
            self.dd += 1
            self.dd_dealer += 1
            self.money -= 3
        elif choice == "2" and self.money>1:
            self.skip += 1
            self.skip_dealer += 1
            self.money -= 2
        elif choice == "3" and self.money>1:
            self.heal += 1
            self.heal_dealer += 1
            self.money -= 2
        elif choice == "1" and self.money<3:
            print("YOU ARE HAVE NOT MANY MONEY TO THIS")
            pass
        elif choice == "2" and self.money < 2:
            print("YOU ARE HAVE NOT MANY MONEY TO THIS")
            pass
        elif choice == "3" and self.money<2:
            print("YOU ARE HAVE NOT MANY MONEY TO THIS")
            pass
    def player_choice(self):
        print("\n"*20)
        print(sorted(self.clip))
        print("YOU ARE SHOOTING")

        choice = input(f"Shot to:\n1)YOU \n2)Dealer\n3)Double Damage\n4)Heal Box\n5)Skip Shoot Dealer")
        sleep(0.5)
        if choice == "1" and self.clip[0] == 1:
            self.lives_player -= self.damage
            print("Player hp:", self.lives_player)
            print("Dealer hp:", self.dealer_player)
            self.clip.remove(self.clip[0])
            self.damage=1
            if self.skip_chek == 1:
                self.skip_chek = 0
                self.player_choice(Pyshot)
        elif choice == "1" and self.clip[0] == 0:
            print("Player hp:", self.lives_player)
            print("Dealer hp:", self.dealer_player)
            self.clip.remove(self.clip[0])
            self.damage = 1
            if self.skip_chek == 1:
                self.skip_chek = 0
                self.player_choice(Pyshot)
            if len(self.clip)>1:
                self.player_choice(Pyshot)
        elif choice == "2" and self.clip[0] == 0:
            print("Player hp:", self.lives_player)
            print("Dealer hp:", self.dealer_player)
            self.clip.remove(self.clip[0])
            self.damage = 1
            if self.skip_chek == 1:
                self.skip_chek = 0
                self.player_choice(Pyshot)
        elif choice == "2" and self.clip[0] == 1:
            self.dealer_player -=self.damage
            print("Player hp:", self.lives_player)
            print("Dealer hp:", self.dealer_player)
            self.clip.remove(self.clip[0])
            self.damage = 1
            if self.skip_chek == 1:
                self.skip_chek = 0
                self.player_choice(Pyshot)
        elif choice == "3" and self.dd > 0:
            self.doubledamage(Pyshot)
            self.dd-=1
            self.player_choice(Pyshot)
        elif choice == "3" and self.dd ==0:
            print("YOU ARE HAVE NOT DOUBLE DAMAGE")
            self.player_choice(Pyshot)
        elif choice == "4" and self.heal > 0:
            self.heal_box(Pyshot)
            self.player_choice(Pyshot)
        elif choice == "4" and self.heal ==0:
            print("YOU ARE HAVE NOT HEAL BOX")
            self.player_choice(Pyshot)
        elif choice == "5" and self.skip > 0:
            self.skip_chek = 1
            self.skip-=1
            self.player_choice(Pyshot)
        elif choice == "4" and self.heal ==0:
            print("YOU ARE HAVE NOT SKIPS DEALER SHOOT")
    def dealer_choice(self):
        print("\n" * 20)
        print("DEALER IS SHOOTING")
        sleep(0.5)
        if self.dd_dealer > 0 and self.lives_player<3 and random.randint(1, 2)==1:
            self.damage_dealer = 2
            self.dd_dealer -=1
            print("DEALER USE DOUBLE DAMAGE")
        if self.dealer_player <=2 and self.heal_dealer >0 and random.randint(1,2) == 1:
            self.dealer_player+=1
            self.heal_dealer -=1
            print("DEALER USE HEAL BOX")
        if self.clip.count(1)/len(self.clip)>0.75:
            if random.randint(1, 3) == 1 and self.skip_dealer >0:
                self.skip_chek_dealer = 1
                self.skip_dealer -=1
                print("DEALER USE SKIP YOUR SHOOT")
        if self.clip.count(1) >= self.clip.count(0):
            choice = "2"
            print("DEALER IS SHOOTING TO YOU")
        else:
            choice = "1"
            print("DEALER IS SHOOTING TO HIMSELF")
        sleep(0.5)
        if choice == "1" and self.clip[0] == 1:
            self.dealer_player -= self.damage_dealer
            print("Player hp:", self.lives_player)
            print("Dealer hp:", self.dealer_player)
            self.clip.remove(self.clip[0])
            self.damage_dealer = 1
            if self.skip_chek_dealer == 1:
                self.skip_chek_dealer = 0
                self.dealer_choice(Pyshot)
        elif choice == "1" and self.clip[0] == 0:
            print("Player hp:", self.lives_player)
            print("Dealer hp:", self.dealer_player)
            self.clip.remove(self.clip[0])
            self.damage_dealer = 1
            if self.skip_chek_dealer == 1:
                self.skip_chek_dealer = 0
                self.dealer_choice(Pyshot)
            if len(self.clip) > 1:
                self.dealer_choice(Pyshot)
        elif choice == "2" and self.clip[0] == 0:
            print("Player hp:", self.lives_player)
            print("Dealer hp:", self.dealer_player)
            self.clip.remove(self.clip[0])
            self.damage_dealer = 1
            if self.skip_chek_dealer == 1:
                self.skip_chek_dealer = 0
                self.dealer_choice(Pyshot)
        elif choice == "2" and self.clip[0] == 1:
            self.lives_player -=self.damage_dealer
            print("Player hp:", self.lives_player)
            print("Dealer hp:", self.dealer_player)
            self.clip.remove(self.clip[0])
            self.damage_dealer = 1
            if self.skip_chek_dealer == 1:
                self.skip_chek_dealer = 0
                self.dealer_choice(Pyshot)
    def play(self):
        while self.lives_player > 0 and self.dealer_player > 0:
            if self.clip == []:
                sleep(0.5)
                print("NEW CLIP")
                self.gen(Pyshot)
            self.player_choice(Pyshot)
            if self.lives_player <= 0:
                print("YOU DEAD, DEALER WIN")
                self.lose +=1
                break
            elif self.dealer_player <= 0:
                print("DEALER DEAD, YOU WIN")
                self.win +=1
                self.money += 1
                break
            if self.clip == []:
                sleep(0.5)
                print("NEW CLIP")
                self.gen(Pyshot)
            self.dealer_choice(Pyshot)
            if self.lives_player <= 0:
                print("YOU DEAD, DEALER WIN")
                self.lose +=1
                break
            elif self.dealer_player <= 0:
                print("DEALER DEAD, YOU WIN")
                self.money += 1
                self.win +=1
                break
    def infiniti_game(self):
        self.static(Pyshot)
        choice = input("MENU:\n 1)PLAY\n 2)LEAVE\n 3)SHOP\n ------> ")
        if choice == "1":
            print(f"DEALERS ITEM:\nDOUBLE DAMAGE: {self.dd_dealer}\nHEAL BOX: {self.heal_dealer}\nSKIP YOUR SHOOT: {self.skip_dealer}")
            self.play(Pyshot)
        elif choice == "2":
            self.leave(Pyshot)
        elif choice == "3":
            self.shop(Pyshot)
    def leave(self):
        quit(Pyshot)
game = Pyshot
game.gen(Pyshot)
while True:
    game.infiniti_game(Pyshot)
    game.new_game(Pyshot)


