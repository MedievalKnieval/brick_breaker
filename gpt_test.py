
import pygame
import sys

WIDTH, HEIGHT = 640, 480

class Paddle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 100
        self.height = 20
        self.velocity = 5

    def draw(self, screen):
        pygame.draw.rect(screen, (0, 0, 255), (self.x, self.y, self.width, self.height))

    def move(self, direction):
        if direction == "left":
            self.x -= self.velocity
        elif direction == "right":
            self.x += self.velocity

        if self.x <= 0:
            self.x = 0
        elif self.x + self.width >= WIDTH:
            self.x = WIDTH - self.width

class Ball:
    def __init__(self, x, y, velocity_x, velocity_y):
        self.x = x
        self.y = y
        self.velocity_x = velocity_x
        self.velocity_y = velocity_y
        self.radius = 10

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 0, 0), (int(self.x), int(self.y)), self.radius)

    def move(self):
        self.x += self.velocity_x
        self.y += self.velocity_y

        if self.x - self.radius <= 0 or self.x + self.radius >= WIDTH:
            self.velocity_x *= -1
        if self.y - self.radius <= 0:
            self.velocity_y *= -1
        elif self.y + self.radius >= HEIGHT:
            pygame.quit()
            sys.exit()

class Brick:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 60
        self.height = 20

    def draw(self, screen):
        pygame.draw.rect(screen, (0, 255, 0), (self.x, self.y, self.width, self.height))

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    ball = Ball(WIDTH // 2, HEIGHT // 2, 5, -5)

    bricks = []
    for i in range(7):
        for j in range(3):
            brick_x = i * 70 + 20
            brick_y = j * 25 + 20
            bricks.append(Brick(brick_x, brick_y))

    paddle = Paddle(WIDTH // 2, HEIGHT - 50)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            paddle.move("left")
        elif keys[pygame.K_RIGHT]:
            paddle.move("right")

        ball.move()

        if ball.y + ball.radius >= paddle.y and ball.x + ball.radius >= paddle.x and ball.x - ball.radius <= paddle.x + paddle.width:
            ball.velocity_y *= -1

        screen.fill((255, 255, 255))

        for brick in bricks:
            brick.draw(screen)

        paddle.draw(screen)
        ball.draw(screen)

        pygame.display.update()
        clock.tick(60)

if __name__ == "__main__":
    main()
