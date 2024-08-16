import random as r

class Hero:
    def __init__(self, player, HP,MP,STR,DEF,SPD,ACC,AGL,name,charge):    
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
        self.shield = 0
        self.shieldState = 0
        self.UltCharge = 0
        self.effects = []
        self.durations = []
        self.effectpower = []
        self.specials = []
        self.name = self.name
        self.intel = self.intel
        
    def attack(self, enemy, mod):
        damage = int((self.STR + r.randint(0, self.STR*0.1)) * mod - enemy.DEF)
        hit = r.randint(0,100)
        if hit <= (74+self.ACC-enemy.AGL):
            if damage <= 0:
                damage = 1
            
            enemy.HP -= damage
            return damage
        else:
            return 0
        
    def buff(self, effect,duration,power):
        self.effects.append(effect)
        self.durations.append(duration)
        self.effectpower.append(power)
        
    def debuff(self,enemy,effect,duration,power):
        enemy.effects.append(effect)
        enemy.durations.append(duration)
        enemy.effectpower.append(power)
        
    def BasicAttack(self, enemy):
        pass
    
    def Ability1(self,enemy):
        pass
    
    def Ability2(self,enemy):
        pass
    
    def Ultimate(self,enemy):
        pass
    
    def instakill(self,enemy):
        if enemy.HP <= int(enemy.MaxHP*0.3):
            enemy.HP = 0
            return 0
        else:
            enemy.HP -= 500 - enemy.DEF
            if enemy.HP <= 0:
                return 0
            else:
                return 1
        
    def MegaBlast(self, enemy):
        hit = r.randint(0,100)
        if hit < 75:
            enemy.HP -= 2000 - enemy.DEF
            if enemy.HP <= 0:
                return 0
            else:
                return 1
        else:
            return 2
            
        
    
    
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
        
    def BasicAttack(self, enemy):
        d = super().attack(enemy,1.5)
        if enemy.HP <= 0:
            return "Ваша атака добивает оппонента! Быстро и эффективнно!"
        elif d == 0:
            return "Ваша атака промахнулась! Оппонент смог избежать вашего лезвия!"
        else:
            return f"Вы совершаете быструю атаку своим клинком, нанося {d} урона!"
        
    def Ability1(self, enemy):
        if self.MP >= 4:
            self.MP -= 4
            d = super().attack(enemy,2.5)  
            if d > 0:
                super().debuff(enemy,"Сила понижена",3,5)
            if enemy.HP <= 0:
                return "Баланс оппонента был сбит настолько сильно, что он больше не может сражаться!"
            elif d == 0:
                return "Ваш приём не повлиял на оппонента! Он продолжает непоколебимо стоять!"
            else:
                return f"Вы используете приём сбивания баланса! Сила противника снижена, вдогонку, вы наносите {d} урона!"
        else:
            return "У вас недостаточно ОН! Сосредоточься, ассасин."  
        
    def Ability2(self, enemy):
        if self.MP >= 9:
            self.MP -= 9
            d = super().attack(enemy,6)  
            if enemy.HP <= 0:
                return "Тяжёлая атака разбивает вашего оппонента вдребезги, не оставляя ни единого шанса!"
            elif d == 0:
                return "Сильный приём! Но иногда нужно ещё смотреть куда бьёшь!"
            else:
                return f"Вы совершаете тяжёлый удар, оппонент получает {d} урона!"
        else:
            return "У вас недостаточно ОН! Терпение, твой момент ещё будет."     
        
    def Ultimate(self, enemy):
        if self.UltCharge == 100:           
            s = super().instakill(enemy)
            if s == 0:
                return "Враг был достаточно ослаблен чтобы уничтожить его изящной чередой ударов!"
            else:
                return "Враг получает тяжёлые ранения от череды ударов!"
        else:
            return "Ваш Ультраприём ещё не заряжен до конца! Дождись, пока ты сможешь выцепить момент."
        
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
        
    def BasicAttack(self, enemy):
        d = super().attack(enemy,2.5)
        if enemy.HP <= 0:
            return "Точный выстрел из револьвера разрешает дело в вашу пользу!"
        elif d == 0:
            return "Ваш выстрел пролетел мимо! В следующий раз попадёте!"
        else:
            return f"Вы совершаете прицельный выстрел, нанося {d} урона!"
        
    def Ability1(self, enemy):
        if self.MP >= 6:
            self.MP -= 6
            super().buff("Ловкость повышена",2,20)
            return "Ваша ловкость значительно повышенна! По вам куда сложнее попасть!"
        else:
            return "У вас недостаточно ОН! Запасись терпением, ковбой."
        
    def Ability2(self, enemy):
        if self.MP >= 9:
            d = super().attack(enemy, 4)
            if d > 0:
                super().debuff(enemy,"Горит",2,25)
            if enemy.HP <= 0:
                return "Нагретый металл прожигает вашего оппонента насквозь, устраняя его!"
            elif d == 0:
                return "Адски горячий снаряд просвистел в паре сантиметров от противника не нанеся никакого урона!"
            else:
                return f"Нагрев свой револьвер вы выстреливаете раскалённым снарядом, нанося {d} урона и поджигая вашего оппонента!"
        else:
            return "У вас недостаточно ОН! Заряди свою пушку как следует!"
    
    def Ultimate(self, enemy):
        if self.UltCharge == 100:
            d = super().MegaBlast(enemy)
            if d == 0:
                return "Пара изменений в револьвере, и ваш следующий выстрел создаёт настолько мощную вспышку с волной, что вас откидывает на землю... Оппонент был стёрт с поля боя."
            elif d == 1:
                return "Пара изменений в револьвере, и ваш следующий выстрел создаёт настолько мощную вспышку с волной, что вас откидывает на землю... Невероятно, но ваш оппонент продолжает стоять на поле боя!"
            else:
                return "Пара изменений в револьвере, и ваш следующий выстрел создаёт... Подождите... Он заклинил... Вы стараетесь вернуть его в прежнее состояние, прежде чем вас настигнут атаки оппонента."
        else:
            return "Ваш Ультраприём ещё не заряжен до конца! Поищи, чем ты можешь занять оппонента до его готовности!"
    
    
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
        
    def BasicAttack(self, enemy):
        d = super().attack(enemy, 2)
        if d > 0:
            enemy.HP -= self.HP// 100
        if enemy.HP <= 0:
            return "Мощный толчок телом, и ваш оппонент оказывается сокрушён под силой вашего веса!"
        elif d == 0:
            return "Ваша атака промахнулась! Возможно, похудение - это ваш лучший вариант для попаданий."
        else:
            return f"Вы используете своё весовое преимуществоб чтобы нанести {d} урона!"
        
    def Ability1(self, enemy):
        if self.MP >= 7:
            self.MP -= 7
            super().buff("Глюкозный разгон",3,10)
            return "Особый шоколадный батончик заметно разгоняет вас повышая несколько характеристик!"
        else:
            return "У вас недостаточно ОН! Пора найти ещё немного запасов!"
        
    def Ability2(self, enemy):
        if self.MP >= 3:
            self.MP -= 3
            if r.randint <= (74+self.ACC-enemy.AGL):
                d = int((self.MaxHP - self.HP)* 0.3)
                enemy.HP -= d
                if enemy.HP <= 0:
                    return ""
                else: 
                    return f"Ярость от полученных вами повреждений выливается на оппонента, нанося {d} урона!"
            else:
                return "Ярость слишком сильно завихряет вам мысли настолько, что вы банально не можете попасть!"
        else:
            return "У вас недостаточно ОН! Видимо большого человека ещё недостаточно много!"
        
    def Ultimate(self, enemy):
        if self.UltCharge == 100:
            self.HP = self.MaxHP
            self.MP = self.MaxMP
            self.ACC += 5
            self.STR += 5
            return "С вами прибывает сила всего сладкого! Вы полностью восстановленны"
        else:
            return "Ваш Ультраприём ещё не заряжен до конца! Толстяк ещё не готов выдать свой главный финт!"
        
            
class Palan(Hero):
    def __init__(self):
        self.HP = 100
        self.MP = 50
        self.STR = 50
        self.DEF = 0
        self.SPD = 50
        self.ACC = 15
        self.AGL = 0
        self.shield = 300
        self.shieldState = 1
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