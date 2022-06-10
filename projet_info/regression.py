import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

class Regression:

    def __init__(self, data):
        self.data = data
        
    def list_variable(self):
        '''Renvoie la liste des variables de la table self.data
        '''
        return self.data[0]

    def get_indice_var(self,var):
        '''Renvoie l'indice de la colonne de la variable var
        '''
        l = self.list_variable()
        if var not in l:
            raise ValueError("la variable {} n'est pas dans la table".format(var))
        indice = 0
        while self.data[0][indice] != var:
            indice += 1
        return indice

    def __convert_to_int(self, var1, var2):
        '''Permet de convertir en float les valeurs des variables qui serviront à la regression
        Cette méthode ne sera utilisée que dans la méthode get_col_var1_et_var2() et nulle part autre
        '''
        l = self.list_variable()
        if var1 not in l:
            raise ValueError("la variable {} n'est pas dans la table".format(var1))
        if var2 not in l:
            raise ValueError("la variable {} n'est pas dans la table".format(var2))

        data = self.data
        n1 = self.get_indice_var(var1)
        n2 = self.get_indice_var(var2)
        for i in range(1,len(data)):
            data[i][n1] = float(data[i][n1])
            data[i][n2] = float(data[i][n2])
        return data

    def __get_col_var1_et_var2(self,var1,var2):
        '''Permet d'extraire une table de longueur 2 avec table[0] qui comprend la liste des valeurs de var1 
        et table[1] qui comprend la liste des valeurs de var2
        Cette méthode ne sera utilisée que dans la méthode regress() et nulle part autre
        '''
        data = self.__convert_to_int(var1, var2)
        n1 = self.get_indice_var(var1)
        n2 = self.get_indice_var(var2)
        t = []
        col1 = []
        col2 = []
        for i in range(1,len(data)):
            col1.append(data[i][n1])
            col2.append(data[i][n2])
        t.append(col1)
        t.append(col2)
        return t

    def regress(self, var1, var2):
        '''Effectue la regression linéaire entre var1 et var2
        '''
        X1 = self.__get_col_var1_et_var2(var1, var2)[0]
        Y1 = self.__get_col_var1_et_var2(var1, var2)[1]
        axes = plt.axes()
        axes.grid() # dessiner une grille pour une meilleur lisibilité du graphe
        plt.scatter(X1,Y1) # X et Y sont les variables qu'on a extraite dans le paragraphe précédent
        
        slope = stats.linregress(X1, Y1)[0]
        intercept = stats.linregress(X1, Y1)[1]

        def f(x,sl,interc):
            return x*sl + interc

        x = np.linspace(3000,25000, 70)
        y = f(x,slope,intercept)

        plt.plot(x, y)
        plt.show()


        