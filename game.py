from random import randrange
from time import sleep
class Character:
    def __init__(self, ATT, DEF, CON, name):
        self.ATT= int(ATT/3)
        self.DEF=DEF
       # if DEF>15:
       #     self.DEF=15+(2*(DEF-15))
        self.CON=CON
        self.HP = 30 + CON/2
        self._defenceHP= self.HP
        self.name=name

    def removeHP(self, hp):
        self.HP -= hp
    
    def defend(self):
        self._def= self._def+self._con/2
        
    def endDefense(self):
        self._def= self._def-self._con/2
    
    @property
    def DEF(self):
        return self._def
    
    @DEF.setter
    def DEF(self, DEF):
        self._def = DEF
    
    @property
    def ATT(self):
        return self._att
    
    @ATT.setter
    def ATT(self, ATT):
        self._att = ATT
        
    @property
    def CON(self):
        return self._con
    
    @CON.setter
    def CON(self, CON):
        self._con = CON
    

def Roll(dice, bonus=0):
    return randrange(1, dice) + bonus

def Attack(playerAttacking, playerDefending):
    ATT = playerAttacking.ATT
    DEF = playerDefending.DEF
    ATT  += Roll(20)
    if ATT >= DEF:
        dmg=Roll(10)
        playerDefending.removeHP(dmg)
        print(f"{playerAttacking.name} dealt {dmg} damage to {playerDefending.name}, {playerDefending.HP} HP remaining, Attack score: {ATT}, Defence score: {DEF}")
        
    else:
        print(f"Attack unsuccessful, Attack score: {ATT}, Defence score: {DEF}")
    
player1 = Character(10, 10, 10, "Gracz1")
player2 = Character(3, 27, 0, "Gracz2")

def main():
    while(player1.HP>0 and player2.HP>0):    
        Attack(player1, player2)
        if not player2.HP>0:
            print(f"{player1.name} won")
            break
        sleep(1)
        Attack(player2, player1)
        if not player1.HP>0:
            print(f"{player2.name} won")
            break
        sleep(1)
        
main()
    
