class Food:
    def __init__(self, x, y):
        self.init(x, y)

    def init(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        rect(self.x, self.y, 20, 20)

class FoodManage:
    def __init__(self):
        self.count = 5
        self.foods = []
        for i in range(self.count):
            x = floor(random(width / 20)) * 20
            y = floor(random(height / 20)) * 20
            found = False
            for j in range(i):
                if x == self.foods[j].x and y == self.foods[j].y:
                    found = True
                    break;
            if found:
                i -= 1
            else:
                self.foods.append(Food(x, y))

    def update(self):
        for i in range(self.count):
            if self.foods[i].x < 0:
                x = floor(random(width / 20)) * 20
                y = floor(random(height / 20)) * 20
                found = False
                for j in range(self.count):
                    if x == self.foods[j].x and y == self.foods[j].y:
                        found = True
                        break;
                if found:
                    i -= 1
                else:
                    self.foods[i].x = x
                    self.foods[i].y = y

    def draw(self):
        stroke(0)
        noFill()
        for i in range(self.count):
            self.foods[i].draw()


class Snake:
    def __init__(self):
        self.positions = []
        self.positions.append(PVector(0, 0))
        self.vx = 1
        self.vy = 0

    def update(self):
        self.positions.insert(0, PVector(self.positions[0].x + self.vx * 20, self.positions[0].y + self.vy * 20))
        if self.positions[0].x + self.vx * 20 > width or self.positions[0].x + self.vx * 20 < 0 or self.positions[
            0].y + self.vy * 20 > height or self.positions[0].y + self.vy * 20 < 0:
            noLoop()
        del (self.positions[-1])

    def draw(self):
        fill(0)
        noStroke()
        for i in range(len(self.positions)):
            rect(self.positions[i].x, self.positions[i].y, 20, 20)

            def checkHit():
                global snake, foodManag

    for i in range(len(foodManage.foods)):
        if snake.positions[0].x == foodManage.foods[i].x and snake.positions[0].y == foodManage.foods[i].y:
            snake.positions.append(PVector(0, 0))
            foodManage.foods[i].x = -20


def setup():
    global foodManage, snake
    size(800, 600)
    noFill()
    frameRate(3)
    foodManage = FoodManage()
    snake = Snake()


def draw():
    global foodManage
    background(255)
    checkHit()
    foodManage.update()
    foodManage.draw()
    snake.update()
    snake.draw()


def keyPressed():
    global snake
    if key == CODED:
        if keyCode == UP:
            if snake.vy == 1:
                return
            else:
                snake.vx = 0
                snake.vy = -1
        elif keyCode == DOWN:
            if snake.vy == -1:
                return
            else:
                snake.vx = 0
                snake.vy = 1
        elif keyCode == LEFT:
            if snake.vx == 1:
                return
            else:
                snake.vx = -1
                snake.vy = 0
        elif keyCode == RIGHT:
            if snake.vx == -1:
                return
            else:
                snake.vx = 1
                snake.vy = 0