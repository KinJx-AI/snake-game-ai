import numpy as np
import random as rd

rd.seed(31165087)

SNAKE_BLOCK_LABEL = 1
FOOD_LABEL = 2
UP_LABEL = 0
DOWN_LABEL = 1
LEFT_LABEL = 2
RIGHT_LABEL = 3

GRID_SIZE = 10
FOOD_COUNT = 1
ORIGIN = (GRID_SIZE // 2, GRID_SIZE // 2, UP_LABEL)


class Block:
    def __init__(self, newX, newY):
        self.x = newX
        self.y = newY
        self.prevX = None
        self.prevY = None

    def move(self, newX, newY):
        self.prevX = self.x
        self.prevY = self.y
        self.x = newX
        self.y = newY


class Body(Block):
    def __init__(self, newX, newY, isHead, parent):
        super().__init__(newX, newY)
        self.isHead = isHead
        if not self.isHead:
            self.parent = parent
        else:
            self.parent = None


class Food(Block):
    def __init__(self, newX, newY):
        super().__init__(newX, newY)


class Snake:
    def __init__(self, newX, newY, newDirection):
        self.head = Body(newX, newY, True, None)
        self.direction = newDirection
        self.body = [self.head]

    def add_body(self):
        tail = self.body[-1]
        self.body.append(Body(tail.prevX, tail.prevY, False, tail))

    def change_direction(self, newDirection):
        if self.direction == 0 or self.direction == 1:
            if newDirection != 0 and newDirection != 1:
                self.direction = newDirection

        if self.direction == 2 or self.direction == 3:
            if newDirection != 2 and newDirection != 3:
                self.direction = newDirection

    def move(self):
        # Move head
        if self.direction == UP_LABEL:
            self.head.move(self.head.x - 1, self.head.y)
        elif self.direction == DOWN_LABEL:
            self.head.move(self.head.x + 1, self.head.y)
        elif self.direction == LEFT_LABEL:
            self.head.move(self.head.x, self.head.y - 1)
        elif self.direction == RIGHT_LABEL:
            self.head.move(self.head.x, self.head.y + 1)

        # Move other body blocks
        for bodyBlockIndex in range(1, len(self.body)):
            currentBodyBlock = self.body[bodyBlockIndex]
            parentBodyBlock = currentBodyBlock.parent
            currentBodyBlock.move(parentBodyBlock.prevX, parentBodyBlock.prevY)


class World:
    def __init__(self, size=GRID_SIZE, foodCount=FOOD_COUNT):
        self.size = size
        self.gridWorld = np.zeros((self.size, self.size))

        self.isCollide = False
        self.stepsTaken = 0
        self.score = 0

        self.snake = Snake(*ORIGIN)
        self.foods = []
        for _ in range(foodCount):
            self.spawn_food()

        self.draw_grid()

    def spawn_food(self):
        spawnPositionNotFound = True
        while spawnPositionNotFound:
            spawnPositionNotFound = False
            x = rd.randint(0, self.size - 1)
            y = rd.randint(0, self.size - 1)

            # Check for empty position without body
            for bodyBlock in self.snake.body:
                if bodyBlock.x == x and bodyBlock.y == y:
                    spawnPositionNotFound = True

            # Check for empty position without food
            for food in self.foods:
                if food.x == x and food.y == y:
                    spawnPositionNotFound = True

        self.foods.append(Food(x, y))

    def check_eat_food(self):
        for foodIndex in range(len(self.foods)):
            food = self.foods[foodIndex]
            if self.snake.head.x == food.x and self.snake.head.y == food.y:
                self.foods.pop(foodIndex)
                self.snake.add_body()
                self.spawn_food()
                self.score += 1
                break

    def check_collision(self):
        x = self.snake.head.x
        y = self.snake.head.y

        # Check edge collision
        if x >= self.size or y >= self.size or x < 0 or y < 0:
            self.isCollide = True
            return

        # Check self collision
        for bodyBlock in self.snake.body:
            if not bodyBlock.isHead and bodyBlock.x == x and bodyBlock.y == y:
                self.isCollide = True
                return

    def draw_grid(self):
        self.gridWorld = np.zeros((self.size, self.size))
        for bodyBlock in self.snake.body:
            self.gridWorld[bodyBlock.x][bodyBlock.y] = SNAKE_BLOCK_LABEL
        for food in self.foods:
            self.gridWorld[food.x][food.y] = FOOD_LABEL

    def step(self):
        self.snake.move()
        self.check_eat_food()
        self.check_collision()

        self.stepsTaken += 1

        if not self.isCollide:
            self.draw_grid()
