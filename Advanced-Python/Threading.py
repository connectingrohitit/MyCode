import threading
from datetime import datetime


def print_cube(num):
    for i in range(0, num):
        print(i)
    print("Cube is : {}".format(num * num * num))


def print_square(num):
    for i in range(0, num):
        print(i)
    print("Square is : {}".format(num * num))

time_format = '%H:%M:%S'
start_time = datetime.now()




print_cube(1000)
print_square(1000)

end_time = datetime.now()
execution_time = end_time - start_time

print('Start Time: {}'.format(start_time))
print('End Time: {}'.format(end_time))
print('Execution Time duration: {}'.format(execution_time.seconds))

# if __name__ == "__main__":
    # t1 = threading.Thread(target=print_square, args=(5,))
    # t2 = threading.Thread(target=print_cube, args=(5,))
    # t1.start()
    # t2.start()
    # t1.join()
    # t2.join()
    # print("Application Code executed successfully!!")
