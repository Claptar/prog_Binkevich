import pygame
import random
import math

pygame.init()
screen = pygame.display.set_mode((640, 480),) # try out larger values and see what happens !
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
        self.x *= constant
        self.y *= constant

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
        self.x = random.randint(100, 400)
        self.y = random.randint(100, 300)
        self.radius = 20
        self.color = (random.randint(0, 255),
                      random.randint(0, 255),
                      random.randint(0, 255))
        self.vx = random.randint(-3, 3)
        self.vy = random.randint(-3, 3)

    def go(self):
        if self.x + self.radius >= 640 or self.x + self.radius <= 50:
            self.vx *= -1
        elif self.y + self.radius >= 480 or self.y + self.radius <= 50:
            self.vy *= -1
        pygame.draw.circle(screen, background_color, (int(self.x), int(self.y)), self.radius)
        self.x += self.vx
        self.y += self.vy
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)


def collide(ball_1, ball_2):
    """
    Рассчёт столкновения двух шариков
    """
    if (ball_1.x - ball_2.x) ** 2 + (ball_1.y - ball_2.y) ** 2 <= (2*ball_1.radius) ** 2:
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
        ball_1.vx = v_line_1 * line.x + v_normal_1 * normal.x
        ball_1.vy = v_line_1 * line.y + v_normal_1 * normal.y
        ball_2.vx = v_line_2 * line.x + v_normal_2 * normal.x
        ball_2.vy = v_line_2 * line.y + v_normal_2 * normal.y



clock = pygame.time.Clock()
n = 6
balls = []
for i in range(0, n):
    balls.append(Ball())
running = True
while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    for ball in balls:
        ball.go()
    for i in range (0, n):
        for t in range (i, n):
            if i != t:
                collide(balls[i], balls[t])
    pygame.display.flip()