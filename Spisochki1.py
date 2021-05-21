
import random
import time
from random import *

def min_max():
        for i in range (len(vozrast)):
            if vozrast[i] == min(vozrast):
                print(min(vozrast)," ",imena[i])
        for i in range (len(vozrast)):
            if imena[i] == max(vozrast):
                print(max(vozrast), " ", imena[i])
def top():
	best_value = 0
	imena_max = []
	top_names = []
	top_score = []
	dyadki_copy = sportsmen.copy()
	results_copy = results.copy()
	for x in results:
		if x > best_value: 
			best_value = x
	top_score.append(best_value)
	for x in results:
		if x == best_value:
			index = results.index(x)
			imena_max.append(dyadki_copy[index])
			top_names.append(dyadki_copy[index])
			break
	while best_value > 0:
		try:
			best_value -= 1
			index = results_copy.index(best_value)
			top_names.append(dyadki_copy[index])
			top_score.append(results_copy[index])
			results_copy.pop(index)
			dyadki_copy.pop(index)
			if(best_value <= 0):
				break
		except:
			if(best_value <= 0):
				break
			continue

	return top_names, top_score
def sred():
        print("Средний возраст старых пенсионеров",(vozrast[0]+vozrast[1]+vozrast[2]+vozrast[3]+vozrast[4]+vozrast[5]+vozrast[6]+vozrast[7]+vozrast[8]+vozrast[9]+vozrast[10]+vozrast[11]+vozrast[12]+vozrast[13]+vozrast[14]+vozrast[14])/15)
imena = ["Тамара","Валентин","Олег","Валера","Наталья","Михаил","Степан","Кирилл","Александр","Мария","Кристина","Анна","Валерия","Людмила","Алексей","Иван"]
vozrast=[65,75,91,93,87,78,69,91,105,95,75,89,78,70,65]
while True:
		print("1 -  Составить список пенсионеров и вывести его на экран \n2 - Найти средний возраст работников; "
              "\n3 -  Отобразить список 10 самых молодых работников фирмы;\n4 -Осуществить поиск работников по году рождения и выведи список на экран ; "
              "\n5 - Добавить имена в список")
		a = input()
		if a == "1":
				print(imena)
		elif a == "2":
				sred()
		elif a == "3":
					top()
	