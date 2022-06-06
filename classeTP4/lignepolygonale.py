from point import Point

class LignePolygonale:
    def __init__(self, l):
        self.__sommets = l
        self.__nb_sommets = len(self.__sommets)

    def get_sommets(self):
        return self.__sommets

    def get_nb_sommets(self):
        return self.__nb_sommets

    def get_sommet_i(self, i):
        return self.__sommets[i]

    def set_sommet(self, i, p):
        self.__sommets[i] = p


if __name__ == '__main__':
    l = LignePolygonale([Point(1,2), Point(3,4)])
    

    