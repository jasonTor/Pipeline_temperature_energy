import sys
sys.path.append('C:\\Users\\jason\\OneDrive\\Bureau\\entrainement\\projet_info')

from donnee import Donnee
import gzip
import json

class Json(Donnee):
    '''Gère l'import des fichier Json

    Attributes
    ----------
    folder : str
        adresse ou se trouve le fichier json.gz
    filename : str
        nom du fichier (en format json.gz)
    '''

    def __init__(self, folder, filename):
        self.folder = folder
        self.filename = filename

    def importer(self):
        '''Cette méthode est utilisée uniquement dans la méthode get_fields()
        et nulle part autre
        '''
        with gzip.open(self.folder + self.filename, mode='rt') as gzfile :
            data = json.load(gzfile)
        return data

    def get_fields(self):
        '''Renvoie une liste de dictionnaire, ou chaque dictionnaire comporte
        comme clé : les noms des variables et en valeur : leur valeur associée
        '''
        tab = self.importer()
        fields = []
        for i in range(len(tab)):
            fields.append(tab[i]['fields'])
        return fields #c'est une liste de dictionnaire ou chaque dic comporte les valeurs de l'observation

    def get_nom_des_variables(self):
        ''' Renvoie une liste comportant le nom des variables
        '''
        fields = self.get_fields()
        l = []

        # On sait qu'il y a 13 variables donc on va chercher le premier
        # indice i de la table get_fields qui comporte 13 entrées
        indice = 0
        while len(fields[indice]) != 13:
            indice += 1 
            # indice = 52 en l'occurence à la fin de la boucle
        
        # En sachant que chaque clé de fields est le nom d'une variable
        for i in fields[52]:
            l.append(i)

        return l
    
    def matrice(self):
        '''Renvoie en liste de liste les données des fichiers json.gz,
        c'est cette méthode qui sera utilisé pour avoir toute les données
        '''
        l = self.get_nom_des_variables()
        table = [l]
        t = self.get_fields()
        for k in range(len(t)):
            t1 = []
            for i in range(len(l)):
                if l[i] in t[k].keys():
                    t1.append(t[k][l[i]])
                else :
                    t1.append('mq')
            table.append(t1)
        return table


    

    


        
    


