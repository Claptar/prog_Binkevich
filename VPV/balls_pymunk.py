import sys, random
import pygame
from pygame.locals import *
import pymunk
import pymunk.pygame_util
import pylab
from threading import Thread
import numpy
import matplotlib.pyplot as plt
import math
import time
import pickle
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
import pandas

WIN_width = 640
WIN_height = 480
IS_ALIVE = True
balls = []
V = []
R = []
R2 = []


def add_ball(space, x, y):
    """Add a ball to the given space at a random position"""
    mass = 1
    radius = 2
    inertia = pymunk.moment_for_circle(mass, 0, radius, (0,0))
    body = pymunk.Body(mass, inertia)
    body.position = x, y
    shape = pymunk.Circle(body, radius, (0, 0))
    space.add(body, shape)
    shape.elasticity = 1.0
    return shape


def add_balls(space, balls):
    global WIN_width, WIN_height
    k = 40
    m = 40
    for j in range(1, k):
        for i in range(1, m):
            if len(balls) == 1:
                ball_shape = add_ball(space, WIN_width / 2, WIN_height / 2)
                balls.append(ball_shape)
                vx = random.randint(-200, 200)
                vy = random.randint(-200, 200)
                balls[len(balls) -1].body._set_velocity((vx, vy))

            else:
                ball_shape = add_ball(space, 20 + 10 * i, 20 + 10 * j)
                balls.append(ball_shape)
                vx = random.randint(-200, 200)
                vy = random.randint(-200, 200)
                balls[len(balls) -1].body._set_velocity((vx, vy))
        
        
def add_static_L(space):
    body1 = pymunk.Body(body_type = pymunk.Body.STATIC) # 1
    body2 = pymunk.Body(body_type=pymunk.Body.STATIC)  # 1
    body3 = pymunk.Body(body_type=pymunk.Body.STATIC) # 1
    body4 = pymunk.Body(body_type=pymunk.Body.STATIC)
    body1.position = (0, WIN_height/2)
    body2.position = (WIN_width, WIN_height/2)
    body3.position = (WIN_width/2, 0)
    body4.position = (WIN_width / 2, WIN_height)
    l1 = pymunk.Segment(body3, (-WIN_width/2, -200), (WIN_width/2, -200), 200) # 2
    l2 = pymunk.Segment(body1, (-200, -WIN_height/2), (-200, 2000), 200)
    l3 = pymunk.Segment(body2, (200, -WIN_width/2), (200, 2000), 200)
    l4 = pymunk.Segment(body4, (-WIN_width / 2, 200), (WIN_width / 2, 200), 200)
    l1.elasticity = 1.0
    l2.elasticity = 1.0
    l3.elasticity = 1.0
    l4.elasticity = 1.0

    space.add(l1, l2, l3, l4) # 3
    return l1, l2, l3, l4


