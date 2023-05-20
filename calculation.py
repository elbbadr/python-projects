# creat a calculation for 2 numbers 
from pystyle import *
print(Box.Lines("welcom to BADR calculater "))
Write.Print("\t welcom\n",Colors.blue_to_cyan,interval=0.05)
Write.Print("Please pick 2 numbers :\n",Colors.blue_to_purple,interval=0.05)
NUM1 = input("NUM 1 : ")
clacluation = Write.Input("+ or - or * or / : ",Colors.green,interval=0.05)
NUM2 = input("NUM 3 : ")
if clacluation=='+':
    Write.Print("resulte : "+str(int(NUM1) + int(NUM2)),Colors.red_to_purple,interval=0.05)
elif clacluation=='-':
    Write.Print("resulte : "+str(int(NUM1) - int(NUM2)),Colors.red_to_purple,interval=0.05)
elif clacluation=='*':
     Write.Print("resulte : "+str(int(NUM1) * int(NUM2)),Colors.red_to_purple,interval=0.05)
elif clacluation =='/':
    Write.Print("resulte : "+str(int(NUM1) / int(NUM2)),Colors.red_to_purple,interval=0.05) 
else:Write.Print("write a calculation pleas",Colors.blue_to_cyan,interval=0.05)
