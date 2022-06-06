class Domino:

    def __init__(self, a, b):
        if a > 6:
            raise ValueError('doit être inferieur à 6')
        if b > 6:
            raise ValueError('doit être inferieur à 6')
        self.a = a
        self.b = b
    
    def __str__(self):
        return '[{},{}]'.format(self.a, self.b)

    def valeur(self):
        return self.a + self.b

    def retourne(self):
        tempa = self.a
        self.a = self.b
        self.b = tempa

    def accepte_apres(self, d):
        return self.b == d.a

class ListeDomino:

    def __init__(self):
        self.liste =[]

    def ajoute_domino(self,d):
        self.liste.append(d)

    def __str__(self):
        a = ''
        for d in self.liste :
            a = a + d.__str__() + ' -- '
        return a[:-4]


def creer_jeu_domino():
    d = ListeDomino()
    for i in range(7):
        for j in range(7):
            d.ajoute_domino(Domino(i,j))
    return d
                
                

if __name__ == '__main__':
    d = creer_jeu_domino()

    print(d)
