from threading import *
from time import sleep

class Employee(Thread):
    def run(self) -> None:
        for i in range(35):
            print('Mohanad',24)
            sleep(1)


class Department(Thread):
    def run(self) -> None:
        for i in range(59):
            print('IT')
            sleep(1)

emp=Employee()

dep=Department()

emp.start()
sleep(0.2)
dep.start()

emp.join()
dep.join()

print('done')