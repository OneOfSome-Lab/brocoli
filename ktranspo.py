 # A transposition cipher is a method of encryption by which the positions 
 # held by units of plaintext (which are commonly characters or groups of characters) 
 # are shifted according to a regular system, 
 # so that the ciphertext constitutes a permutation of the plaintext. 
 
 # This script goes with a "simple transposition". It is only interesting for long messages
 # 15.01.2020 blackfriar@gmx.com
 # Python3.6.9
 

def main ():
	msg = input ('Introduce your message: ')
	k = int (input ('Introduce your key (a number): '))
	msg = rmv_blankspace (msg)
	
	kriptogram = salida (cipher (msg,k))
	
	print (kriptogram.upper())

#Removing Blank Spaces
def rmv_blankspace (msg):
	newmsg = ''
	for x in msg:
		if x != '':
			newmsg += x
	return newmsg

# Showing the message into groups of 5 char including spaces
def salida (kriptogram):
	BLOCK = 5
	text = ''
	for i in range (len(kriptogram)):
		if (i+1) % BLOCK != 0:
			text += kriptogram [i]
		else:
			text += kriptogram [i] + ' '
	return text
	  

def cipher (msg,k):
# Each cryptogram string is a column of the list
	kriptogram = [' ']*k

	for col in range(k):
		pos = col
		while pos < len (msg):
			kriptogram [col] += msg [pos]
			pos += k
	return ''.join(kriptogram)	


main ()	
