class Complexe:

    def __init__(self, re, im):
        self.__re = re
        self.__im = im

    def __add__(self, b):
        r = self.__re + b.get_re()
        i = self.__im + b.get_im()
        return Complexe(r,i)

    def get_re(self):
        return self.__re
    
    def get_im(self):
        return self.__im

    def __str__(self):
        return "{} + {}i".format(self.__re, self.__im)




if __name__ == '__main__':
    z = Complexe(4,2)
    c = Complexe(2,7)
    str(z)
