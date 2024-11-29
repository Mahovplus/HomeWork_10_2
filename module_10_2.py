import threading
import time
import threading
class Knight(threading.Thread):
    """Инизиализация объекта 'Рыцарь'."""
    def __init__(self, name, power):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power

    def run(self):
        print(f"{self.name}, на нас напали!")
        days = 0
        warriors = 100
        while warriors:
            warriors -= self.power
            days += 1
            time.sleep(1)
            print(f"{self.name} сражается {days} день(дня)..., осталось {warriors} воинов.")
        return print(f"{self.name} одержал победу спустя {days} дней(дня)!")


first_knight = Knight('Sir Lancelot', 10)
first_knight.start()
time.sleep(1)

second_knight = Knight("Sir Galahad", 20)
second_knight.start()
time.sleep(1)

first_knight.join()
second_knight.join()
print("Все битвы закончились")