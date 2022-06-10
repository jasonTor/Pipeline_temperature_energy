from manipDonneeMeteo import ManipDonneeMeteo
from manipJSON import ManipJSON

class Jointure:

    def __init__(self, data1, data2):    
        if type(data1) != list or type(data2) != list:
            raise ValueError("Il faut que la table soit une liste")
        self.data1 = data1
        self.data2 = data2

    def liste_variable_data1(self):
        d = []
        for i in range(len(self.data1[0])):
            d.append(self.data1[0][i].lower())
        return d

    def liste_variable_data2(self):
        d = []
        for i in range(len(self.data2[0])):
            d.append(self.data2[0][i].lower())
        return d

    
    def get_indice_var_data1(self, var):
        if var not in self.liste_variable_data1():
            raise ValueError("la variable n'existe pas")

        indice = 0
        while self.data1[0][indice] != var :
            indice += 1
        return indice


    def get_indice_var_data2(self, var):
        if var not in self.liste_variable_data2():
            raise ValueError("la variable n'existe pas")

        indice = 0
        while self.data2[0][indice] != var :
            indice += 1
        return indice


    def inner_join(self, var):
        d1 = self.data1
        d2 = self.data2
        d = []

        l1 = self.liste_variable_data1()
        l2 = self.liste_variable_data2()

        if var not in l1 or var not in l2:
            raise ValueError("la variable n'est ni dans data1 ni dans data2, la jointure est donc impossible")

        j1 = self.get_indice_var_data1(var)
        j2 = self.get_indice_var_data2(var)
        for i1 in range(len(d1)):
            for i2 in range(len(d2)):
                if d1[i1][j1] == d2[i2][j2]:
                    row = d1[i1] + d2[i2]
                    d.append(row)
        return d









