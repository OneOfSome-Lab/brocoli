# kcesar.py.- In cryptography, a Caesar cipher is an ancient form of substitution cipher. 
# It is named in the honor of Roman emperor, Julius Caesar. It was in use till 1916, the Russian Army 
# used it during the I GW. Traditionaly the key is 3, and just characters 
# with this software the key could be from 1  to 46  instead 1 to 26
# and you can use numbers and others characters.
# -------------------------------------------------------------------
#  10.01.2020 blackfriar@gmx.com
#---------------------------------------------
# Python 3.6.9

#The orders
ABC = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.,;:()%&$!?€'

mod = input ('To encode writte "e". To decode writte "d", and press enter: ')

text = input ('\nIntroduce your text: ')

key = int(input ('''\nIntroduce a key-number. You must REMEMBER IT to Encode/Decode the message later.\n 
Choose a key-number from 1 to 47: '''))

ex = ' '

#The algorithm based in modal arithmetic
for x in text.upper():
	if x in ABC:
		pos = ABC.find(x)
		if mod == 'e':
			pos = (pos + key) % 48
		elif mod == 'd':
			pos = (pos - key) % 48
		
		ex += ABC [pos]
		
	else:
		ex += x

print ('\nYour text now is: ' + ex)
