#-*- coding: utf-8 -*
import robot
r = robot.rmap()
r.lm('task1')
def task():
	pass
	#------- пишите код здесь -----

	for x in range (4):
		for i in range(3):
			r.paint()
			r.down(3)
		r.right()
		r.up(2)
		r.paint()
		for i in range(2):
			r.up(3)
			r.paint()
		r.right()
		r.up()
		for i in range(3):
			r.paint()
			r.down(3)
		r.up(9)
		r.right(2)


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
