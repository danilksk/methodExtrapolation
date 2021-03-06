#разработка с помощью методов экстраполяции
# Область предопределённый переменных
N = 0.1 # Дополнение с учётом порядкового номера в списке группы 
base = [2.99, 2.66+N, 2.63, 2.56+N, 2.40, 2.22, 1.97, 1.72, 1.56+N, 1.42] # Исходный числовой ряд
prognoz = 3 # сколько переменных нужно прогнозировать
n = 3 # база метода скользящей средней (то сколько чисел мы берём и на что делим в формуле)
alpha = 0.3; # альфа для расчёта в третьем метода
#

#Область переменных для записи результата
y1 = 0 # задание переменных для вычисления (y - прогнозируемая переменная)
y2 = 0
y3 = 0
#

# Область временных переменных 
temp = 0
#

# Переменные для регрессивного анализа (вычисления и подстановки в формулы)
x_summa = 0 # Сумма всех X (Номеров месяцев)
y_summa = 0 # Сумма всех Y (Процентов)
xy_summa = 0 # Сумма произведений X на Y
x2_summa = 0 # Сумма квадратов X
y2_summa = 0 # Сумма квадратов Y
x_average = 0 # Средний X
y_average = 0 # Средний Y
a = 0 # У a и b нет обозначения, они просто часть основной формулы регрессивного анализа
b = 0
#

# метод со скользящей средней (первый метод)
print("1-ый метод")
massiv_method1 = list(base) # Создаём копию оригинального числового ряда для страховки и используем её
for j in range(prognoz): #начало цикла столько раз сколько нужно прогнозировать переменных
    for i in range(n): # цикл считывания переменных с конца для просчёта прогнозируемой переменной
        temp = temp + massiv_method1[len(massiv_method1)-i-1] # подсчёт числителя в формуле
    y1 = temp/n # конец формулы
    massiv_method1.append(y1) # добавление высчитанного прогнозируемого числа в конец первого скопированного списка
    print(len(massiv_method1)," - й член числового ряда","%.2f" %(y1))# вывод этого прогнозируемого числа (Здесь "%.2f" % - форматирование вывода (2 знака после запятой))
    temp = 0
#print ("Вид числового ряда при использовании 1-го метода:",massiv_method1)


# метод экспоненциального сглаживания
print("2-ой метод")
massiv_method2 = list(base) # Создаём копию оригинального числового ряда для страховки и используем её
for i in range(prognoz): #начало цикла столько раз сколько нужно прогнозировать переменных
    y2 = massiv_method2[len(massiv_method2)-1]*alpha + massiv_method2[len(massiv_method2)-2]*(1-alpha)# сама формула
    massiv_method2.append(y2) # добавление в конец списка
    print(len(massiv_method2)," - й член числового ряда","%.2f" %(y2))
#print ("Вид числового ряда при использовании 2-его метода:",massiv_method2)


# метод регрессионного анализа
print("3-ий метод")
massiv_method3 = list(base) # Создаём копию оригинального числового ряда для страховки и используем её
for i in range(len(massiv_method3)): # начало цикла для просчёта сумм (для формул), который идёт по всему списку (3-ей копией)
    x_summa = x_summa + (i+1) #просчёт суммы номеров месяцев
    y_summa = y_summa + massiv_method3[i] # просчёт суммые всех процентов
    xy_summa = xy_summa + ((i+1)*massiv_method3[i]) # просчёт суммы произведений
    x2_summa = x2_summa + pow((i+1),2) # просчёт суммы квадратов всех номеров месяцев (pow - возведение в степень)
    y2_summa = y2_summa + pow(massiv_method3[i],2)# просчёт суммы квадратов всех процентов
x_average = x_summa/len(massiv_method3) # высчет среднего x
y_average = y_summa/len(massiv_method3) # высчет среднего y
b = (xy_summa - len(massiv_method3)*x_average*y_average)/(x2_summa-len(massiv_method3)*pow(x_average,2)) # высчет b из формулы
a = y_average - b*x_average # высчет a из формулы
for i in range(prognoz): # весь цикл для подсчёта прогнозируемого числа
    y3 = a + b*(len(massiv_method3)+i+1) # непосредственно сама основная формула регрессивного анализа
    massiv_method3.append(y3)
    print(len(massiv_method3)," - й член числового ряда","%.2f" %(y3))
#print ("Вид числового ряда при использовании 3-его метода:",massiv_method3)


