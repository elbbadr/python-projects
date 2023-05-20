from cgi import print_arguments
from pystyle import *
print(Box.Lines("Multiplication Table "))
Write.Print("welcome to my Multiplication table from 1-12 APP\n " ,Colors.blue_to_green,interval=0.05)
while True :
    number = int(Write.Input("number : " ,Colors.green,interval=0.05))
    for i in range (1,13):
        print(number," * ",i," = ",number *i )

