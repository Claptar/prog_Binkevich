import math
import random
from tkinter import *
import graphics as gr
root = Tk()
fr = Frame(root)
root.geometry('1000x800')
canv = Canvas(root, bg='white')
n = 10
time_counter = 0
g = 9.8  # Ускорение свободного падения для снаряда.
Balls = []
for i in range(n):
    Balls.append(0)
score = 0
score_text = canv.create_text(200, 60, text='Попадания score = {} '.format(score), font='Arial 25', )


class Vector:
    """
    Вспомогательный класс, для векторных оперций
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Cannon:
    max_velocity = 100

    def __init__(self, canvas):
        self.canvas = canvas
        self.x = x = -30
        self.y = y = 550
        self.shell_num = 1
        self.direction = math.pi/4
        self.power = 0
        self.power_speed = 0
        self.cannon_diametr = 80
        self.line_length = 80
        self.line = canv.create_line(x + 30, y + 30,
                                     x + 110,
                                     y + 110,
                                     width=20, fill="red")
        self.oval = canv.create_oval(x, y,
                                     x + self.cannon_diametr,
                                     y + self.cannon_diametr,
                                     outline="black", fill="black")

    def aim(self, x, y):
        """
        Меняет направление direction так, чтобы он из точки
         (self.x, self.y) указывал в точку (x, y).
        :param x: координата x, в которую целимся
        :param y: координата y, в которую целимся
        :return: None
        """

        self.direction = math.atan((self.y - y)/(self.x - x))

        self.draw(self.x+40, self.y+40)

    def fire(self):
        """
        Создаёт объект снаряда (если ещё не потрачены все снаряды)
        летящий в направлении угла direction
        со скоростью, зависящей от длительности клика мышки
        :return: экземпляр снаряда типа Shell
        """
        if len(shells) < 10:
            self.time_length = self.stop_time - self.start_time
            self.power_speed = (self.power * self.time_length)/3
            shell = Shell(self.x + 40 + self.line_length*math.cos(self.direction),
                          self.y + 40 + self.line_length*math.sin(self.direction),
                          self.power_speed, self.power_speed, self.canvas, self.direction)

            shells.append(shell)
        else:
            canv.create_text(200, 20, text="Закончились снаряды", font='Arial 25', )
            print("Закончились снаряды")

    def draw(self, x_gun, y_gun):
        """
        Рисует дуло пушки, которое движется в зависимости от перемещений мышки
        :return:
        """
        global y_end
        self.canvas.delete(self.line)
        x_start = x_gun + math.cos(self.direction)*self.cannon_diametr/8
        y_start = y_gun + math.sin(self.direction) * self.cannon_diametr / 8
        x_end = x_gun + self.line_length*math.cos(self.direction)
        y_end = y_gun + self.line_length*math.sin(self.direction)
        self.line = self.canvas.create_line(
            x_start,
            y_start,
            x_end,
            y_end, width=20, fill="red"
        )


class Shell:
    global standard_radius
    standard_radius = 10

    def __init__(self, x, y, Vx, Vy, canvas, direction):
        self.x, self.y = x, y
        self.Vx, self.Vy = Vx, Vy
        self.direction = direction
        self.r = standard_radius
        x1 = x - standard_radius
        y1 = y - standard_radius
        x2 = x + standard_radius
        y2 = y + standard_radius
        self.delta_x = 0
        self.delta_y = 0

        self.canvas = canvas

        self.oval = self.canvas.create_oval(x1, y1, x2, y2, fill='red', outline="pink")

    def go(self, dt):
        """
        Сдвигает снаряд исходя из его кинематических характеристик
        и длины кванта времени dt
        в новое положение, а также меняет его скорость.
        :param dt: время элементарного перемещения
        :return: Движущийся снаряд
        """

        ax, ay = 0, g
        self.delta_x = self.Vx * dt * math.cos(self.direction) + ax * (dt ** 2) / 2
        self.delta_y = self.Vy * dt * math.sin(self.direction) + ay * (dt ** 2) / 2
        self.x += self.delta_x
        self.y += self.delta_y
        self.Vx += ax * dt
        self.Vy += -ay * dt

        self.draw()

        if self.y > 600:
            self.canvas.delete(self.oval)
        if self.x > 1000:
            self.Vx = -self.Vx

    def draw(self):
        """
        Рисует движущийся снаряд
        :return:
        """
        self.canvas.move(self.oval, self.delta_x, self.delta_y)

    def detect_collision(self, other):
        """
        Проверяет факт соприкосновения снаряда и объекта other
        :param other: объект, который должен иметь поля x, y, r
        :return: логическое значение типа bool
        """

        length = ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5
        return length <= self.r + other.r


class Target:
    standard_radius = 50

    def __init__(self, x, y, Vx, Vy, red, green, blue, r):
        self.x = x
        self.y = y
        self.Vx = Vx
        self.Vy = Vy
        self.design = canv.create_oval(x, y, x + r, y + r, fill=gr.color_rgb(red, green, blue))
        self.r = r

    def go(self):
        """
        Сдвигает шарик-мишень исходя из его кинематических характеристик
        и длины кванта времени dt
        в новое положение, а также меняет его скорость.
        :return:
        """
        if (self.x + self.r > 1000) or (self.x - self.r < 300):
            self.Vx *= -1
        elif (self.y + self.r > 600) or (self.y - self.r < 0):
            self.Vy *= -1
        canv.move(self.design, self.Vx, self.Vy)
        self.x += self.Vx
        self.y += self.Vy


def hit_checker(shell, target):
    if shell == 0 or target == 0:
        return False
    if (shell.x - target.x) ** 2 + (shell.y - target.y) ** 2 <= (target.r + shell.r) ** 2:
        return True


def collide(ball_1, ball_2):
    """
    Рассчёт столкновения двух шариков
    """
    if (ball_1.x - ball_2.x) ** 2 + (ball_1.y - ball_2.y) ** 2 <= ball_1.r ** 2:
        v1 = Vector(ball_1.Vx, ball_1.Vy)
        v2 = Vector(ball_2.Vx, ball_2.Vy)
        line = Vector(ball_1.x - ball_2.x, ball_1.y - ball_2.y)
        line.x = line.x / math.sqrt((ball_1.x - ball_2.x) ** 2 + (ball_1.y - ball_2.y) ** 2)
        line.y = line.y / math.sqrt((ball_1.x - ball_2.x) ** 2 + (ball_1.y - ball_2.y) ** 2)
        normal = Vector(-line.y, line.x)
        v_line_1 = v1.x * line.x + v1.y * line.y
        v_line_2 = v2.x * line.x + v2.y * line.y
        v_normal_1 = v1.x * normal.x + v1.y * normal.y
        v_normal_2 = v2.x * normal.x + v2.y * normal.y
        v_line_1, v_line_2 = v_line_2, v_line_1
        ball_1.Vx = v_line_1 * line.x + v_normal_1 * normal.x
        ball_1.Vy = v_line_1 * line.y + v_normal_1 * normal.y
        ball_2.Vx = v_line_2 * line.x + v_normal_2 * normal.x
        ball_2.Vy = v_line_2 * line.y + v_normal_2 * normal.y


def target_creator():
        r = 50
        x = random.randint(400, 800)
        y = random.randint(100, 600)
        Vx = random.randint(-3, 3)
        Vy = random.randint(-3, 3)
        red = random.randint(50, 255)
        green = random.randint(50, 255)
        blue = random.randint(50, 255)
        return Target(x, y, Vx, Vy, red, green, blue, r)


def mouse_move_handler(event):
    """
    Направляет дуло пушки в сторону курсора
    :param event: перемещение курсора по экрану
    :return: Координаты курсорв мыши
    """
    cannon.aim(event.x, event.y)


def tick():
    global Balls, score, score_text
    """
    Считает время нажатия клавиши мыши
    :return:
    """
    for i in range(n):
        if Balls[i] == 0:
            Balls[i] = target_creator()
    for k in range(n-1):
        for t in range(k, n):
            if k != t:
                collide(Balls[k], Balls[t])
    for g in range(n):
        Balls[g].go()
    global time_counter
    time_counter += 1
    for g in range(len(shells)):
        if shells[g] != 0:
            shells[g].go(0.1)
            for i in range(len(Balls)):
                if hit_checker(shells[g], Balls[i]):
                    canv.delete(Balls[i].design)
                    canv.delete(shells[g].oval)
                    Balls[i] = 0
                    shells[g] = 0
                    score += 1
                    canv.delete(score_text)
                    score_text = canv.create_text(200, 60, text='Попадания score = {} '.format(score), font='Arial 25')


    root.after(10, tick)


def time_start(event):
    """
    Включает счетчик в момент нажания левой клавиши мыши
    :param event: Момент нажатия левой клавиши
    :return: Начальное значение времени
    """
    global time_counter
    cannon.start_time = time_counter


def time_stop(event):
    """
    Выключает счетчик после отпускания левой клавиши
    Обнуляет счетчик
    Запускает снаряд в момент момент отпускания левой клавиши
    :param event: Момент отпускания левой клавиши
    :return: Конечное значение времени
    """
    global time_counter
    cannon.stop_time = time_counter
    cannon.fire()
    time_counter = 0


def power_maker(event):
        cannon.power = 2 * power_scale.get()


canv.pack(fill=BOTH, expand=1)

power_scale = Scale(root, orient=HORIZONTAL,
                length=300,
                from_=0, to=10, tickinterval=1, resolution=1, width=5)
power_scale.pack()
power_scale.set(1)

canv.bind('<Motion>', mouse_move_handler)
canv.bind("<ButtonPress-1>", time_start)
canv.bind("<ButtonRelease-1>", time_stop)
power_scale.bind("<Motion>", power_maker)
shells = []
cannon = Cannon(canv)

tick()
root.mainloop()
