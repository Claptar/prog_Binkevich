#-*- coding: utf-8 -*
import robot
r = robot.rmap()
r.lm('task1')
def task():
	pass
	#------- пишите код здесь -----

	lenght = int(input("Введите длинну "))
	hight = int(input("Введите высоту"))
	while (lenght > 15)or(hight > 10):
		print("Введите высоту меньше 24 и ширину меньше 10")
	r.right(int((24-lenght)/2))
	for x in range(lenght-1):
		r.paint()
		r.right()
	r.paint()
	r.left(int(lenght/2))
	for x in range(hight-1):
		r.down()
		r.paint()


#------- пишите код здесь -----
r.start(task)

#Отступ слева (tab) сохранять!
#r.help() - Список команд и краткие примеры
#r.demo() - показать решение этой задачи (только результат, не текст программы)
#r.demoAll() - показать все задачи (примерно 20 минут)

#r.rt() - вправо
#r.rt(3)- вправо на 3
#r.dn() - вниз
#r.up() - вверх
#r.lt() - влево
#r.pt() - закрасить  Paint

#r.cl() - закрашена ли клетка? Color
#r.fr() - свободно ли справа? freeRight
#r.fl() - свободно ли слева?  freeLeft
#r.fu() - свободно ли сверху? freeUp
#r.fd() - свободно ли снизу?  freeDown

#r.wr() - стена ли справа? freeRight
#r.wl() - стена ли слева?  freeLeft
#r.wu() - стена ли сверху? freeUp
#r.wd() - стена ли снизу?  freeDown


#red - красный
#blue - синий
#yellow - желтый
#green - зеленый
