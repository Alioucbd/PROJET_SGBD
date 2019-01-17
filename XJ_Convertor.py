import svgwrite
def genererSVG(nomEntite,nom,prenom,card1,nomEntite2,intitule,card2,nomAssos,date,formt):
	if formt=="JSON":
		nom=""
		prenom=""
		card2=""
		card1=""
		intitule=""
		date=""
	dwg = svgwrite.Drawing('projet.svg')
		
		# CREATION D'UNE ENTITE
	dwg.add(dwg.rect((10, 10), (200, 100),
		stroke=svgwrite.rgb(0,0, 0, '%'),
		fill='white')
	)
		
		# ASSOCIER LA CARDINALITE A L'ENTITE
	dwg.add(dwg.text(card1,
	    insert=(65,125),
	    stroke='none',
	    fill=svgwrite.rgb(15, 15, 15, '%'),
	    font_size='15px',
	    font_weight="bold")
	)
		# LIGNE RELIANT DEUX CLASSE
	dwg.add(dwg.line((210, 40), (8, 40), 
		stroke=svgwrite.rgb(0,0,0, '%'))
	)

		# NOM DE L'ENTITE
	dwg.add(dwg.text(nomEntite,
	    insert=(65,25),
	    stroke='none',
	    fill='black',
	    font_size='15px',
	    font_weight="bold",
	    font_family="Arial")
	)
	dwg.add(dwg.text(nom,
	    insert=(65,67),
	    stroke='none',
	    fill='black',
	    font_size='12px',
	    font_weight="bold",
	    font_family="Arial")
	)
	dwg.add(dwg.text(prenom,
	    insert=(65,55),
	    stroke='none',
	    fill='black',
	    font_size='12px',
	    font_weight="bold",
	    font_family="Arial")
	)
		
		# 
	dwg.add(dwg.rect((10, 400), (200, 100),
	    stroke=svgwrite.rgb(0, 0, 0, '%'),
	    fill='white')
	)
	
	# 
	dwg.add(dwg.text(nomEntite2,
	    insert=(70, 420),
	    fill='black',
	    font_size='15px',
	    font_weight="bold",
	    font_family="Arial")
	)
	dwg.add(dwg.text(intitule,
	    insert=(70, 450),
	    fill='black',
	    font_size='15px',
	    font_weight="bold",
	    font_family="Arial")
	)
		
	
	# 
	dwg.add(dwg.text(card2,
	    insert=(65,395),
	    stroke='none',
	    fill=svgwrite.rgb(15, 15, 15, '%'),
	    font_size='15px',
	    font_weight="bold")
		)
	
	dwg.add(dwg.line((100, 110), (100, 400), 
		stroke=svgwrite.rgb(0,0,0, '%'))
	)
	
	
		#l'association
	dwg.add(dwg.line((210, 430), (8, 430), 
		stroke=svgwrite.rgb(0,0,0, '%'))
	)
	dwg.add(dwg.circle(center=(100,250),
	    r=60, 
	    stroke=svgwrite.rgb(15, 15, 15, '%'),
		    fill='white')
	)

	dwg.add(dwg.text(nomAssos,
	    insert=(70, 250),
	    fill='black',
	    font_size='15px',
	    font_weight="bold",
	    font_family="Arial")
	)
	dwg.add(dwg.text(date,
	    insert=(70, 270),
	    fill='black',
	    font_size='15px',
	    font_weight="bold",
	    font_family="Arial")
	)
	dwg.add(dwg.line((40, 255), (160, 255), 
		stroke=svgwrite.rgb(0,0,0, '%'))
	)
	# output our svg image as raw xml
	print(dwg.tostring())
	dwg.save()	
