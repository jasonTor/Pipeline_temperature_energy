from importJSON import Json
from importCSV import Csv
from manipCSV import ManipCSV
from manipDonneeMeteo import ManipDonneeMeteo
from manipJSON import ManipJSON
from manipPostesSynop import ManipPostesSynop
from jointure import Jointure
from regression import Regression

class Pipeline:

    def __init__(self, data_csv, data_json):
        self.data_csv = data_csv
        self.data_json = data_json

    def lien_temperature_consommation(self):
        '''Execute le pipeline associé à la regression linéaire faisant ainsi le lien entre température et consommation
        '''
        datajs = Json("D:\\Users\\Jason\\Desktop\\entrainement\\données_électricité\\",self.data_json)
        data_2013_01 = datajs.matrice() # La table (liste de liste) des données de consommation d'energie (json.gz)

        datacsv = Csv("D:\\Users\\Jason\\Desktop\\entrainement\\données_météo\\",self.data_csv)
        data_201301 = datacsv.importer() # La table (liste de liste) des données météos (csv.gz)
        copy_data_201301 = datacsv.copy_data() # Copie de la table data_201301

        postesSynopAvecRegions = Csv("D:\\Users\\Jason\\Desktop\\entrainement\\","postesSynopAvecRegions.csv")
        data_postesSynop = postesSynopAvecRegions.matrice() # La table (liste de liste) des données postesSynopAvecRegion

        manip_data_201301 = ManipDonneeMeteo(copy_data_201301) #On lui donne copy_data_201301 pour que data_201301 ne soit pas modifier dans l'appel des différentes méthodes après
        join = manip_data_201301.jointure_postesSynop(data_postesSynop)

        manip_data_postesSynop = ManipPostesSynop(join)
        manip_data_2013_01 = ManipJSON(data_2013_01)

        a = manip_data_postesSynop.get_matrice_moyenne_temperature_par_region()
        b = manip_data_2013_01.get_matrice_consommation_moyenne_par_region() 

        objet_jointure = Jointure(a,b)
        table = objet_jointure.inner_join('region')

        table_regression = Regression(table)
        table_regression.regress('consommation','temperature')