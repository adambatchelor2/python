
#nb_year(1500, 5, 100, 5000) -> 15

def nb_year(p0, percent, aug, p):
    percent = percent/100
    year = 0
    while p0 < p:
        p0 += (p0*percent)
        p0 += aug
        year += 1
    return year

print(nb_year(1500, 5, 100, 5000))