import svgwrite
from genererSVG import genererSVG

def extractXML(root,arg3):
	
	#PARCOURIR LE FICHIER XML AFIN DE RECUPERER LES ENTITES ET LES ASSOCIATIONS ET LEURS ATTRIBUTS

	for entite1 in root.findall('entite1'):
	 
	    # name = entite.get('id')
	    nomEntite = entite1.find('nomEntite').text
	    for attribut in entite1.findall('attribut'):
	     	ide = attribut.find('id').text
	     	nom = attribut.find('nom').text
	    	prenom = attribut.find('prenom').text
	    card1 = entite1.find('cardinalite').text
	
	
	for entite2 in root.findall('entite2'):
	     
	    # name = entite.get('id')
	    nomEntite2 = entite2.find('nomEntite').text
	    for attribut in entite2.findall('attribut'):
	     	ide2 = attribut.find('id').text
	     	intitule = attribut.find('intitule').text
	    card2 = entite2.find('cardinalite').text
	
	for association in root.findall('association'):
	     
	    # name = entite.get('id')
	    nomAssos = association.find('nomAssos').text
	    for attribut in association.findall('attribut'):
	    	date = attribut.find('date').text
	
	#trace du fichier xml
	if arg3=="-t" :
	  	print nomEntite
		print ide
		print nom
		print prenom
		print card1
		
		print nomEntite2
		print ide2
		print intitule
		print card2
	
		print nomAssos
		print date
		#CREATION DU FICHIER SVG
	genererSVG(nomEntite,nom,prenom,card1,nomEntite2,card2,nomAssos)
	