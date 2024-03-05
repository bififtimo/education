import random
import logging

# Пример 1(удачный): 2 77
# Пример 2(левая граница больше):  9 1
# Пример 3(граница меньше нуля):  -1 3
def generation(x, y):
    logging.basicConfig(level=logging.INFO, filename="2_6.log", filemode="w",
                        format="%(asctime)s %(levelname)s %(message)s")
    try:
        if x > y:
            raise ValueError("The left boundary of the segment is larger than the right")
        elif x < 0 or y < 0:
            raise ValueError("Bounds less than zero")
        else:
            num = random.randint(x, y)
            logging.info(f'Result of successful program execution: {num}.')
            return num
    except Exception as e:
        logging.info(f"An error has occurred: {e}")
        print("Операция завершилась некорректно. Попробуйте снова")

print("Введите границы дипазона по следующим правилам: 1.Границы не могут быть меньше нуля\n2.Левая граница должна быть меньше правой")
x = int(input("x = "))
y = int(input("y = "))
r = generation(x, y)
if r != None:
    print("Случайное число из диапазона: ", r)
