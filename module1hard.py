grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]] #дан список (list)
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'} #дано множество (set)
print(type(grades)) #для уверенности проверим тип данных
print(type(students)) #для уверенности проверим тип данных

#1) Поработаем со списком и приведём его в удобный для нас вид
#а именно, с помощью функций "sum", "len" и математ-ой операции деления посчитаем среднеарифметическое значение
#подсписков списка "grades" и присвоим получившимся значениям переменные

grades[0]=a=(sum(grades[0])/len(grades[0]))
grades[1]=b=(sum(grades[1])/len(grades[1]))
grades[2]=c=(sum(grades[2])/len(grades[2]))
grades[3]=d=(sum(grades[3])/len(grades[3]))
grades[4]=e=(sum(grades[4])/len(grades[4]))
print(grades) #выведем результат вычислений и преобразований
values=grades #для удобства переименуеем наш список т.к. далее его элементы мы будим использовать в качестве значений
print(values) #проверим изменения

#--------------------------------------------------------------------------------------------------------------------

#2)Поработаем с множеством и приведё в удобный для дальнейшего использования вид

students=frozenset({'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}) #изменим тип множество на список
keys=list(students) #присвоим полученному списку перменную, т.к. элементы списка будем исползовать в виде ключей
print(keys.sort()) #отсортируем по алфовиту полученный список
print(keys) #проверим что получилось
info = dict(zip(keys,values)) #объединим элементы двух списков в словарь
print(info) #проверим полученный результат
