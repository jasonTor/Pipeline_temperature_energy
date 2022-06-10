import sys
sys.path.append('d:\\Users\\Jason\\Desktop\\entrainement\\projet_info')

from donnee import Donnee
import gzip
import csv

class Csv(Donnee):
    '''Gère l'import des fichiers CSV

    Attributes
    ----------
    folder : str
        adresse ou se trouve le fichier csv.gz
    filename : str
        nom du fichier (en format csv.gz)
    '''

    def __init__(self, folder, filename):
        self.folder = folder
        self.filename = filename

    def importer(self):
        '''Pour importer les fichiers csv.gz compressés,
        Renvoie en liste de liste les données des fichiers csv.gz
        '''
        data = []
        with gzip.open(self.folder + self.filename, mode='rt') as gzfile :
            synopreader = csv.reader(gzfile, delimiter=';')
            for row in synopreader :
                data.append(row)
        return data


    def copy_data(self):
        data = self.importer()
        copy = []
        for i in range(len(data)):
            copy.append(data[i])
        return copy
    

    def importer_non_compress(self):
        '''Pour importer les fichiers csv non compressés, 
        Cette méthode est uniquement utilisée dans la méthode d'après 
        matrice()
        '''
        # Attention à bien respecter les bonnes indentations
        data = []
        with open(self.filename, 'r') as f:
            obj = csv.reader(f) # Créer un objet csv à partir du fichier
            for row in obj:
                data.append(row)
        return data

    def matrice(self):
        '''Permet de retourner sous forme de liste de liste le fichier
        postesSynopAvecRegions.csv
        '''
        t = self.importer_non_compress()
        data = []
        for i in range(len(t)):
            row = t[i][0].split(';')
            data.append(row)
        return data

            

            



    



