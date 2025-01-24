import threading
import time

def file1():
    time.sleep(5)

    with open('file1.txt', 'w') as f:
        pass

    print('File 1 created')

def file2():
    time.sleep(5)

    with open('file2.txt', 'w') as f:
        pass

    print('File 2 created')

def file3():
    time.sleep(5)

    with open('file3.txt', 'w') as f:
        pass

    print('File 3 created')

def file4():
    time.sleep(5)

    with open('file4.txt', 'w') as f:
        pass

    print('File 4 created')

if __name__ == '__main__':
    start = time.perf_counter()

    thread1 = threading.Thread(target=file1)
    thread2 = threading.Thread(target=file2)
    thread3 = threading.Thread(target=file3)
    thread4 = threading.Thread(target=file4)

    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()

    thread1.join()
    thread2.join()
    thread3.join()
    thread4.join()

    print(f'Program took {time.perf_counter() - start} seconds to exectue!')