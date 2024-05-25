import math
import statistics as stat

import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as sp
from sklearn.neighbors import KernelDensity

import function

NUM_SAMPLES = 10

# Чтение файла
numOfPoints: int
numOfPointsInOneUnderArray: int
with open("C:\\Users\\danii\\Downloads\\TASK2A.txt", 'r') as file:
    numOfPoints = int(file.readline().split(' = ')[1])
    numOfPointsInOneUnderArray = numOfPoints // NUM_SAMPLES
    data = np.fromstring(file.readline(), dtype=float, sep=' ')

# Инициализия подвыборок
np.random.shuffle(data)
subData: list = []
for i in range(NUM_SAMPLES):
    sub_samples = []
    for j in range(1 + (i - 1) * numOfPoints // 10, i * numOfPoints // 10 + 1):
        sub_samples.append(data[j])
    subData.append(sub_samples)

# Cортировка значений
data.sort()
for i in range(NUM_SAMPLES):
    list.sort(subData[i])
    print("№{} [len={}]: {}...".format(i + 1, len(subData[i]), subData[i][:5]))
print("Full data [len={}]: {}...\nMin: {}\nMax: {}\n".format(len(data), data[:5], data[0], data[numOfPoints - 1]))
# Функция распределения и гистограммы
m = 100  # кол-во интервалов

minValue = min(data)  # минимальное значение в выборке
maxValue = max(data)  # максимальное значение в выборке
distributionFun = np.zeros(m)
h = (maxValue + 0.00000000001 * maxValue - minValue) / m  # шаг, с которым идут интервалы
steps = []  # массив точек с шагом h
for t in range(1, m + 1):
    steps.append(t * h + minValue)
index = 0
for value in data:
    if value > steps[index]:
        p = int(abs(steps[index] - value) / h) + 1
        for i in range(1, p):
            distributionFun[index + i] = distributionFun[index]
        distributionFun[index] = distributionFun[index - 1]
        index += p
    distributionFun[index - 1] += 1
fig12, chart = plt.subplots(1, 1)
chart.set_title("Выборочная функция распределения")
chart.bar(steps, distributionFun / len(data), h)

# абсолютная гистограмма
fig122, chart = plt.subplots(1, 1)
chart.set_title("Абсолютная гистограмма")
chart.hist(data, 100)

# Относительная гистограмма
fig123, chart = plt.subplots(1, 1)
chart.set_title("Относительная гистограмма")
chart.hist(data, 100, density=True)

# ядерное оценивание
linspace = np.linspace(minValue, maxValue, 100, dtype=float)


def kde(sample, x, kernel='gaussian', bandwidth=0.15) -> np.ndarray:
    kde_ = KernelDensity(kernel=kernel, bandwidth=bandwidth)
    kde_.fit(sample[:, np.newaxis])
    log_pdf = kde_.score_samples(x[:, np.newaxis])
    return np.exp(log_pdf)


def kde_prob(sample, plot, kernel='gaussian', bandwidth=0.15, **kwargs):
    kwargs['label'] = kwargs.get('label', 'kde')
    density = kde(sample, linspace, kernel, bandwidth)
    plot.plot(linspace, density, **kwargs)


fig_2, chart = plt.subplots(1, 1)
chart.set_title("ядерное оценивание")
chart.hist(data, 100, density=True)
kde_prob(data, chart, kernel="tophat", bandwidth=0.4, label="Tophat kernel")
kde_prob(data, chart, kernel="linear", bandwidth=0.4, label="Triangular kernel")
kde_prob(data, chart, kernel="gaussian", bandwidth=0.4, label="Gauss kernel")
fig_2.legend()

# Точечные оценки
print("\n================== ТОЧЕЧНЫЕ ОЦЕНКИ =========================")
empty = np.zeros(11)
median = [stat.median(data)]  # медианы
mean = [stat.mean(data)]  # среднее арифметическое (мат. ожидание)
midRange = [(minValue + maxValue) / 2]  # средина размаха
dispersion = [functions.dispersion(data, mean[0])]  # дисперсия s^2
rootDispersion = [math.sqrt(dispersion[0])]  # корень из дисперсии s
centralMoment3 = [functions.centralMoment(data, 3, mean[0])]  # 3-ий центральный момент
centralMoment4 = [functions.centralMoment(data, 4, mean[0])]  # 4-ый центральный момент
asymmetry = [functions.asymmetry(centralMoment3[0], rootDispersion[0])]  # асимметрия
kurtosis = [functions.kurtosis(centralMoment4[0], dispersion[0])]  # эксцесс
interquantileInterval = [np.quantile(data, 0.025), np.quantile(data, 0.975)]

index = 1
for n in subData:
    median.append(stat.median(n))
    mean.append(stat.mean(n))
    midRange.append((min(n) + max(n)) / 2)
    dispersion.append(functions.dispersion(n, mean[index]))
    rootDispersion.append((math.sqrt(dispersion[index])))
    centralMoment3.append(functions.centralMoment(n, 3, mean[index]))
    centralMoment4.append(functions.centralMoment(n, 4, mean[index]))
    asymmetry.append(centralMoment3[index] / pow(rootDispersion[index], 3))
    kurtosis.append(functions.kurtosis(centralMoment4[index], dispersion[index]))
    index += 1
print("Min: {}\nMax: {}".format(minValue, maxValue))


def printWithFull(string_name, arr):
    print("{} [{:.4f}]\n\t{}".format(string_name, arr[0],
                                     '\n\t'.join(map(lambda x: "№{} {:.4f}".format(arr.index(x), x), arr[1:]))))


def printWithoutFull(string_name, arr):
    print("{}\n\t{}".format(string_name, '\n\t'.join(map(lambda x: "№{} {}".format(arr.index(x) + 1, x), arr))))


printWithFull("x_med", median)
printWithFull("M[x]", mean)
printWithFull("x_cp", midRange)
printWithFull("s^2", dispersion)
printWithFull("s", rootDispersion)
printWithFull("∘µ_3", centralMoment3)
printWithFull("∘µ_4", centralMoment4)
printWithFull("As", asymmetry)
printWithFull("Ex", kurtosis)

print("J (значения) : {}\n".format(interquantileInterval))
fig3 = plt.figure()
chart1 = plt.subplot(9, 1, 1)
chart1.set_title('Медианы')
chart1.set_yticks([])
chart1.plot(median, empty, 'r+')
chart1.plot(median[0], 0, 'rp')

chart2 = plt.subplot(9, 1, 3)
chart2.set_title('Среднее арифметическое (мат ожидание)')
chart2.set_yticks([])
chart2.plot(mean, empty, 'b+')
chart2.plot(mean[0], 0, 'bp')

chart3 = plt.subplot(9, 1, 5)
chart3.set_title('Средина размаха')
chart3.set_yticks([])
chart3.plot(midRange, empty, 'g+')
chart3.plot(midRange[0], 0, 'gp')

chart4 = plt.subplot(9, 1, 7)
chart4.set_title('Дисперсия')
chart4.set_yticks([])
chart4.plot(dispersion, empty, 'g+')
chart4.plot(dispersion[0], 0, 'gp')

chart5 = plt.subplot(9, 1, 9)
chart5.set_title('Среднеквадратичное отклонение')
chart5.set_yticks([])
chart5.plot(rootDispersion, empty, 'g+')
chart5.plot(rootDispersion[0], 0, 'gp')

fig3_1 = plt.figure()

chart1 = plt.subplot(7, 1, 1)
chart1.set_title('Третий центральный момент')
chart1.set_yticks([])
chart1.plot(centralMoment3, empty, 'r+')
chart1.plot(centralMoment3[0], 0, 'rp')

chart2 = plt.subplot(7, 1, 3)
chart2.set_title('Четвертый центральный момент')
chart2.set_yticks([])
chart2.plot(centralMoment4, empty, 'b+')
chart2.plot(centralMoment4[0], 0, 'bp')

chart3 = plt.subplot(7, 1, 5)
chart3.set_title('Асимметрия')
chart3.set_yticks([])
chart3.plot(asymmetry, empty, 'g+')
chart3.plot(asymmetry[0], 0, 'gp')

chart4 = plt.subplot(7, 1, 7)
chart4.set_title('Эксцесс')
chart4.set_yticks([])
chart4.plot(kurtosis, empty, 'g+')
chart4.plot(kurtosis[0], 0, 'gp')

# 1.4
# Интервальные оценки
print("\n====================== 1.4. Интервальные оценки ======================")
Q = 0.8  # доверительная вероятность

leftChi2inv = sp.chi2.ppf(0.9, numOfPoints - 1)
rightChi2inv = sp.chi2.ppf(0.1, numOfPoints - 1)
t_inv = sp.t.ppf(0.9, numOfPoints - 1)
meanInterval = [functions.meanInterval(numOfPoints, mean[0], rootDispersion[0], t_inv)]
dispersionInterval = [functions.dispersionInterval(numOfPoints, dispersion[0], leftChi2inv, rightChi2inv)]


def printInterval(string_name, arr):
    print("{} {}\n\t{}".format(string_name, arr[0],
                               '\n\t'.join(map(lambda x: "№{} {}".format(arr.index(x), x), arr[1:]))))


for i in range(1, 11):
    meanInterval.append(functions.meanInterval(numOfPointsInOneUnderArray, mean[i], rootDispersion[i], t_inv))
    dispersionInterval.append(functions.dispersionInterval(numOfPoints, dispersion[i], leftChi2inv, rightChi2inv))
printInterval("Интервальные оценки для мат. ожидания:", meanInterval)
printInterval("Интервальные оценки для дисперсии:", dispersionInterval)

# Для мат. ожидания
plt.figure()
axes = [plt.subplot(11, 1, 1)]
axes[0].set_yticks([])
axes[0].set_ylabel('Full')
plt.title('Интервальные оценки мат. ожидания')
plt.setp(axes[0].get_xticklabels(), visible=False)
plt.plot(mean[0], 0, 'rp')
plt.plot(meanInterval[0][0], 0, 'b<')
plt.plot(meanInterval[0][1], 0, 'b>')

for i in range(1, 11):
    axes.append(plt.subplot(11, 1, i + 1, sharex=axes[0]))
    axes[i].set_yticks([])
    axes[i].set_ylabel(str(i))
    if i < 10:
        plt.setp(axes[i].get_xticklabels(), visible=False)
    plt.plot(mean[i], 0, 'r+')
    plt.plot(meanInterval[i][0], 0, 'b<')
    plt.plot(meanInterval[i][1], 0, 'b>')
mathScale = max(mean) - min(mean)


# Для дисперсии
plt.figure()
axes = [plt.subplot(11, 1, 1)]
axes[0].set_yticks([])
axes[0].set_ylabel('Full')
plt.title('Интервальные оценки дисперсии')
plt.setp(axes[0].get_xticklabels(), visible=False)
plt.plot(dispersion[0], 0, 'rp')
plt.plot(dispersionInterval[0][0], 0, 'b<')
plt.plot(dispersionInterval[0][1], 0, 'b>')

for i in range(1, 11):
    axes.append(plt.subplot(11, 1, i + 1, sharex=axes[0]))
    axes[i].set_yticks([])
    axes[i].set_ylabel(str(i))
    if i < 10:
        plt.setp(axes[i].get_xticklabels(), visible=False)
    plt.plot(dispersion[i], 0, 'r+')
    plt.plot(dispersionInterval[i][0], 0, 'b<')
    plt.plot(dispersionInterval[i][1], 0, 'b>')
dispScale = max(dispersion) - min(dispersion)

# Толерантные пределы
print("\n============================= ТОЛЕРАНТНЫЕ ПРЕДЕЛЫ ===================================")
p = 0.95  # вероятность для интерквантильного промежутка
q = 0.8  # доверительная вероятность
tolerantIntervalAvg = [0, 0]  # массив для толерантных пределов
k = functions.find_k(numOfPoints, p, q)  # кол-во отбрасываемых точек
print("Предел k : {};\t\tЗначение биномиального распределения : {};".format(k, sp.binom.cdf(numOfPoints - k,
                                                                                            numOfPoints, p)))

# Для всей выборки относительно среднего арифметического
if k % 2 == 0:
    left_lim = int(k / 2)
    right_lim = numOfPoints - left_lim
    tolerantIntervalAvg[0], tolerantIntervalAvg[1] = data[left_lim], data[right_lim]
else:
    left_lim = int((k - 1) / 2)
    right_lim = int(numOfPoints - (k - 1) / 2)
    tolerantIntervalAvg[0], tolerantIntervalAvg[1] = data[left_lim], data[right_lim]

# Для всей выборки относительно нуля
# Для этого возьмем модули отрицательных значений и пересортируем выборку
dataAbs = np.sort(np.array(data))
tolerantIntervalZero = [-dataAbs[numOfPoints - k + 1], dataAbs[numOfPoints - k + 1]]
print("Толерантные пределы для всей выборки относительно среднего: {}".format(tolerantIntervalAvg))
print("Толерантные пределы для всей выборки относительно нуля: {}".format(tolerantIntervalZero))

plt.figure()
plt.title("Толерантные пределы относительно среднего значения")
plt.yticks([])
plt.plot(tolerantIntervalAvg[0], 0, 'b<')
plt.plot(tolerantIntervalAvg[1], 0, 'b>')
plt.plot(interquantileInterval[0], 0, 'ro')
plt.plot(interquantileInterval[1], 0, 'ro')
plt.legend(("Левый толерантный предел", "Правый толерантный предел", "Интерквантильный промежуток"), 
loc='upper right')

plt.figure()
plt.title("Толерантные пределы относительно нуля")
plt.yticks([])
plt.plot(tolerantIntervalZero[0], 0, 'b<')
plt.plot(tolerantIntervalZero[1], 0, 'b>')
plt.legend(("Левый толерантный предел", "Правый толерантный предел"), loc='upper right')


# Считаем параметрические толерантные пределы подвыборок
kTolerantMulti = 1.96
paramTolerantInterval = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
for i in range(10):
    paramTolerantInterval[i][0] = mean[i + 1] - kTolerantMulti * rootDispersion[i + 1]
    paramTolerantInterval[i][1] = mean[i + 1] + kTolerantMulti * rootDispersion[i + 1]
printWithoutFull("Параметрические толерантные интервалы для подвыборок:", paramTolerantInterval)

plt.figure()
axes = []
for i in range(10):
    if i == 0:
        axes.append(plt.subplot(10, 1, i + 1))
        plt.title("Параметрические толерантные пределы для подвыборок")
    else:
        axes.append(plt.subplot(10, 1, i + 1, sharex=axes[0]))
    axes[i].set_yticks([])
    axes[i].set_ylabel(str(i + 1))
    if i < 9:
        plt.setp(axes[i].get_xticklabels(), visible=False)
    plt.plot(paramTolerantInterval[i][0], 0, 'b<')
    plt.plot(paramTolerantInterval[i][1], 0, 'b>')
    plt.plot(mean[i + 1], 0, 'ro')

plt.show()
