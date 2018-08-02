import numpy as np

import pendulum


def rk4(double_pendulum):
    dt = 0.02
    condition = np.array([double_pendulum.pendulum1.theta,
                          double_pendulum.pendulum2.theta,
                          double_pendulum.pendulum1.vel,
                          double_pendulum.pendulum2.vel])
    k1 = function(condition, double_pendulum) * dt
    k2 = function(condition + k1/2, double_pendulum) * dt
    k3 = function(condition + k2/2, double_pendulum) * dt
    k4 = function(condition + k3, double_pendulum) * dt
    condition += (k1 + 2*k2 + 2*k3 + k4)/6
    return pendulum.double_pendulum(pendulum.pendulum(double_pendulum.pendulum1.mass,
                                                      double_pendulum.pendulum1.length,
                                                      condition[0],
                                                      condition[2]),
                                    pendulum.pendulum(double_pendulum.pendulum2.mass,
                                                      double_pendulum.pendulum2.length,
                                                      condition[1],
                                                      condition[3]),
                                    double_pendulum.gravity)


def function(vector, double_pendulum):
    m1 = double_pendulum.pendulum1.mass
    m2 = double_pendulum.pendulum2.mass
    l1 = double_pendulum.pendulum1.length
    l2 = double_pendulum.pendulum2.length
    g = double_pendulum.gravity

    dtheta1 = vector[2]

    dtheta2 = vector[3]

    p1 = -m2*l1*np.sin(2*vector[0]-2*vector[1])*pow(vector[2], 2)/2
    p2 = -m2*l2*np.sin(vector[0]-vector[1])*pow(vector[3], 2)
    p3 = m2*g*np.sin(vector[1])*np.cos(vector[0]-vector[1])
    p4 = -(m1+m2)*g*np.sin(vector[0])
    p5 = l1*(m1+m2*pow(np.sin(vector[0]-vector[1]), 2))
    dvel1 = (p1+p2+p3+p4)/p5

    q1 = (m1+m2)*l1*np.sin(vector[0]-vector[1])*pow(vector[2], 2)
    q2 = m2*l2*np.sin(2*vector[0]-2*vector[1])*pow(vector[3], 2)/2
    q3 = (m1+m2)*g*np.sin(vector[0])*np.cos(vector[0]-vector[1])
    q4 = -(m1+m2)*g*np.sin(vector[1])
    q5 = l2*(m1+m2*pow(np.sin(vector[0]-vector[1]), 2))
    dvel2 = (q1+q2+q3+q4)/q5

    vector = np.array([dtheta1, dtheta2, dvel1, dvel2])
    return vector
