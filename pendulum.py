class pendulum():
    def __init__(self, mass=1.0, length=1.0, theta=90.0, vel=0.0):
        self.mass = mass
        self.length = length
        self.theta = theta
        self.vel = vel


class double_pendulum():
    def __init__(self, pendulum1=pendulum(), pendulum2=pendulum(), gravity=9.8):
        self.pendulum1 = pendulum1
        self.pendulum2 = pendulum2
        self.gravity = gravity
