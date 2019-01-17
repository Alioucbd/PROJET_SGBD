# fonction pour vaider la commande pour l'execution du code
def validationCMD(argv2,argv3,argv4,argv5,argv6,argv7):	
	
	try:
		if sys.argv[1]=="-i":
			print sys.argv[1]
	except Exception as e:
		argv2=False
		#raise e
		
	try:
		if sys.argv[2]=="xml" or sys.argv[2]=="json":
			print("")
	except Exception as e:
		argv3=False
		#raise e
	
	try:
		if sys.argv[3]=="-f" or sys.argv[3]=="-t":
			print("")
	except Exception as e:
		argv4=False
		#raise e
	
	try:
		if sys.argv[4]=="SGBD.xml":
	
			print("")
	except Exception as e:
	#raise e
		argv5=False
	
	try:
		if sys.argv[5]=="-o" or sys.argv[5]=="SGBD.xml":
			print("")
	except Exception as e:
	#raise e
		argv6=False
