from manipCSV import ManipCSV

class ManipDonneeMeteo(ManipCSV):

    def __init__(self,data):
        super().__init__(data) # data est déjà sous forme de liste de liste

    def get_col_station(self, station, var):
        '''Renvoie sous forme de liste toute les valeurs enregistrées groupées par la variable 'var' 
        pour la station 'station'
        '''
        data = self.data
        l = self.list_station()
        if station not in l:
            raise ValueError("la station n'exsite pas")
        if var not in data[0]:
            raise ValueError("la variable n'existe pas")

        col = []
        indice = self.get_indice_var(var)
        for i in range(1,len(data)):
            if data[i][0] == station:
                col.append(data[i][indice])
        return col

    def moyenne_temperature_station(self, station):
        '''Renvoie la température moyenne d'une station donnée
        '''
        l1 = self.list_station()
        if station not in l1:
            raise ValueError("la station n'existe pas")

        l2 = self.get_col_station(station, 't')
        n = 0
        k = 0
        for i in range(len(l2)):
            if l2[i] != 'mq':
                n += float(l2[i])
                k += 1
        return n/k

    def jointure_postesSynop(self, data_postesSynop):
        '''Effectue une jointure a gauche d'une table csv.gz et de la table data_postesSynop
        '''
        for n in range(len(data_postesSynop[0])):
            self.data[0].append(data_postesSynop[0][n]) # Cette boucle pour ajouter 'ID', 'Nom', 'Latitude', 'Longitude', 'Altitude', 'Region' 
        
        for i in range(1,len(self.data)):
            for k in range(1,len(data_postesSynop)):
                if self.data[i][0] == data_postesSynop[k][0]:
                    for n in range(len(data_postesSynop[0])):
                        self.data[i].append(data_postesSynop[k][n])
        return self.data
