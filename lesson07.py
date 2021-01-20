class Worker:
    def __init__(self,worker = "unknown worker",salary = '10 000'):
        self.worker = worker
        self.salary = salary

    def work(self):
        print("Профессия: ", self.worker, "Его зарплата: ", self.salary)

    def __del__(self):
        print("Сейчас данный рабочий будет удалён")

class Driver(Worker):
    def __init__(self, salary = "15 000", name = "Unknown"):
        self.salary = salary
        self.name = name

    def __drive(self):
        print("Имя водителя", self.name)

    def work(self):
        print("Это ВОДИТЕЛЬ. Зарплата состовляет ", self.salary)
        self.__drive()


job = Worker("Сантехник", "16 000")#Нужно вписать сперва профессию и после зарплату
sotd = Driver("21 000", "Дима")#(salary of the driver) Нужно задать значение зарплаты и после ввести имя водителя


job.work()
sotd.work()