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
        self.isParrying = False
        
    @classmethod
    def InputCharacterStats(cls):
        print("Input your character stats. Stats have to add up to 30.")
        ATT = GetStat("Attack: ")
        DEF = GetStat("Defense: ")
        CON = GetStat("Constitution: ")
        Name = input("Name: ")
        if(ATT+DEF+CON) !=30:
            print("Stats don't add up to 30")
            return cls.InputCharacterStats()
        return Character(ATT, DEF, CON, Name)

    def removeHP(self, hp):
        self.HP -= hp
    
    def defend(self):
        self.endParry()
        self._def= self._def+self._con/2
        self._defending = True
        
    def endDefense(self):
        if self._defending:
            self._def= self._def-self._con/2
            self._defending = False
            
    def parry(self):
        self.endDefense()
        self._isParrying = True
    
    def endParry(self):
        self._isParrying = False
        
        
        
    @property
    def isParrying(self):
        return self._isParrying
    
    @isParrying.setter
    def isParrying(self, isParrying):
        self._isParrying = isParrying
    
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
    
### Rolls

def Roll(dice, bonus=0):
    return randrange(1, dice) + bonus

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
    
### Actions
def Attack(playerAttacking, playerDefending):
    ATT = playerAttacking.ATT
    DEF = playerDefending.DEF
    ATT  += Roll(20)
    
    if playerDefending.isParrying==True:
        dmg=Roll(10)
        playerAttacking.removeHP(dmg)
        print(f"{playerDefending.name} parried and dealt {dmg} damage to {playerAttacking.name}, {playerAttacking.HP} HP remaining")
        playerDefending.endParry()
    else:    
        if ATT >= DEF:
            dmg=Roll(10)
            playerDefending.removeHP(dmg)
            print(f"{playerAttacking.name} dealt {dmg} damage to {playerDefending.name}, {playerDefending.HP} HP remaining, Attack score: {ATT}, Defence score: {DEF}")

        else:
            print(f"Attack unsuccessful, Attack score: {ATT}, Defence score: {DEF}")
       
### Choice menu
 
def ChoiceMenu(playerChoosing, otherPlayer):
    playerChoosing.endDefense()
    playerChoosing.endParry()
    print("")
    print(f"{playerChoosing.name} - Choose an action:")
    print("1 - Attack")
    print("2 - Defend")
    print("3 - Parry")
    choice = GetChoiceMenuInput()
    match choice:
        case "1":
            Attack(playerChoosing, otherPlayer)
        case "2":
            playerChoosing.defend()
            NoAttackToParry(playerChoosing, otherPlayer)
        case "3":
            playerChoosing.parry()
            NoAttackToParry(playerChoosing, otherPlayer)
    print("")

def GetChoiceMenuInput():
    choice = input("Choice: ")
    if choice not in ['1', '2', '3']:
        print("Wrong input")
        return GetChoiceMenuInput()
    return choice

def NoAttackToParry(playerChoosing, otherPlayer):
    if otherPlayer.isParrying:
        otherPlayer.endParry()
        oldDefence = otherPlayer.DEF
        otherPlayer.DEF=otherPlayer.DEF/2
        ChoiceMenu(playerChoosing, otherPlayer)
        otherPlayer.DEF = oldDefence
    else:
        pass
    
### Stat handling
def CheckIfStatValid(stat):
    try:
        statnum = int(stat)
    except ValueError:
        print("Not a number")
        return False
        
    if statnum<0 or statnum>30:
        print("Stat invalid")
        return False
    
    return True

def GetStat(message):
    stat = input(message)
    if CheckIfStatValid(stat):
        return int(stat)
    else:
        return GetStat(message)
    
    


character1 = Character(10, 10, 10, "Player 1")
character2 = Character(15, 15, 0, "Player 2")
def main():    
    #character1 = Character.InputCharacterStats()   
    #character2 = Character.InputCharacterStats()
    player1, player2 = InitiativeRoll(character1, character2)
    while(player1.HP>0 and player2.HP>0):    
        ChoiceMenu(player1, player2)
        if not player2.HP>0:
            print(f"{player1.name} won")
            break
        sleep(0.5)
        ChoiceMenu(player2, player1)
        if not player1.HP>0:
            print(f"{player2.name} won")
            break
        sleep(0.5)



if __name__ == "__main__":
    main()
    
