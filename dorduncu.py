#coding:utf8

#def kare(x):
#    return x**2
#
#def kup(x):
#    return x**3
#
#
#karesi=kare(4)

#print kare(4)


import random
print(random.choice([1,2,3,60,24,32]))

#%%
import math

print (math.cos(math.pi/110))

#%%

import math
print (math.log(1500,10))

#%% sayinin kupunu alan program

from ucuncu import kup

sayi=kup(32)

sayinin_yazimi='Otuz iki bin yedi yüz altmış sekiz'

print sayinin_yazimi


#%% 

from datetime import date

datetoday=date.today()

print(datetoday)

print(datetoday.strftime("%B %d %Y"))


#%% dosya yazdirma
#coding:utf8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

dosya=open('yenidosya2.txt','w')

dosya.write('Merhaba Bunun Mart 2si\n')

dosya.write('örnek parağraf\n')
dosya.close()
print('dosya yazildi')