def x_y_scale(balls):
    v = []
    num = []
    for ball in balls:
        vx = ball.body._get_velocity()[0]
        vy = ball.body._get_velocity()[1]
        v.append(math.sqrt(vx**2 + vy**2))
    max_v = int(max(v) // 10 * 10)
    v = numpy.array(v)
    x = []
    for i in range(0, 350, 10):
        number = len(v[v <= i])/1600
        num.append(number)
        x.append(i)
    return [x, num, max_v]


def s_d_scale():
    global V
    num = []
    max_v = int(max(V) // 10 * 10)
    v = numpy.array(V)
    x = []
    for i in range(0, 350, 10):
        number = len(v[v <= i])/len(V)
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


def main():
    global IS_ALIVE, balls
    pygame.init()
    screen = pygame.display.set_mode((WIN_width, WIN_height))
    pygame.display.set_caption("Joints. Just wait and the L will tip over")
    clock = pygame.time.Clock()

    space = pymunk.Space()

    lines = add_static_L(space)
    n = 15*18
    balls = []
    draw_options = pymunk.pygame_util.DrawOptions(screen)
    add_balls(space, balls)
    p = 0
    t = 0
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit(0)
            elif event.type == KEYDOWN and event.key == K_s:
                with open("copy_and_pickle.pickle", "wb") as f:
                    pickle.dump(space, f)
            elif event.type == KEYDOWN and event.key == K_l:
                with open("copy_and_pickle.pickle", "rb") as f:
                    space = pickle.load(f)
                    shapes = space._get_shapes()
                    for i in range(0, len(shapes) - 4):
                        balls[i] = shapes[i + 4]
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                sys.exit(0)
            elif event.type == KEYDOWN and event.key == K_m:
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
                        del(x1[i - t])
                        t += 1
                del(x1[0])
                plt.plot(x1, y1, 'o', label='Гиббс')
                d1 = []
                s1 = list(s)
                t = 0
                for i in range(1, len(d)):
                    if d[i] - d[i - 1] != 0 and d[i] - d[i - 1] != 0.0:
                        d1.append(d[i] - d[i - 1])
                    else:
                        del(s1[i - t])
                        t += 1
                del(s1[0])
                df = pandas.DataFrame({'x1': x1,
                                       'y1': y1})

                writer = ExcelWriter('rhogb1.xlsx')
                df.to_excel(writer, 'Sheet1', index=False)
                writer.save()
                df = pandas.DataFrame({'s1': s1,
                                       'd1': d1})

                writer = ExcelWriter('rhogb3.xlsx')
                df.to_excel(writer, 'Sheet1', index=False)
                writer.save()
                plt.plot(s1, d1, 'o', label='Больцман')
                plt.grid(True)
                plt.legend()
                plt.show()
                v = numpy.array(x1)
                ro = numpy.array(y1)
                y1 = numpy.log(ro/v)
                x1 = v*v
                r = plt_const(x1, y1)
                a = r[0]
                b = r[1]
                plt.plot(x1, y1, 'o', x1, a * x1 + b, label='Гиббс')
                s1 = numpy.array(s1)
                d1 = numpy.array(d1)
                d1 = numpy.log(d1 / s1)
                s1 = s1*s1
                r = plt_const(s1, d1)
                a1 = r[0]
                b1 = r[1]
                df = pandas.DataFrame({'x1': x1,
                                       'y1': y1})
                writer = ExcelWriter('rhogb2.xlsx')

                df.to_excel(writer, 'Sheet2', index=False)
                writer.save()
                df = pandas.DataFrame({'s1': s1,
                                       'd1': d1})

                writer = ExcelWriter('rhogb4.xlsx')
                df.to_excel(writer, 'Sheet1', index=False)
                writer.save()
                plt.plot(s1, d1, 'o', s1, a1 * s1 + b1, label='Больцман')

                plt.grid(True)
                plt.legend()
                plt.show()
                k = [a, b, a1, b1]
                print("a = ", a, "b = ", b, "a1 = ", a1, "b1 = ", b1)
                with open("файл.txt", "w") as file:
                    print(*k, file=file)
                IS_ALIVE = True
            elif event.type == KEYDOWN and event.key == K_1:
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
                y1 = numpy.log(ro / v)
                x1 = v * v
                r = plt_const(x1, y1)
                a = r[0]
                b = r[1]
                plt.plot(x1, y1, 'o', x1, a * x1 + b, label='Гиббс')
                plt.grid(True)
                plt.legend()
                plt.show()
                print("a = ", a, "b = ", b)
                IS_ALIVE = True
            elif event.type == KEYDOWN and event.key == K_2:
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
                d1 = numpy.log(d1 / s1)
                s1 = s1 * s1
                r = plt_const(s1, d1)
                a1 = r[0]
                b1 = r[1]
                plt.plot(s1, d1, 'o', s1, a1 * s1 + b1, label='Больцман')
                plt.grid(True)
                plt.legend()
                plt.show()
                print("a1 = ", a1, "b1 = ", b1)
                IS_ALIVE = True
        space.step(1/50.0)
        screen.fill((255, 255, 255))
        space.debug_draw(draw_options)

        pygame.display.flip()
        print('P = ', p)
        print(time.clock())
        clock.tick(50)


def plot_starter():
    global V, balls
    t = 0
    while thread1.is_alive():
        if IS_ALIVE:
            if len(balls) > 2:
                t += 1
                vx = balls[1].body._get_velocity()[0]
                vy = balls[1].body._get_velocity()[1]
                V.append(math.sqrt(vx ** 2 + vy ** 2))
            pylab.pause(1/4)


def plot_starter2():
    global V, balls
    t = 0
    time = []
    x0 = 0
    y0 = 0
    while thread1.is_alive():
        if IS_ALIVE:
            if len(balls) > 2:
                time.append(t)
                t += 1
                if t == 1:
                    x0 = balls[1].body.position[0]
                    y0 = balls[1].body.position[1]
                r = (x0 - balls[1].body.position[0]) ** 2 + (y0 - balls[1].body.position[1]) ** 2
                R2.append(r)
                R_np = numpy.array(R2)
                av_r = numpy.average(R2)
                R.append(av_r)
                pylab.clf()
                r = plt_const(time, R)
                a = r[0]
                b = r[1]
                plt.plot(time, R, 'o', time, a * numpy.array(time) + b)
                pylab.grid(True)
                pylab.draw()
            pylab.pause(1/4)


if __name__ == '__main__':
    thread1 = Thread(target=main)
    thread2 = Thread(target=plot_starter)
    thread3 = Thread(target=plot_starter2)

    thread1.start()
    thread2.start()
