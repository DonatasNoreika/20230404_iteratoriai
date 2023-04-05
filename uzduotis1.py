from time import sleep

def poriniai():
    number = 2
    while True:
        yield number
        number += 2

porinis = poriniai()

while True:
    print(next(porinis))
    sleep(0.1)

