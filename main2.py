
def skaiciuojam(iki):
    count = 1
    while count <= iki:
        yield count
        count += 1

counter = skaiciuojam(10)
print(next(counter))
print(next(counter))
print(next(counter))
sarasas = list(counter)
print(sarasas)
print(next(counter))
