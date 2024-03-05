import logging

# Пример 1(неудачный): 2 3 4
# Пример 2(с одним корнем):  1 -2 1
# Пример 3(с двумя корнями):  1 -3 2
# Доп пример с делением на 0: 0 2 3

def quadratic_equation(a, b, c):
    logging.basicConfig(level=logging.INFO, filename="2_5.log", filemode="w",
                        format="%(asctime)s %(levelname)s %(message)s")
    try:
        discriminant = b ** 2 - 4 * a * c
        if discriminant < 0:
            raise ValueError('The discriminant is negative. There are no roots')
        elif discriminant == 0:
            x = -b / (2 * a)
            logging.info(f"Result of successful program execution: {x}.")
            return x
        else:
            x1 = (-b + discriminant ** 0.5) / (2 * a)
            x2 = (-b - discriminant ** 0.5) / (2 * a)
            logging.info(f"Result of successful program execution: {x1, x2}.")
            return x1, x2
    except Exception as e:
        logging.info(f"Error: {e}")
        logging.info(f"Failed operation")
        print("Операция завершилась некорректно. Попробуйте снова")


print("Введите коэффициенты a, b ,c: ")
a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))

r = quadratic_equation(a, b, c)
if r != None:
    print("Успешное выполнение программы: ", r)
