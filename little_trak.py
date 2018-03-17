import explorerhat as eh
import time

class Robot():
    def __init__(self):
        self.sequence = []
        self.moving = False

    def left(self):
        eh.motor.one.backwards()
        eh.motor.two.forwards()

    def right(self):
        eh.motor.one.forwards()
        eh.motor.two.backwards()

    def forwards(self):
        eh.motor.forwards()

    def backwards(self):
        eh.motor.backwards()

    def stop(self):
        eh.motor.stop()

    def program(self, channel, event):
        # Function to record presses on capacative touch and store in sequence
        self.sequence.append(channel)
        print(self.sequence)
        if channel == 5:
            self.moving = True

    def move(self):
        # Function to iterate through sequence and move robot in direction
        for i in range(len(self.sequence)):
            #print(self.sequence[i])
            #time.sleep(0.5)
            if self.sequence[i] == 1:
                self.forwards()
            if self.sequence[i] == 2:
                self.backwards()
            if self.sequence[i] == 3:
                self.left()
            if self.sequence[i] == 4:
                self.right()
            if self.sequence[i] == 5:
                self.stop()
            time.sleep(0.5)
        self.moving = False
        self.sequence = []

robot = Robot()

while True:
    if robot.moving == False:
        eh.touch.pressed(robot.program)
       # print(robot.sequence)
    else:
        robot.move()
