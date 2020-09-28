import math

# Initialisation des variables
F = 10000  # en N
E = 210  # en GPa = 10^3 N/mm^2
L = 100  # en mm

# poutre rectangulaire
b = 10  # en mm
h = 20  # en mm
inertie_rect = (b * h ** 3) / 12

# poutre carrée
a = 15  # en mm
inertie_carre = (a ** 4)/12

# poutre ronde
d = 5  # en mm
inertie_rond = (math.pi * d ** 4) / 64

# poutre creuse
D = 15  # en mm
d = 5  # en mm
inertie_creu = math.pi * (D ** 4 - d ** 4) / 64

list_inertie = [inertie_rect, inertie_carre, inertie_rond, inertie_creu]

# Calcul de la section optimale
list_delta = []
for i in list_inertie:
    delta_ea = (F * L ** 3)/(3 * 1000 * E * i)
    list_delta.append(delta_ea)

min_deformation = min(list_delta)

list_section = ['rectangulaire', 'carrée', 'ronde', 'creuse']

for i in range(len(list_delta)):
    if list_delta[i] == min_deformation:
        print("Le type de section minimisant la deformation maximale est", list_section[i], ", avec une deformation de %.2f mm" % min_deformation)
