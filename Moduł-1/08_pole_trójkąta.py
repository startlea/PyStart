xa = int(input("Podaj współżędną x wierzchołka A "))
ya = int(input("Podaj współżędną y wierzchołka A "))
xb = int(input("Podaj współżędną x wierzchołka B "))
yb = int(input("Podaj współżędną y wierzchołka B "))
xc = int(input("Podaj współżędną x wierzchołka C "))
yc = int(input("Podaj współżędną y wierzchołka C "))

p_abc = float(abs(1/2 * ((xb - xa) * (yc - ya) - (yb - ya) * (xc - xa))))

print(f"Pole trójkąta o podanych wierzchołkach wynosi: {p_abc}")