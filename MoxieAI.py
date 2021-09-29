#-------------------------------------------------------------------------------------------------------------------
import pyttsx3
from webbrowser import open as show_me
import random
import string
import time
import datetime
import os
import urllib.request
import json
from random import randint
global name, engine
assistant = pyttsx3.init()
#--------------------------------------------------------------------------------------------------------------------
class CurrencyConverter:

	rates = {}

	def __init__(self, url):
		req = urllib.request.Request(url, headers={'User-Agent': 'howCode Currency Bot'})
		data = urllib.request.urlopen(req).read()
		data = json.loads(data.decode('utf-8'))
		self.rates = data["rates"]
#--------------------------------------------------------------------------------------------------------------------
name = input("what is your name?: ")
print("Hello " + name)
assistant.say("Hello. Good to see you")
assistant.runAndWait()
e = datetime.datetime.now()

print ("Info at time logged in :")
print ("Current date and time: %s" % e)

print ("Today's date: %s/%s/%s" % (e.day, e.month, e.year))

print ("The time is now: %s:%s:%s" % (e.hour, e.minute, e.second))
#--------------------------------------------------------------------------------------------------------------------
def app(APP):
     os.system(APP)

def close_app(App):
     os.close(App)
#--------------------------------------------------------------------------------------------------------------------     
def  url():
     URL = input("Enter url: ")
     print(name + ", Browser has succsessfully opened and redirecting to url typed. Yay!!!")
     show_me(URL)
#--------------------------------------------------------------------------------------------------------------------
def quiz():
     answer1 = input("1. What is your name: ")
     if answer1 == name:
          print("Yay! Correct!")
     else:
               print("Sorry! Correct answer is " + name)
     answer2 = input("2.Which team won the Euro 2020 football game A) Engalnd B) Italy C) Germany")
     if answer2 == "Italy" or "italy" or "b" or "B" or "ITALY":
          print("Yay")
          print("Awww!, Sorry! More quiz coming soon!")
     elif answer2 == "I dont know" or "i dont know" or "idk" or "IDK" or "I dont know?" or "idk?" or "IDK?" or "I DONT KNOW?" or "I DONT KNOW?" or "I don't know":
                    print("Don't worry, ", name)
                    print("answer is B) Italy")
                    print("Awww!, Sorry! More quiz coming soon!")
     else:
          print("Sorry answer is B) Italy")
          print("Awww!, Sorry! More quiz coming soon!")

def hlp():
     print("Hey ", name, "! Welcome to help! Enter any quieries you need help with : ")
     quiries = input("Please type your quieries")

def change_name(change):
     print('Name changed to ', change,"!")

def what_is_my_name():
     print('Your name is', name)

def virus_prank():
     confirm_answer = input("Are you sure you want to install a temporary file?(y / n): ")
     if confirm_answer == 'y' or 'yes' or 'Yes' or 'YES' or 'Y':
          time.sleep(5)
          print("Installing...")
          time.sleep(3)
          print("5%")
          time.sleep(2)
          print("40%")
          time.sleep(7)
          print("94%")
          time.sleep(2)
          print("*Virus installed*")
     else:
         if confirm_answer == "N" or "n" or "NO" or "No" or "no":
              print("Ok user! virus is not being installed and executed.")
def Round(number):
     print(round(number))
def farenheit_celcius(Number):
     calculation = Number * 1.8 + 32
     print("It is", calculation, "in celcius", name)

def celcius_farenheit(NUMBER):
     Calculation = NUMBER / 1.8 - 32
     print("It is", Calculation, "in celcius", name)
def weather_tempreture(number):
     Number = number
     if Number < 10:
          print("F-F-Freezzzing!")
     elif Number >= 10:
          print("I don't feel a thing!")
     elif Number >= 20:
          print("Sunny, right?")
     elif Number >= 30:
          print("I'm dying! Give me the ice-cream, please!")
     elif Number >= 40:
          print("H-H-Help...")

def roll_dice(dots):
    dice_roll = randint(1, dots)
    print(name + ", You threw a", dice_roll)
def hello():
     print("Hello", name) or print("Hope you had a great time", name)
     assistant.say("Hello", name)
     assistant.runAndWait()
def time():
     J = datetime.datetime.now()
     print ("Today's date: %s/%s/%s" % (J.day, J.month, J.year))

     print ("The time is now: %s:%s:%s" % (J.hour, J.minute, J.second))

def convert(self, amount, from_currency, to_currency):
		initial_amount = amount
		if from_currency != "EUR":
			amount = amount / self.rates[from_currency]
		if to_currency == "EUR":
			return initial_amount, from_currency, '=', amount, to_currency
		else:
			return initial_amount, from_currency, '=', amount * self.rates[to_currency], to_currency
