import pygame
import random
import math
import pylab
from matplotlib import mlab

pygame.init()
WIN_width = 640
WIN_height = 800
screen = pygame.display.set_mode((WIN_width, WIN_height),)  # try out larger values and see what happens !
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
    def __init__(self):
        self.x = random.randint(40, 500)
        self.y = random.randint(40, 400)
        self.radius = 5
        self.color = (255, 255, 255)
        self.vx = random.randint(-3, 3)
        self.vy = -1

    def go(self):
        if self.x + self.radius >= WIN_width or self.x + self.radius <= 20:
            self.vx *= -1
        elif self.y + self.radius >= WIN_height:
            self.vy *= -1
        out_of_range(self)
        ax, ay = 0, 9.81
        dt = 0.05
        delta_x = self.vx * dt + ax * (dt ** 2) / 2
        delta_y = self.vy * dt + ay * (dt ** 2) / 2

        pygame.draw.circle(screen, background_color, (int(self.x), int(self.y)), self.radius)
        self.x += delta_x
        self.y += delta_y
        self.vx += ax * dt
        self.vy += ay * dt
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)

    def click_create(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color


def out_of_range(ball):
    """
    Предотвращение вылета шарика за границы сосуда
    """
    if math.fabs(ball.x) < ball.radius:
        n = (ball.radius - ball.x)/math.fabs(ball.vx)
        ball.x += (n + 0.3)*math.fabs(ball.vx)
    elif (math.fabs(WIN_width - ball.x) < ball.radius) and (math.fabs(WIN_width - ball.x) < ball.vx):
        n = (ball.x - WIN_width - ball.radius)/math.fabs(ball.vx)
        ball.x += (n - 0.3)*math.fabs(ball.vx)

    if (math.fabs(WIN_height - ball.y) < ball.radius) and (math.fabs(WIN_height - ball.y) < ball.vy):
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
            n = r / (math.fabs(v_line_2) + math.fabs(v_line_1))
            if v_line_1 > 0:
                r1 = r1.sum(line.multiplication(n + 0.1))
                ball_1.x, ball_1.y = r1.x, r1.y
            elif v_line_2 > 0:
                r2 = r2.sum(line.multiplication(n))
                ball_2.x, ball_2.y = r2.x, r2.y

        ball_1.vx = v_line_1 * line.x + v_normal_1 * normal.x
        ball_1.vy = v_line_1 * line.y + v_normal_1 * normal.y
        ball_2.vx = v_line_2 * line.x + v_normal_2 * normal.x
        ball_2.vy = v_line_2 * line.y + v_normal_2 * normal.y

Y_scale = []
X_scale = []
X = 0

clock = pygame.time.Clock()
n = 200
sum_v = 0
sr_v = sum_v / n
sum_y = 0
balls = []
k = 0
for i in range(0, n):
    balls.append(Ball())
running = True
while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                balls.append(Ball())
                balls[len(balls) - 1].x = event.pos[0]
                balls[len(balls) - 1].y = event.pos[1]
                balls[len(balls) - 1].color = (255, 0, 0)
                n += 1

    screen.fill(background_color)
    for ball in balls:
        ball.go()
        sum_v += math.sqrt(ball.vx ** 2 + ball.vy ** 2)
        sum_y += WIN_height-ball.y
        if ball.x > WIN_width or ball.x < -20 or ball.y > WIN_height:
            k += 1
    print("Средняя скорость шариков = ", sum_v / (n - k))
    print("Средняя высота шариков = ", sum_y / (n - k))
    print("Число вылетевших = ", k)
    X += 1/60
    Y_scale.append(sum_y / (n - k))
    X_scale.append(X)
    sum_y = 0
    sum_v = 0
    k = 0
    for i in range(0, n):

        for t in range(i, len(balls)):
            if i != t:
                collide(balls[i], balls[t])

    sum_v = 0
    pylab.clf()
    pylab.plot(X_scale, Y_scale)
    pylab.draw()
    pylab.pause(1/60)
    pygame.display.flip()
