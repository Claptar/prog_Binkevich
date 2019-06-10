import sys, random
import pygame
from pygame.locals import *
import pymunk
import pymunk.pygame_util
import pylab
from threading import Thread
from matplotlib import mlab
import numpy
import matplotlib.pyplot as plt
import math

WIN_width = 500
WIN_height = 800
IS_ALIVE = True
balls = []
H = []


def add_ball(space, x, y):
    """Add a ball to the given space at a random position"""
    mass = 1
    radius = 2
    inertia = pymunk.moment_for_circle(mass, 0, radius, (0, 0))
    body = pymunk.Body(mass, inertia)
    body.position = x, y
    shape = pymunk.Circle(body, radius, (0, 0))
    space.add(body, shape)
    shape.elasticity = 1.0
    return shape


def add_balls(space, balls):
    global WIN_width, WIN_height
    k = 20
    m = 20
    for j in range(1, k):
        for i in range(1, m):
            if len(balls) == 1:
                ball_shape = add_ball(space, WIN_width / 2, 800 - random.expovariate(1/400))
                balls.append(ball_shape)

            else:
                ball_shape = add_ball(space, random.randint(20, WIN_width - 50), 800 - random.expovariate(1/400))
                balls.append(ball_shape)


def add_static_L(space):
    body1 = pymunk.Body(body_type=pymunk.Body.STATIC)  # 1
    body2 = pymunk.Body(body_type=pymunk.Body.STATIC)  # 1
    body3 = pymunk.Body(body_type=pymunk.Body.STATIC)  # 1
    body4 = pymunk.Body(body_type=pymunk.Body.STATIC)
    body1.position = (0, WIN_height / 2)
    body2.position = (WIN_width, WIN_height / 2)
    body3.position = (WIN_width / 2, 0)
    body4.position = (WIN_width / 2, 3000)
    l1 = pymunk.Segment(body3, (-WIN_width / 2, 0), (WIN_width / 2, 0), 5)  # 2
    l2 = pymunk.Segment(body1, (0, -3000), (0, 3000), 5)
    l3 = pymunk.Segment(body2, (0, -3000), (0, 3000), 5)
    l4 = pymunk.Segment(body4, (-WIN_width / 2, 0), (WIN_width / 2, 0), 5)
    l1.elasticity = 1.0
    l2.elasticity = 1.0
    l3.elasticity = 1.0
    l4.elasticity = 1.0

    space.add(l1, l2, l3, l4)  # 3
    return l1, l2, l3, l4


