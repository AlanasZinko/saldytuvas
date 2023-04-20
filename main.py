class Gyvunas:
    def __init__(self, vardas):
        self.vardas = vardas

    def balsas(self):
        print("laiu")

    def judeti(self):
        print('Ramiai guliu...')

class Kate(Gyvunas):
    def balsas(self):
        print('Miau')

    def judeti(self):
        print('Einu lėtai')

class Suo(Gyvunas):
    def balsas(self):
        print('Au au!')

    def judeti(self):
        print('Bėgu greitai')


seskas = Gyvunas('Pilkis')
kate = Kate('Rainė')
suo = Suo('Margis')

print(seskas.vardas)
seskas.balsas()
seskas.judeti()

print(kate.vardas)
kate.balsas()
kate.judeti()

print(suo.vardas)
suo.balsas()
suo.judeti()