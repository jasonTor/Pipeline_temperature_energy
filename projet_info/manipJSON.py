from manip import Manipulation

class ManipJSON(Manipulation):

    def __init__(self, data):
        self.data = data

    def list_variable(self):
        '''Renvoie la liste des variables de la table self.data
        '''
        return self.data[0]

    def get_indice_var(self, var):
        '''Renvoie l'indice de la colonne de la variable var
        '''
        l = self.list_variable()
        if var not in l:
            raise ValueError("La variable {} n'existe pas".format(var))
        indice = 0
        while self.data[0][indice] != var :
            indice += 1
        return indice

    def list_region(self):
        '''Renvoie la liste des régions
        '''
        data = self.data
        j = self.get_indice_var('region')
        ens = set()
        for i in range(1,len(data)):
            ens.add(data[i][j])
        l = list(ens)
        return l

    def get_col_region(self, region, var):
        '''Renvoie sous forme de liste toute les valeurs enregistrées de la variable 'var' 
        pour la region 'region'
        '''
        data = self.data
        l = self.list_region()
        if region not in l:
            raise ValueError("la station n'exsite pas")
        if var not in data[0]:
            raise ValueError("la variable n'existe pas")

        col = []
        indice_var = self.get_indice_var(var)
        indice_region = self.get_indice_var('region')
        for i in range(1,len(data)):
            if data[i][indice_region] == region:
                col.append(data[i][indice_var])
        return col

    def consommation_moyenne_par_region(self, region):
        '''Renvoie la consommation brute totale moyenne pour une région donnée donnée en argument
        '''
        l1 = self.list_region()
        if region not in l1 :
            raise ValueError("la région {} n'est pas dans la base de donnée".format(region))

        l2 = self.get_col_region(region, 'consommation_brute_totale')
        n = 0
        k = 0
        for i in range(len(l2)):
            if l2[i] != "mq":
                n += float(l2[i])
                k += 1
        return n/k


    def get_matrice_consommation_moyenne_par_region(self):
        '''Renvoie la matrice ou chaque ligne est de la forme [région, consommation moyenne]
        '''
        data = []
        data.append(['region', 'consommation'])
        l1 = self.list_region()
        for i in range(len(l1)):
            row = []
            row.append(l1[i])
            row.append(self.consommation_moyenne_par_region(l1[i]))
            data.append(row)
        return data