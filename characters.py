import random as r

class Hero:
    def __init__(self, player, HP,MP,STR,DEF,SPD,ACC,AGL,name):    
        self.player = player
        self.HP = self.HP
        self.MaxHP = self.HP
        self.MP = self.MP
        self.MaxMP = self.MP
        self.STR = self.STR
        self.DEF = self.DEF
        self.SPD = self.SPD
        self.ACC = self.ACC
        self.AGL = self.AGL
        self.effects = []
        self.durations = []
        self.specials = []
        self.name = self.name
        
    def attack(self, enemy, mod):
        damage = (self.STR + r.randint(0, self.STR*0.1)) * mod - enemy.DEF
        if damage <= 0:
            damage = 1
        
        enemy.HP -= damage
        
    def buff(self, effect):
        self.effects.append(effect)
        
    def debuff(self,enemy,effect):
        enemy.effects.append(effect)
        
    
    
class Blade(Hero):
    def __init__(self):
        self.HP = 750
        self.MP = 35
        self.STR = 50
        self.DEF = 12
        self.SPD = 75
        self.ACC = 10
        self.AGL = 10
        self.name = "Blade"
        
class GlassJoe(Hero):
    def __init__(self):
        self.HP = 350
        self.MP = 20
        self.STR = 120
        self.DEF = 0
        self.SPD = 40
        self.ACC = 5
        self.AGL = 20
        self.name = "Glass Joe"
    
class Bob(Hero):
    def __init__(self):
        self.HP = 2000
        self.MP = 15
        self.STR = 20
        self.DEF = 45
        self.SPD = 10
        self.ACC = 0
        self.AGL = -20
        self.name = "Bob"
    
class Palan(Hero):
    def __init__(self):
        self.HP = 100
        self.MP = 50
        self.STR = 50
        self.DEF = 0
        self.SPD = 50
        self.ACC = 15
        self.AGL = 0
        self.name = "Palan"
        
class YV(Hero):
    def __init__(self):
        self.HP = 800
        self.MP = 10
        self.STR = 40
        self.DEF = 10
        self.SPD = 0
        self.ACC = 45
        self.AGL = 20
        self.name = "Y.V."
        
class Ravick(Hero):
    def __init__(self):
        self.HP = 1000
        self.MP = 24
        self.STR = 60
        self.DEF = -20
        self.SPD = 45
        self.ACC = 10
        self.AGL = 10
        self.name = "Ravick"

class Devourer(Hero):
    def __init__(self):
        self.HP = 600
        self.MP = 30
        self.STR = 25
        self.DEF = 5
        self.SPD = 15
        self.ACC = 7
        self.AGL = 10
        self.name = "Devourer"
        
class Fortune(Hero):
    def __init__(self):
        self.HP = 675
        self.MP = 40
        self.STR = 40
        self.DEF = 0
        self.SPD = 100
        self.ACC = 50
        self.AGL = 15
        self.name = "Fortune teller"
        
class Coder(Hero):
    def __init__(self):
        self.HP = 999
        self.MP = 20
        self.STR = 99
        self.DEF = 0
        self.SPD = 64
        self.ACC = 0
        self.AGL = 0
        self.name = "Coder"
        
class Lost(Hero):
    def __init__(self):
        self.HP = 1
        self.MP = 20
        self.STR = 50
        self.DEF = 0
        self.SPD = 110
        self.ACC = 50
        self.AGL = 20
        self.name = "Lost"
    
class Molten(Hero):
    def __init__(self):
        self.HP = 1200
        self.MP = 30
        self.STR = 30
        self.DEF = 3
        self.SPD = 30
        self.ACC = 30
        self.AGL = 10
        self.name = "Molten"

class Commando(Hero):
    def __init__(self):
        self.HP = 800
        self.MP = 30
        self.STR = 12
        self.DEF = 10
        self.SPD = 32
        self.ACC = 25
        self.AGL = 10
        self.name = "Commando"
        
class Omega(Hero):
    def __init__(self):
        self.HP = 750
        self.MP = 100
        self.STR = 40
        self.DEF = 10
        self.SPD = 60
        self.ACC = 100
        self.AGL = 0
        self.name = "O M E G A"