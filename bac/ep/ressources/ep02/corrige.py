

print("\nNSI Partie Pratique - SUJET nº02\nBooleans/conditions et ...\n------------------------------------------\n\n• Exo 1 -->")

def correspond(mot:str,mot_a_trous:str)-> bool:
    """Renvoie vrai si les deux mots sont correspondants"""
    if len(mot)!= len(mot_a_trous):
        return False
    else:
        for i in range(len(mot)):
            if mot[i]!= mot_a_trous[i] and mot_a_trous[i]!= '*':
                return False
        return True
    
print(f"correspond('INFORMATIQUE','INFO*MA*IQUE) --> {correspond('INFORMATIQUE','INFO*MA*IQUE')}\ncorrespond('AUTOMATIQUE','INFO*MA*IQUE') --> {correspond('AUTOMATIQUE','INFO*MA*IQUE')}\ncorrespond('STOP','S*') --> {correspond('STOP','S*')}\ncorrespond('AUTO','*UT*') --> {correspond('AUTO','*UT*')}")

print("• Exo 2 -->") 

def est_cyclique(plan):
    '''
        Prend en paramètre un dictionnaire `plan` correspondant à
        un plan d'envoi de messages (ici entre les personnes A, B, C,
        D, E, F).
        Renvoie True si le plan d'envoi de messages est cyclique et
        False sinon.'''
    expediteur = 'A'
    destinataire = plan[expediteur] 
    nb_destinataires = 1
    while destinataire != expediteur:
        destinataire = plan[destinataire] 
        nb_destinataires = nb_destinataires + 1 
    return nb_destinataires == 6

print(est_cyclique({'A':'E','F':'A','C':'D','E':'B','B':'F','D':'C'})) #False
print(est_cyclique({'A':'E','F':'C','C':'D','E':'B','B':'F','D':'A'})) #True
print(est_cyclique({'A':'B','F':'C','C':'D','E':'A','B':'F','D':'E'})) #True
print(est_cyclique({'A':'B','F':'A','C':'D','E':'C','B':'F','D':'E'})) #False







print()