# Initialisation des variables

F = 10000  # en N
E = 210  # en GPa = 10^3 N/mm^2
L = 100  # en mm
b = 10  # en mm
h = 20  # en mm

# Calcul de l'inertie
inertie = (b * h ** 3) / 12

# Calcul de la déformation maximale
delta_max = (F * L ** 3) / (3 * 1000 * E * inertie)
print("La deformation maximale de la poutre de section rectangulaire est %.2f mm" % delta_max)
