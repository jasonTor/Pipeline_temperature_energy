from manipCSV import ManipCSV

class ManipPostesSynop(ManipCSV):

    def __init__(self,data):
        super().__init__(data) # data est déjà sous forme de liste de liste

    def list_region(self):
        data = self.data
        j = self.get_indice_var('Region')
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
        indice_region = self.get_indice_var('Region')
        for i in range(1,len(data)):
            if data[i][indice_region] == region:
                col.append(data[i][indice_var])
        return col

    def moyenne_temperature_region(self, region):
        '''Renvoie la température moyenne enregistré pour la région 'région'
        '''
        l1 = self.list_region()
        if region not in l1 :
            raise ValueError("la région {} n'est pas dans la base de donnée".format(region))

        l2 = self.get_col_region(region, 't')
        n = 0
        k = 0
        for i in range(len(l2)):
            if l2[i] != "mq":
                n += float(l2[i])
                k += 1
        return n/k

    def get_matrice_moyenne_temperature_par_region(self):
        '''Renvoie une matrice donnant la temperature moyenne pour chaque region chaque ligne se présente sous la forme suivante [région,température moyenne]
        '''
        data = []
        data.append(['region', 'temperature'])
        l1 = self.list_region()
        for i in range(len(l1)):
            row = []
            row.append(l1[i])
            row.append(self.moyenne_temperature_region(l1[i]))
            data.append(row)
        return data

        

        
        