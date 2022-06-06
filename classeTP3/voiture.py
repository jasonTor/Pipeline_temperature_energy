class Voiture:
    
    def __init__(self, couleur, nom):
        self.couleur = couleur
        self.nom = nom
        self.vitesse = 0

    def accelere(self, accel):
        if accel > 10:
            raise ValueError("l'acceleration doit être inférieure ou égale à 10km/h")
        elif accel < 0:
            raise ValueError("l'acceleration doit être une valeur positive")
        if self.vitesse + accel > 130:
            self.vitesse = 130
        else:
            self.vitesse += accel

    def freine(self, decrement):
        if decrement < 0:
            raise ValueError("la deceleration doit être une valeur positive")
        
        if self.vitesse < decrement:
            self.vitesse = 0
        else :
            self.vitesse -= decrement

    def est_arrete(self):
        return self.vitesse == 0

    def __str__(self):
        return "voiture {} de couleur {} qui roule a une vitesse de {}".format(self.nom, self.couleur, self.vitesse)

if __name__ == '__main__':
    a = Voiture('rouge', 'bite')
    a.accelere(10)
    a.accelere(10)
    a.freine(20)
    a.accelere(5)
    a.freine(4)
    print(a.vitesse)
    