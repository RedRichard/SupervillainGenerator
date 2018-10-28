from Villain import *
import random

class Generations:
    def __init__(self):
        self.first_gen = []
        self.megamentes = []
        self.sedusas = []
        self.sedumentes = []
        self.megamente_f = None
        self.sedusa_f = None
        self.sedumente_f = None

    def gen_first_generation(self):
        for i in range(0, 100):
            self.first_gen.append(Villain())
            self.first_gen[i].generate_abilities()
    
    def gen_second_generation(self):
        for i in range(0, 10):
            self.megamentes.append(self.gen_megamente_sedusa(self.first_gen))
            self.sedusas.append(self.gen_megamente_sedusa(self.first_gen))

    def gen_third_generation(self):
        for i in range(0, 10):
            self.sedumentes.append(self.gen_sedumente(self.megamentes[i], self.sedusas[i]))
    
    def gen_fourth_generation(self):
        self.megamente_f = self.gen_megamente_sedusa(self.sedumentes)
        self.sedusa_f = self.gen_megamente_sedusa(self.sedumentes)

    def gen_fifth_generation(self):
        self.sedumente_f = self.gen_sedumente(self.megamente_f, self.sedusa_f)

    def gen_sedumente(self, megamente, sedusa):
        num_megamente = random.randint(0, 10)
        abilities = megamente.get_abilities()[:num_megamente] + sedusa.get_abilities()[num_megamente:]
        return Villain(abilities)
    
    def gen_megamente_sedusa(self, villain_sample):
        abilities = []
        for i in range(0, 10):
            vil_i = random.randint(0,len(villain_sample)-1)
            abilities.append(villain_sample[vil_i].get_abilities()[i])
        return Villain(abilities)

generacion = Generations()
generacion.gen_first_generation()
for i in range(0,100):
    print(str(i+1) + ". " + str(generacion.first_gen[i].get_abilities()))

generacion.gen_second_generation()
print("Megamentes: ")
for i in range(0,10):
    print(generacion.megamentes[i].get_abilities())
print("Sedusas: ")
for i in range(0,10):
    print(generacion.sedusas[i].get_abilities())

generacion.gen_third_generation()
print("Sedumentes: ")
for i in range(0,10):
    print(generacion.sedumentes[i].get_abilities())

generacion.gen_fourth_generation()
print("Megamente cuarta: " + str(generacion.megamente_f.get_abilities()))
print("Sedusa cuarta: " + str(generacion.sedusa_f.get_abilities()))

generacion.gen_fifth_generation()
print("Megamente quinta: " + str(generacion.sedumente_f.get_abilities()))