import numpy as np
import matplotlib.pyplot as plt

'''
# Параметры нормального распределения
mean = 0 # Среднее значение
std_dev = 1 # Стандартное отклонение
num_samples = 1000 # Количество образцов

# Генерация случайных чисел, распределенных по нормальному распределению
data = np.random.normal(mean, std_dev, num_samples)

plt.hist(data, bins=100)

plt.xlabel("x ось")
plt.ylabel("y ось")
plt.title("Гистограма нормального распределения")

plt.show()
'''
random_array = np.random.rand(5)  # массив из 5 случайных чисел

plt.scatter(random_array, random_array)

plt.xlabel("x ось")
plt.ylabel("y ось")
plt.title("Точечный график")

plt.show()



print(random_array)

