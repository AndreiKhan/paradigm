import math
import statistics

def pirson(x, y):
    dx = []
    dy = []
    dxy = []
    sqrx = []
    sqry = []

    # Среднее ариф массивов
    mx = (sum(x)/len(x))
    my = (sum(y)/len(y))

    for i in range(len(x)):
        # Разница значений для x и y
        dx.append(x[i] - mx)
        dy.append(y[i] - my)

        # Сумма чисел будет = числителю формулы
        dxy.append(dx[i] * dy[i])

        # Корень суммы чисел двух массивов будет = знаменателю формулы
        sqrx.append(dx[i] ** 2)
        sqry.append(dy[i] ** 2)

    return (sum(dxy) / (math.sqrt(sum(sqry) * sum(sqrx))))


x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [10, 20, 29, 50, 1, 80, 99, 11, 45, 170]

# Моя функция для расчета Пирсона
print(pirson(x, y))

# Встроенная функция расчета Пирсона
print(statistics.correlation(x, y))