import pygame
import random
import math
import pylab
from threading import Thread
from matplotlib import mlab
import numpy
import matplotlib.pyplot as plt

IS_ALIVE = True
pygame.init()
WIN_width = 640
WIN_height = 480
screen = pygame.display.set_mode((WIN_width, WIN_height),) # try out larger values and see what happens !
background = pygame.Surface(screen.get_size())
background_color = (200, 90, 100)
background.fill(background_color)
screen.blit(background, (0, 0))


class Vector:
    """
    Вспомогательный класс, для векторных оперций
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def normal_vector(self):
        """
        Нахождение вектора нормального данному
        :return: вектор нормальный данному
        """
        return Vector(-self.y, self.x)

    def multiplication(self, constant):
        """
        :param constant: Константа, на которую умножается вектор
        :return:
        """

        return Vector(self.x*constant, self.y*constant)

    def vector_scal_multiplication(self, vector):
        """
        :param vector: векор, на который умножается исходный вектор
        :return: результат скалярного умножения векторов
        """
        return self.x*vector.x + self.y*vector.y

    def sum(self, vector):
        """
        :param vector: вектор, который складываетяс с данным
        :return: результат сложения векторов
        """
        return Vector(self.x + vector.x, self.y + vector.y)

    def unit_vector(self):
        """
        :return: единичный вектор от данного
        """
        return Vector(self.x / math.sqrt(self.x ** 2 + self.y ** 2),
                      self.y / math.sqrt(self.x ** 2 + self.y ** 2))


class Ball:
    def __init__(self, x, y):
        self.x = x
        self.x0 = x
        self.y0 = y
        self.y = y
        self.radius = 5
        self.color = (255, 255, 255)
        self.vx = random.randint(-400, 400)/100
        self.vy = random.randint(-400, 400)/100

    def go(self):
        if self.x + self.radius >= WIN_width or self.x - self.radius <= 0:
            self.vx *= -1
        elif self.y + self.radius >= WIN_height or self.y - self.radius <= 0:
            self.vy *= -1
        out_of_range(self)
        pygame.draw.circle(screen, background_color, (int(self.x), int(self.y)), self.radius)
        self.x += self.vx
        self.y += self.vy
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)


def out_of_range(ball):
    """
    Предотвращение вылета шарика за границы сосуда
    """
    if math.fabs(ball.x) < ball.radius:
        n = (ball.radius - ball.x)/math.fabs(ball.vx)
        ball.x += (n - 0.3)*math.fabs(ball.vx)
    elif (math.fabs(WIN_width - ball.x) < ball.radius) and (math.fabs(WIN_width - ball.x) < ball.vx):
        n = (ball.x - WIN_width - ball.radius)/math.fabs(ball.vx)
        ball.x += (n - 0.3)*math.fabs(ball.vx)
    elif math.fabs(ball.y) < ball.radius:
        n = (ball.radius - ball.y)/math.fabs(ball.vy)
        ball.y += (n - 0.3)*math.fabs(ball.vy)
    elif (math.fabs(WIN_height - ball.y) < ball.radius) and (math.fabs(WIN_height - ball.y) < ball.vy):
        n = (ball.y - WIN_height - ball.radius)/math.fabs(ball.vy)
        ball.y += (n - 0.3)*math.fabs(ball.vy)


def collide(ball_1, ball_2):
    """
    Рассчёт столкновения двух шариков
    """
    if (ball_1.x - ball_2.x) ** 2 + (ball_1.y - ball_2.y) ** 2 <= (2*ball_1.radius) ** 2:
        r1 = Vector(ball_1.x, ball_1.y)
        r2 = Vector(ball_2.x, ball_2.y)
        v1 = Vector(ball_1.vx, ball_1.vy)
        v2 = Vector(ball_2.vx, ball_2.vy)
        line = Vector(ball_1.x - ball_2.x, ball_1.y - ball_2.y)
        line = line.unit_vector()
        normal = line.normal_vector()
        v_line_1 = v1.vector_scal_multiplication(line)
        v_line_2 = v2.vector_scal_multiplication(line)
        v_normal_1 = v1.vector_scal_multiplication(normal)
        v_normal_2 = v2.vector_scal_multiplication(normal)
        v_line_1, v_line_2 = v_line_2, v_line_1
        r = ball_1.radius * 2 - math.sqrt((ball_1.x - ball_2.x) ** 2 + (ball_1.y - ball_2.y) ** 2)
        if r > (math.fabs(v_line_2) + math.fabs(v_line_1)):
            n = r /(math.fabs(v_line_2) + math.fabs(v_line_1))
            if v_line_1 > 0:
                r1 = r1.sum(line.multiplication(n - 0.5))
                ball_1.x, ball_1.y = r1.x, r1.y
            elif v_line_2 > 0:
                r2 = r2.sum(line.multiplication(n - 0.5))
                ball_2.x, ball_2.y = r2.x, r2.y

        ball_1.vx = v_line_1 * line.x + v_normal_1 * normal.x
        ball_1.vy = v_line_1 * line.y + v_normal_1 * normal.y
        ball_2.vx = v_line_2 * line.x + v_normal_2 * normal.x
        ball_2.vy = v_line_2 * line.y + v_normal_2 * normal.y


def x_y_scale():
    global balls
    v = []
    num = []
    i = 0
    for ball in balls:
        v.append(math.sqrt(ball.vx**2 + ball.vy**2)*100)
    max_v = int(max(v) // 10 * 10)
    v = numpy.array(v)
    x = []
    for i in range(0, max_v, 20):
        i += 1
        number = len(v[v <= i])
        num.append(number)
        x.append(i)
    return [x, num, max_v]


def s_d_scale():
    global balls, V
    num = []
    i = 0
    max_v = int(max(V) // 10 * 10)
    v = numpy.array(V)
    x = []
    for i in range(0, max_v, 20):
        i += 1
        number = len(v[v <= i])
        num.append(number)
        x.append(i)
    return [x, num, max_v]


def plt_const(x, y):
    """
    Функция рассчитывает по МНК коэффициенты прямой по полученным координатам точек. Так же рассчитывает их погрешности.
    :param x: Массив абсцисс точек
    :param y: Массив оридинат точек
    :return: [значение углового коэфф a, значение коэфф b, значение погрешности a, значение погрешности b]
    """
    x = numpy.array(x)
    y = numpy.array(y)
    av_x = numpy.sum(x)/len(x)
    av_y = numpy.sum(y)/len(y)
    sigmas_x = numpy.sum(x*x)/len(x) - (numpy.sum(x)/len(x))**2
    sigmas_y = numpy.sum(y*y)/len(y) - (numpy.sum(y)/len(y))**2
    r = numpy.sum(x*y)/len(x) - av_x*av_y
    a = r/sigmas_x
    b = av_y - a*av_x
    return [a, b]

balls = []


def lab_start():
    global balls, IS_ALIVE
    clock = pygame.time.Clock()
    k = 18
    m = 15
    n = (k-1)*(m-1)
    for j in range(1, k):
        for i in range(1, m):
            if len(balls) == 1:
                balls.append(Ball(WIN_width/2, WIN_height/2))
            else:
                balls.append(Ball(20 + 40*i, 20 + 40*j))
    running = True
    while running:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                IS_ALIVE = False
                x = x_y_scale()[0]
                y = x_y_scale()[1]
                plt.plot(x, y, 'o', label='Гиббс')
                s = x_y_scale()[0]
                d = x_y_scale()[1]
                plt.plot(s, d, 'o', label='Больцман')
                plt.grid(True)
                plt.legend()
                plt.show()
                y1 = []
                x1 = []
                for i in range(1, len(y)):
                    if y[i] - y[i - 1] != 0 and y[i] - y[i - 1] != 0.0:
                        y1.append(y[i] - y[i - 1])
                        x1.append(i)
                plt.plot(x1, y1, 'o', label='Гиббс')
                d1 = []
                s1 = []
                for i in range(1, len(d)):
                    if d[i] - d[i - 1] != 0 and d[i] - d[i - 1] != 0.0:
                        d1.append(d[i] - d[i - 1])
                        s1.append(i)
                plt.plot(s1, d1, 'o', label='Гиббс')
                plt.grid(True)
                plt.legend()
                plt.show()
                x1 = numpy.array(x1)
                y1 = numpy.array(y1)
                y1 = numpy.log(y1/x1)
                x1 = numpy.log(x1*x1)
                r = plt_const(x1, y1)
                a = r[0]
                b = r[1]
                plt.plot(x1, y1, 'o', x1, a * x1 + b, label='Гиббс')
                s1 = numpy.array(s1)
                d1 = numpy.array(d1)
                d1 = numpy.log(d1 / s1)
                s1 = numpy.log(s1 * s1)
                r = plt_const(s1, d1)
                a1 = r[0]
                b1 = r[1]
                plt.plot(s1, d1, 'o', s1, a1 * s1 + b1, label='Гиббс')
                plt.grid(True)
                plt.legend()
                plt.show()
                IS_ALIVE = True

        screen.fill(background_color)
        for ball in balls:
            ball.go()
        for i in range(0, n):
            for t in range(i, n):
                if i != t:
                    collide(balls[i], balls[t])

        pygame.display.flip()


V = []
R = []
R2 = []


def plot_starter():
    global V, balls, R
    t = 0
    time = []
    balls[1].color = (255, 0, 0)
    while thread1.is_alive():
        if IS_ALIVE:
            t += 1
            print(t)
            V.append(math.sqrt(balls[1].vx**2 + balls[1].vy**2))
            print()

            pylab.pause(1)


thread1 = Thread(target=lab_start)
thread2 = Thread(target=plot_starter)

thread1.start()
thread2.start()

"""
r = (balls[1].x0 - balls[1].x)**2 + (balls[1].y0 - balls[1].y)**2
            R2.append(r)
            R_np = numpy.array(R2)
            av_r = numpy.average(R2)
            R.append(av_r)
            time.append(t)
            pylab.clf()
            r = plt_const(time, R)
            a = r[0]
            b = r[1]
            plt.plot(time, R, 'o', time, a * numpy.array(time) + b)
            pylab.grid(True)
            pylab.draw()
"""