from multiprocessing import Pool


def cube(number):
    return number * number * number


if __name__ == "__main__":
    numbers = range(1, 11)
    pool = Pool()
    # map, apply, join, close
    result = pool.map(cube, numbers)
    print(result)

    # result = pool.apply(cube, numbers[0])
    # print(result)

    pool.close()
    pool.join()
