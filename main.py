from threading import Thread
from time import sleep

class Class1(Thread):
    def run(self):
        for i in range(5):
            print("class1")
            sleep(1)

class Class2(Thread):
    def run(self):
        for i in range(5):
            print("class2")
            sleep(1)

obj1 = Class1()
obj2 = Class2()

# method start inside the Thread class is used to perform multi threading
obj1.start()
sleep(0.2)
obj2.start()

#joining the threads
obj1.join()
obj2.join()

print("main")
