
def pin_breaker():
    num = 0
    while num < 10000:
        yield f"{num:04}"
        num += 1

PIN = '9999'

breaker = pin_breaker()

while True:
    spejimas = next(breaker)
    print(spejimas)
    if spejimas == PIN:
        print(f"Kodas {spejimas} nulaužtas")
        break

