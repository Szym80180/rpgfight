from random import randrange
from time import sleep
class Character:
    def __init__(self, ATT, DEF, CON, name):
        self.ATT= int(ATT/3)
        if ATT>15:
            self.ATT=int(15+(1.34*(ATT-15)))
        self.DEF=DEF       
        self.CON=CON
        self.HP = 30 + CON/2
        self._defenceHP= self.HP
        self.name=name
        self._defending = False
    

    def removeHP(self, hp):
        self.HP -= hp
    
    def defend(self):
        self._def= self._def+self._con/2
        self._defending = True
        
    def endDefense(self):
        if self._defending:
            self._def= self._def-self._con/2
            self._defending = False
    
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
    playerAttacking.endDefense()
    ATT = playerAttacking.ATT
    DEF = playerDefending.DEF
    ATT  += Roll(20)
    if ATT >= DEF:
        dmg=Roll(10)
        playerDefending.removeHP(dmg)
        print(f"{playerAttacking.name} dealt {dmg} damage to {playerDefending.name}, {playerDefending.HP} HP remaining, Attack score: {ATT}, Defence score: {DEF}")
        
    else:
        print(f"Attack unsuccessful, Attack score: {ATT}, Defence score: {DEF}")
        
def ChoiceMenu(playerChoosing, otherPlayer):
    print(f"{playerChoosing.name} - Choose an action:")
    print("1 - Attack")
    print("2 - Defend")
    choice = input("Choice: ")
    match choice:
        case "1":
            Attack(playerChoosing, otherPlayer)
        case "2":
            playerChoosing.defend()
    
def InitiativeRoll(character1, character2):
    rollCharacter1 = Roll(20)
    rollCharacter2 = Roll(20)
    if rollCharacter1 > rollCharacter2:
        print(f"Initiative roll: {character1.name}: {rollCharacter1}, {character2.name}: {rollCharacter2}")
        return (character1, character2)
    elif rollCharacter2 > rollCharacter1:
        print(f"Initiative roll: {character1.name}: {rollCharacter1}, {character2.name}: {rollCharacter2}")
        return (character2, character1)
    else:
        return InitiativeRoll(character1, character2)
    
character1 = Character(20, 0, 10, "Gracz1")
character2 = Character(3, 27, 0, "Gracz2")

def main():
    player1, player2 = InitiativeRoll(character1, character2)
    while(player1.HP>0 and player2.HP>0):    
        ChoiceMenu(player1, player2)
        if not player2.HP>0:
            print(f"{player1.name} won")
            break
        sleep(1)
        ChoiceMenu(player2, player1)
        if not player1.HP>0:
            print(f"{player2.name} won")
            break
        sleep(1)
        
main()
    
