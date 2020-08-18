# coding: utf-8

"""
BY AHMED
Last Updated -
Python 2.7.13
"""

# DICTIONNAIRE FR
unit = ('Zéro',  'Un',   'Deux',  'Trois', 'Quatre',   'Cinq',   'Six', 'Sept', 'Huit', 'Neuf') 
dizaine_1 = ('Dix', 'Onze', 'Douze', 'Treize', 'Quatorze', 'Quinze', 'Seize', 'Dix-Sept', 'Dix-Huit', 'Dix-Neuf')
dizaine_2 = ('Vingt', 'Trente', 'Quarante', 'Cinquante', 'Soixante', 'Soixante', 'Quatre-Vingt', 'Quatre-Vingt')
separator = ('Cent', 'Mille', 'Million', 'Milliard', 'Billion', 'Quadrillion', 'Quintillion', 'Sextillion', 'Septillion', 'Octillion', 'Nonillion','Décillion', 
    'Undecillion', 'Duodecillion', 'Tredecillion', 'Quattuordecillion', 'Sexdecillion', 'Septendecillion', 'Octodecillion', 'Icosillion', 'Vigintillion' )


# PERMET LA LECTURE DES UNITES
def readUnit ( num, lettre = "", print_zero = False):
	if print_zero == True and long(num) == 0 :
		lettre = unit[long(num)]
	elif long(num) != 0 :
		lettre += unit[long(num)]
	elif long(num) == 0 :
		lettre = ''
	return lettre

# PERMET LA LECTURE DES DIZAINE, UTILISE LA LECTURE DES UNITES
def readTen( num, lettre = "" ):
	if long(num[0]) == 0:
		lettre += readUnit(num[1])
	elif long(num[0]) == 1:
		lettre += dizaine_1[ long( num[1] ) ]
	elif long(num[0]) == 7 or long(num[0]) == 9:
		lettre += dizaine_2[ long( num[0] ) - 2 ] + ' ' 
		lettre += dizaine_1[ long( num[1] ) ] 
	else:
		lettre += dizaine_2[ long( num[0] ) -  2 ] + ' '
		lettre += readUnit(num[1])
	return lettre.strip()


# PERMET LA LECTURE DES CENTAINES, UTILISE LA LECTURE DES DIZAINES
def readCent( num, lettre = ""):
	if long(num [0]) == 0:
		lettre += readTen(num[1:])
	elif long(num [0]) == 1:
		lettre += separator[0] + ' '
		lettre += readTen(num[1:])
	else:	
		lettre += readUnit(num[0]) + ' '+ separator[0] + ' '
		lettre += readTen(num[1:])
	return lettre.strip()

# FONCTION D'ENTREE 
def lireLettre(num):
	try:
		if len(num) == 1 and long(num) == 0:
			return readUnit(num,"",True)

		tour = (len(num) / 3)
		if (len(num) % 3) == 0 and tour > 0:
			tour = tour - 1

		lettre = lectureEnLettre(num, tour)	

		return lettre
	except:
		return "Is not a number"


# FONCTION RECURSIVE QUI ORGANISE LA LECTURE, APPELER DANS LA FONCTION D'ENTREE 
def lectureEnLettre(num, tour):
	if tour == 0 :
		if len(num)== 3:
			return readCent(num)
		elif len(num)== 2:
			return readTen(num) 
		else:
			return readUnit(num)
	else:
		lettre = ""
		num_2 = ""
		mod =  (len(num) % 3)
		if mod == 0:
			num_2 = num[:3]
			num = num[3:] 
		else:
			num_2 = num[:mod]
			num = num[mod:]

		if len(num_2) == 3:
			lettre = readCent(num_2)
		elif len(num_2) == 2:
			lettre = readTen(num_2)
		elif (len(num_2) == 1 and len(num) > 3) or (len(num_2) == 1 and long(num_2) != 1):
			lettre = readUnit(num_2)

		if(long(num_2) > 0):
			lettre += ' ' + separator[tour]

		# Correction of space between words
		if(len(lettre) > 0):
			lettre = lettre.strip() + ' '
		else:
			lettre = lettre.strip()

		return lettre + lectureEnLettre(num, tour - 1)


"""
	TESTS
"""

# TEST 1
#num = str()
#while 1:
#	num = raw_input("Entrez un nombre (Tapez 'Q' pour quitter) : ")
#	if num == "Q" or num.lower() == "q":
#		print ("Fin du Test")
#		break
#	print (num + ' - '+ lireLettre(num))


# TEST 2

#num = str(input("Entrez un nombre : "))
#print( lireLettre (num))

# TEST 3

#for i in range(10000010):
#	print(str(i) + ' - '+ lireLettre(str(i)))
