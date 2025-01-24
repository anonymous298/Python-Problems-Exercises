from ast import arg
import multiprocessing
import time



def square(number):
    num = 1
    for i in range(number + 1):
        num ** 2

def main():
    print(multiprocessing.cpu_count())

    start = time.perf_counter()

    process1 = multiprocessing.Process(target=square, args=(250000000,))
    process2 = multiprocessing.Process(target=square, args=(250000000,))

    process1.start()
    # process2.start()

    process1.join()
    # process2.join()

    print(f'Finished in {time.perf_counter() - start} seconds')

if __name__ == '__main__':
    main()