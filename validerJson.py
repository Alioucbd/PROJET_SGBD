import json
import svgwrite
from genererSVG import genererSVG
from pprint import pprint 
def validerJson(monFchier):
   dic=[]
   i=0
   with open(monFchier) as f_read:
      lst_dico = json.load(f_read)
      for key, dic in lst_dico.iteritems():
      #dic.append(value)
         print key
   #for key in lst_dico.keys(): 
        # print key
         if i==0:
            nomEntite2=key
            intitule=dic
            card2=dic
         if i==1:
               nomEntite=key
               nom=dic
               prenom=dic
               card1=dic
         if i==2 :
            nomAssos=key 
            date=dic
         i=i+1
   formt="JSON"      
   genererSVG(nomEntite,nom,prenom,card1,nomEntite2,intitule,card2,nomAssos,date,formt)
   print nomEntite2
   #rint dic