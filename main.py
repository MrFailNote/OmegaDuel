import telebot 
from config import token
import random as r
import characters as c
import logicHandler as l

bot = telebot.TeleBot(token)

@bot.message_handler(commands = ['pick'])
def pickCharachter(message):
    if message.from_user.username not in c.Hero.player.keys():
        if len(message.text) > 5:
            currentPick = message.text[5:] 
        else:
            currentPick = 1
        
        match currentPick:
            case 1:
                fighter = c.Blade(message.from_user.username)
            case 2:
                fighter = c.GlassJoe(message.from_user.username)
            case 3:
                fighter = c.Bob(message.from_user.username)
            case 4:
                fighter = c.Palan(message.from_user.username)
            case 5:
                fighter = c.Ravick(message.from_user.username)
            case 6:
                fighter = c.Devourer(message.from_user.username)
            case 7:
                fighter = c.YV(message.from_user.username)
            case 8:
                fighter = c.Fortune(message.from_user.username)
            case 9:
                fighter = c.Coder(message.from_user.username)
            case 10:
                fighter = c.Lost(message.from_user.username)
            case 11:
                fighter = c.Molten(message.from_user.username)
            case 12:
                fighter = c.Commando(message.from_user.username)
            case 13:
                fighter = c.Omega(message.from_user.username)
            
        bot.send_message(message.chat.id, f"Ваш выбраннный чемпион: {fighter.name}")
        
@bot.message_handler(commands = ['intel'])
def getInfo(message):
    if message.from_user.username in c.Hero.player.keys():
        targetHero = c.Hero.player[message.from_user.username]
        bot.reply_to(message, f'''Информация о вашем чемпионе [{targetHero.name}]:
Здоровье: {targetHero.HP}\{targetHero.MaxHP}
Очки Навыков: {targetHero.MP}\{targetHero.MaxMP}
Сила: {targetHero.STR}
Защита: {targetHero.DEF}
Точность: {targetHero.ACC}
Ловкость: {targetHero.AGL} 
Скорость: {targetHero.SPD}
''')
    else:
        bot.reply_to(message, "Пожалуйста, выберите себе чемпиона для получения справки о нём.")
        
@bot.message_handler(commands = ['fight'])
def Initiate(message):
    if message.from_user.username in c.Hero.player.keys():
        if len(message.text) > 6:
            targetEnemy = message.text[6:] 
            
        else:
            bot.reply_to(message, "Выберите того, с кем будете сражаться! Не пишите что попало.")
        
        