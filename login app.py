# creat a login page using pystyle 
from pystyle import *
print(Box.Lines("welcome to our page "))
Write.Print("welcome to your acount \n",Colors.blue_to_cyan,interval=0.05)
Write.Print("Please write your username and password\n\n",Colors.blue_to_green,interval=0.05)
print(Box.DoubleCube("\nACCOUNT  "))
while True :
    username = Write.Input("username : ",Colors.dark_green,interval=0.05)
    password = Write.Input("password : ",Colors.dark_green,interval=0.05)
    if username=="badr" and password=="123456" :
       Write.Print("welcom "+ username,Colors.orange,interval=0.05)
       input("\ntyp inter to clos the app ...")
       break
    else:Write.Print("please try again ",Colors.blue_to_purple,interval=0.05)
