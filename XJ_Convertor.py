import sys
import xml.etree.ElementTree as ET
import requests
from extractXML import extractXML
from validationCMD import validationCMD

#

argv2=True
argv3=True
argv4=True
argv5=True
argv6=True
argv7=True

validationCMD(argv2,argv3,argv4,argv5,argv6,argv7)
#fonction qu permet de faire l'extraction au niveau du fichier XML
def validerXml():
	if sys.argv[5]=="-h":
		r = requests.get("http://sgbdproject.000webhostapp.com/files/qtDTO.html")
		#creation du fichier fluxXml.xml
		fichier = open("fluxXml.xml","w")
		fichier.write(r.text)
		fichier.close()
		tree = ET.parse("fluxXml.xml")
		root = tree.getroot()
		extractXML(root,arg3)
	else:
		if sys.argv[5]=="SGBD.xml":
			tree = ET.parse(sys.argv[5])
			root = tree.getroot()
			extractXML(root,arg3)
		if sys.argv[4]=="SGBD.xml":
			tree = ET.parse(sys.argv[4])
			root = tree.getroot()
			extractXML(root,arg3)
#fonction qui permet de faire l'extraction au niveau du fichier JSON

def validerJson():
	r = requests.get("")
	#creation du fichier fluxXml.xml
	fichier = open("fluxXml.json","w")
	fichier.write(r.text)
	fichier.close()
	tree = ET.parse("fluxXml.json")
	root = tree.getroot()
	extractJSON(root,arg3)
	if sys.argv[5]=="SGBD.json":
		tree = ET.parse(sys.argv[5])
		root = tree.getroot()
		extractJSON(root,arg3)
	if sys.argv[4]=="SGBD.json":
		tree = ET.parse(sys.argv[4])
		root = tree.getroot()
		extractJSON(root,arg3)

#print sys.argv[0],argv2,argv3,argv4,argv5,argv6
if (sys.argv[0]=="XJ_Convertor.py" and argv2 and argv3 and argv4 and argv5 and argv6):
	if sys.argv[2]=="xml":
		arg3=sys.argv[3]
		validerXml()
	else:
		validerJson()
else :
	print (" Commande incorrecte!")
	print (" Elle est sous la forme : XJ_Convertor -i xml/json [-t][-h Url_FluxHTTP] -f monfichier.xml -o nomFichier.svg")
# SAUVEGARDER LE FICHIER SVG
