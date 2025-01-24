from this import d
import threading
import time

def oil_frying():
    time.sleep(10)
    print('Oil Fried')

def vegetables_cutting():
    time.sleep(4)
    print('Vegetables Cut')

def spices_collecting(spicy):
    time.sleep(6)
    print(f'Spices Collected making it {spicy}')

task1 = threading.Thread(target=oil_frying)
task2 = threading.Thread(target=vegetables_cutting)
task3 = threading.Thread(target=spices_collecting, args=('Spicy',))

task1.start()
task2.start()
task3.start()

print('All Threads Running')

task1.join()
task2.join()
task3.join()

print('All threads completed')