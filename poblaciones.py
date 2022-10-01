#PROCESSING
hab_a=3500000
hab_b=5000000
año=1980
while hab_b>hab_a:
    hab_a=hab_a*1.07
    hab_b=hab_b*1.05
    año = año + 1

#OUTPUT
print("\nLa poblacion A sera igual a la poblacion B en el año " + str(año))