def x_y_scale(balls):
    h = []
    num = []
    for ball in balls:
        y = ball.body.position[1]
        h.append(y)
    max_h = int(max(h) // 10 * 10)
    h = numpy.array(h)
    x = []
    number_piz = 0
    for i in range(0, max_h, 20):
        number = len(h[h <= i])
        num.append(number)
        x.append(i)
    print(number_piz, " number_piz")
    return [x, num, max_h]


def s_d_scale():
    global H
    num = []
    max_h = int(max(H) // 10 * 10)
    h = numpy.array(H)
    x = []
    for i in range(0, max_h, 20):
        number = len(h[h <= i])
        num.append(number)
        x.append(i)
    return [x, num, max_h]


def plt_const(x, y):
    """
    Функция рассчитывает по МНК коэффициенты прямой по полученным координатам точек. Так же рассчитывает их погрешности.
    :param x: Массив абсцисс точек
    :param y: Массив оридинат точек
    :return: [значение углового коэфф a, значение коэфф b, значение погрешности a, значение погрешности b]
    """
    x = numpy.array(x)
    y = numpy.array(y)
    av_x = numpy.sum(x) / len(x)
    av_y = numpy.sum(y) / len(y)
    sigmas_x = numpy.sum(x * x) / len(x) - (numpy.sum(x) / len(x)) ** 2
    sigmas_y = numpy.sum(y * y) / len(y) - (numpy.sum(y) / len(y)) ** 2
    r = numpy.sum(x * y) / len(x) - av_x * av_y
    a = r / sigmas_x
    b = av_y - a * av_x
    return [a, b]


def main():
    global IS_ALIVE, balls
    pygame.init()
    screen = pygame.display.set_mode((WIN_width, WIN_height))
    pygame.display.set_caption("Joints. Just wait and the L will tip over")
    clock = pygame.time.Clock()

    space = pymunk.Space()
    space.gravity = (0.0, -20.0)

    lines = add_static_L(space)
    n = 20 * 20
    balls = []
    draw_options = pymunk.pygame_util.DrawOptions(screen)
    add_balls(space, balls)
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit(0)
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                sys.exit(0)
            if event.type == KEYDOWN and event.key == K_b:
                IS_ALIVE = False
                x = x_y_scale(balls)[0]
                y = x_y_scale(balls)[1]
                print(x)
                print(y)
                plt.plot(x, y, 'o', label='Гиббс')
                s = s_d_scale()[0]
                d = s_d_scale()[1]
                print(s)
                print(d)
                plt.plot(s, d, 'o', label='Больцман')
                plt.grid(True)
                plt.legend()
                plt.show()
                y1 = []
                x1 = list(x)
                t = 0
                for i in range(1, len(y)):
                    if y[i] - y[i - 1] != 0 and y[i] - y[i - 1] != 0.0:
                        y1.append(y[i] - y[i - 1])
                    else:
                        del (x1[i - t])
                        t += 1
                del (x1[0])
                plt.plot(x1, y1, 'o', label='Гиббс')
                d1 = []
                s1 = list(s)
                t = 0
                for i in range(1, len(d)):
                    if d[i] - d[i - 1] != 0 and d[i] - d[i - 1] != 0.0:
                        d1.append(d[i] - d[i - 1])
                    else:
                        del (s1[i - t])
                        t += 1
                del (s1[0])
                plt.plot(s1, d1, 'o', label='Больцман')
                plt.grid(True)
                plt.legend()
                plt.show()
                v = numpy.array(x1)
                ro = numpy.array(y1)
                y1 = numpy.log(ro)
                x1 = v
                r = plt_const(x1, y1)
                a = r[0]
                b = r[1]
                plt.plot(x1, y1, 'o', x1, a * x1 + b, label='Гиббс')
                s1 = numpy.array(s1)
                d1 = numpy.array(d1)
                d1 = numpy.log(d1 )
                s1 = s1
                r = plt_const(s1, d1)
                a1 = r[0]
                b1 = r[1]
                plt.plot(s1, d1, 'o', s1, a1 * s1 + b1, label='Больцман')
                plt.grid(True)
                plt.legend()
                plt.show()
                IS_ALIVE = True
            if event.type == KEYDOWN and event.key == K_1:
                IS_ALIVE = False
                x = x_y_scale(balls)[0]
                y = x_y_scale(balls)[1]
                plt.plot(x, y, 'o', label='Гиббс')
                plt.grid(True)
                plt.legend()
                plt.show()
                y1 = []
                x1 = list(x)
                t = 0
                for i in range(1, len(y)):
                    if y[i] - y[i - 1] != 0 and y[i] - y[i - 1] != 0.0:
                        y1.append(y[i] - y[i - 1])
                    else:
                        del (x1[i - t])
                        t += 1
                del (x1[0])
                plt.plot(x1, y1, 'o', label='Гиббс')
                plt.grid(True)
                plt.legend()
                plt.show()
                v = numpy.array(x1)
                ro = numpy.array(y1)
                y1 = numpy.log(ro)
                x1 = v
                r = plt_const(x1, y1)
                a = r[0]
                b = r[1]
                plt.plot(x1, y1, 'o', x1, a * x1 + b, label='Гиббс')
                plt.grid(True)
                plt.legend()
                plt.show()
                IS_ALIVE = True
            if event.type == KEYDOWN and event.key == K_2:
                IS_ALIVE = False
                s = s_d_scale()[0]
                d = s_d_scale()[1]
                plt.plot(s, d, 'o', label='Больцман')
                plt.grid(True)
                plt.legend()
                plt.show()
                d1 = []
                s1 = list(s)
                t = 0
                for i in range(1, len(d)):
                    if d[i] - d[i - 1] != 0 and d[i] - d[i - 1] != 0.0:
                        d1.append(d[i] - d[i - 1])
                    else:
                        del (s1[i - t])
                        t += 1
                del (s1[0])
                plt.plot(s1, d1, 'o', label='Больцман')
                plt.grid(True)
                plt.legend()
                plt.show()
                s1 = numpy.array(s1)
                d1 = numpy.array(d1)
                d1 = numpy.log(d1)
                s1 = s1
                r = plt_const(s1, d1)
                a1 = r[0]
                b1 = r[1]
                plt.plot(s1, d1, 'o', s1, a1 * s1 + b1, label='Больцман')
                plt.grid(True)
                plt.legend()
                plt.show()
                IS_ALIVE = True
        for i in range(0, len(balls)):
            y1 = balls[i].body.position[1]
            x1 = balls[i].body.position[0]
            if (x1 > WIN_width + 10) or (x1 < -10) or (y1 > 3000) or (y1 < -10):
                ball_shape = add_ball(space, random.randint(50, WIN_width - 50), 800 - random.expovariate(1 / 400))
                balls[i] = ball_shape
        space.step(1 / 50.0)
        screen.fill((255, 255, 255))
        space.debug_draw(draw_options)

        pygame.display.flip()
        clock.tick(50)


def plot_starter():
    global V, balls
    t = 0
    while thread1.is_alive():
        if IS_ALIVE:
            t += 1
            print(t)
            if len(balls) > 2:
                y = balls[1].body.position[1]
                H.append(y)
            pylab.pause(1)


if __name__ == '__main__':
    thread1 = Thread(target=main)
    thread2 = Thread(target=plot_starter)

    thread1.start()
    thread2.start()
