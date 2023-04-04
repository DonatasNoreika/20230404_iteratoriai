

def prime_generator(given_range):
    for num in range(given_range):
        if num > 1:
            for i in range(2, num):
                if num % i == 0:
                    break
            else:
                yield num

def infinite_prime_generator():
    num = 2
    while True:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            yield num
        num += 1

# pr_gr = prime_generator(10000)
infinite = infinite_prime_generator()

while True:
    try:
        print(next(infinite))
    except StopIteration:
        print("Pabaiga")
        break
