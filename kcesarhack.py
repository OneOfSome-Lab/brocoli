#Cracker. 
#This srcipt decrypts what was encrypted with kcesar.py also returns the encryption key
#Python3.6.9 blackfriar@gmx.com

ABC = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.,;:()%&$!?€'

kriptogram = input ('Introduce your Kriptogram: ')

for x in range (1, len(ABC)):
	ex = ' '
	for b in kriptogram:
		if b in ABC:
			pos = ABC.find(b)
			#crack
			pos = (pos - x) % len (ABC)
			ex += ABC[pos]
		else:
			ex += b
	print ('Key %d: %s' % (x, ex))
