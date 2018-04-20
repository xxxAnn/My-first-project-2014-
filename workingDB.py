#Initializing Values
End = 0
line = 0
waitingMessage = "Please Wait Checking Your Informations ..." + "\n" "(It May Be Long To Create An Account)"
fMessage = "Completed √"
goodpass = ""
alreadyCreated = "false"
#Asking for login information 
login = input("Login >>>>")
pass_word = input("Password >>>>>")
#Creating A Value With All The Login Information
userEntry = ("[" + "'" + login + "'" + ", " + "'" + pass_word + "'" + "]")
print (waitingMessage)
while End == 0 :
	userpass = ""
	passfile = open('passwords.dat','r')
	#Verifiyng Line
	while line < 1000000 :
		userpass = passfile.readline().split()
		line = line + 1
		#See Values
		#print (line)
		#print (str(userpass))
		#print (str(userEntry))
		#Checking If Account Is Created
		if str(userpass) == str(userEntry) :
			alreadyCreated = "true"
			goodpass = userpass[1]
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
	if str(pass_word) == str(goodpass) and alreadyCreated == "true"  :
		print (fMessage)
		print("Welcome " + login)
	elif alreadyCreated == "true" :
		print ("Password Refused Or Username Already Used")		  
