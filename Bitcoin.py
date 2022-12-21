from termcolor import colored
import random
import time
from os import system
mining = 150
ramdon_total = 0
print('₿ Welcome the miner')
time.sleep(0.5)
print('₿ How many do you want to mine?')
print('₿ Min. till your first reward!.')
durchgang = int(input("₿ -> "))
print (colored('Start mining...', 'green'))
while durchgang >= 10:
    ramdon = str(random.randint(1,9))
    ramdon_total += int(ramdon)
    randomhigh = str(random.randint(16,1036))
    while(mining >= 1):
        print (colored('Failed... BTC == 0.00000000 OR 0.00€', 'red'))
        mining -= 1
        durchgang -= 1
        time.sleep(0.05)
    while mining < 20:
        print (colored('Success... BTC == 0.00000' + randomhigh  +' OR 0.0' + ramdon + '€', 'green'))
        mining += random.randint(50,120)
        time.sleep(0.05)
        durchgang -= 1
        system("title " + 'Total = ' + str(ramdon_total) + ' Cent' )
print("Total: " + str(ramdon_total) + ' Cent')