# we will use pyshort and pystyle 
import pyshorteners 
from pystyle import *
print(Box.Lines("Multiplication Table "))
Write.Print("welcome to URL shortner app : \n " ,Colors.blue_to_green,interval=0.05)
url = Write.Input("pleas inter the URL : ",Colors.cyan_to_green,interval=0.05)
sht = pyshorteners.Shortener()
Write.Print(sht.(url),Colors.green_to_white,interval=0.05)
input("\npleas typ key to clos the app...")


