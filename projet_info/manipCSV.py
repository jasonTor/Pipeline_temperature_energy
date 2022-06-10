from manip import Manipulation

class ManipCSV(Manipulation):
    
    def __init__(self, data):
        self.data = data # data est déjà sous forme de liste de liste


    def list_variable(self):
        return self.data[0]
    

    def get_indice_var(self, var):
        '''Renvoie l'indice j de la colonne associée à la variable 'var'
        c'est le j de : data[0][j] = var

        Examples
        --------
        >>> datacsv = Csv("D:\\Users\\Jason\\Desktop\\entrainement\\données_météo\\","synop.201301.csv.gz")
        >>> manip = ManipCSV(datacsv.importer())
        >>> manip.get_indice_var('t') 
        7
        '''
        l = self.list_variable()
        if var not in l:
            raise ValueError("La variable {} n'existe pas".format(var))
        indice = 0
        while self.data[0][indice] != var :
            indice += 1
        return indice # En l'occurence pour la température indice = 7 -> data[0][7] = 't'

    def list_station(self):
        '''Renvoie sous forme de liste les identifiants des stations
        '''
        data = self.data
        ens = set()
        for i in range(1,len(data)):
            ens.add(data[i][0])
        l = list(ens)
        return l









        

    





