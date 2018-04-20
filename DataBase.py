#Initializing Values
import msvcrt
import base64
import os
import time
import sys
def encode(key, clear):
    enc = []
    for i in range(len(clear)):
        key_c = key[i % len(key)]
        enc_c = chr((ord(clear[i]) + ord(key_c)) % 256)
        enc.append(enc_c)
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()

def decode(key, enc):
    dec = []
    enc = base64.urlsafe_b64decode(enc).decode()
    for i in range(len(enc)):
        key_c = key[i % len(key)]
        dec_c = chr((256 + ord(enc[i]) - ord(key_c)) % 256)
        dec.append(dec_c)
    return "".join(dec)
def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)
#userpass = [2,2,2,2,2,2,2]
userpass = []
End = 0
TH3 = "Add A Encode Gui"
line = 0
waitingMessage = "Please Wait Checking Your Informations ..." + "\n" "(It May Be Long To Create An Account)"
fMessage = "Completed √"
goodpass = ""
alreadyCreated = "false"
Repeat = True
Repeatpw = True
#Asking for login information 
while Repeat == True :
	login2 = input("Login >>>> ")
	login = login2.replace(" ", "")
	if str(login) == str(login2) :
		Repeat = False
	if Repeat == True :
		print("Do Not Put Spaces in username (you could use : " + str(login) + ")")
while Repeatpw == True :		
	pw2 = input("Password >>>>> ")
	pw = pw2.replace(" ", "")
	if str(pw) == str(pw2) :
		Repeatpw = False
	if Repeatpw == True :
		print("Do Not Put Spaces in password (you could use : " + str(pw) + ")")
pass_word = encode(TH3,pw)
#Creating A Value With All The Login Information
userEntry = ("[" + "'" + login + "'" + ", " + "'" + pass_word + "'" + "]")
#print (waitingMessage)
time.sleep(.1500)
while End == 0 :
	userpass = ""
	passfile = open('passwords.dat','r')
	#Verifiyng Line
	while line < 1000000 :
		userpass = passfile.readline().split()
		line = line + 1
		if len(userpass) == 0 :
			End = 1
			line = 1000001
		if len(userpass) > 0 :
			up = encode(TH3,userpass[1]) 
			#print(str(decode(TH3,up)))	
			#print(str(pass_word))	
		#See Values
		#print (line)
		#print (str(userpass))
		#print (str(userEntry))
		#Checking If Account Is Created
			if str(login) == str(userpass[0]) :
				alreadyCreated = "true"
				goodpass = str(decode(TH3,up))
				End = 1
				line = 1000001

		#Checking If This Is A New Account
		if line == 99999 :
			End = 1
		#Writing Information If This Is A New Account
	if alreadyCreated == "false" and End == 1 :
		passfile.close()
		passfile = open('passwords.dat','a')
		passfile.write(str(login + " "))
		passfile.write(str(pass_word))
		passfile.write('\n')
		print (fMessage)
		print ("succesfuly created account")
		End = 1
	#Verifying If This Is The Good Password If The Account Is Already Created
	if str(pass_word) == str(goodpass) and alreadyCreated == "true" and str(login) == str(userpass[0])  :
		print (fMessage)
		print("Welcome " + login)
		createFolder('./users/'+ login + '/')
		while True :
			if msvcrt.kbhit() :
					esc = b''
					key = msvcrt.getch()
					if key == esc :
						sys.exit("You Pressed Esc ...")
					elif str(key) == str("b'd'") :
						downloadSite = input("The Adresse Of Image You Want Too Dowload")
							
	elif alreadyCreated == "true" and str(pass_word) != str(goodpass) :
		print("Bad Password")	

#print (str(userpass[2])) 
