from projet_info.importJSON import Json
from projet_info.importCSV import Csv
from projet_info.manipCSV import ManipCSV
from projet_info.manipDonneeMeteo import ManipDonneeMeteo
from projet_info.manipJSON import ManipJSON
from projet_info.manipPostesSynop import ManipPostesSynop
from projet_info.jointure import Jointure
from projet_info.pipeline import Pipeline
from projet_info.regression import Regression

pipe = Pipeline("synop.201301.csv.gz", "2013-01.json.gz")
pipe.lien_temperature_consommation()

