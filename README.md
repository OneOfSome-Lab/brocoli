#09.01.2020 16:36:29
#made by OneofSome blackfriar@gmx.es
#This program uses the ATBASH cipher to cripto a message. Is a very simple #script wich I added numbers, so you can use numbers #in the message and at the same time make the message a bit darker

#Atbash is a very common method of encryption (cryptography) of the Hebrew alphabet.
#it belongs to the so-called Classic Cryptography and is a type of encryption by substitution.
#One of its most famous uses is given in the book of Jeremiah (Bible)

#!usr/bin python3.6.9

PLANE_TXT = "0123456789abcdefghijklmnopqrstuvwxyz "
CIPHER = "ZYXWVUTSRQPONMLKJIHGFEDCBA9876543210 "

txts = input ('Introduce your text: ')
txt2 = ' '

for txt in txts.lower():
	if txt in PLANE_TXT:
		ind = PLANE_TXT.index (txt)
		txt2 += CIPHER [ind]
print (txt2)

