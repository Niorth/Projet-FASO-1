import sys

sys.path.insert(0, './biblio_ext')
from gopigo import *
import time, math
from grovepi import *
import os  # pour PushBullet
import main
def DeroulerFeuille(coef):
	#print(coef)
	fwd()
	time.sleep(5)
	stop()
	time.sleep(4)
	main.main()
