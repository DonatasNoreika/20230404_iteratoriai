
def iteruoklis(objektas, func):
    iteratorius = iter(objektas)
    while True:
        try:
            item = next(iteratorius)
        except StopIteration:
            break
        else:
            func(item)


broliai = ['jurgis', 'antanas', 'aloyzas', 'martynas']
iteruoklis(broliai, print)


nums = [1, 2, 3, 4, 5]

iteruoklis(nums, lambda x: print(x ** 3))