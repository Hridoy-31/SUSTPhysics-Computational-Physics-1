#!/usr/bin/env python3

import drawing
import pygame


def main():

    # default simulation parameter values
    g = 10
    dt = 0.04
    m1 = float(input("Mass 1 : "))
    m2 = 7.0
    t1 = t2 = 0.5
    w1 = w2 = 2.5
    L1 = L2 = 1.0

    # default window dimensions
    cwidth = cheight = 500

    # by default, use the Euler-Lagrange equations to simulate the system
    lagrangian = True

    # in test mode, no window is displayed (only text output is produced)
    test_mode = False

    # initialize the double pendulum
    if lagrangian == True:
        from dp_lagrangian import DoublePendulumLagrangian
        obj = DoublePendulumLagrangian(g, m1, m2, t1, t2, w1, w2, L1, L2)
    else:
        from dp_hamiltonian import DoublePendulumHamiltonian
        obj = DoublePendulumHamiltonian(g, m1, m2, t1, t2, w1, w2, L1, L2)
        
    step = 0

    # maximum energy change (compared to E0): too large => unstable simulation

    # set up the clock and the output window
    if test_mode == False:
        pygame.init()
        clock = pygame.time.Clock()
        canvas = pygame.display.set_mode((cwidth, cheight), pygame.RESIZABLE)
        pygame.display.set_caption("double pendulum")

    # keep running the simulation until the user closes the window
    while True:

        # redraw the double pendulum at a maximum rate of 25 fps
        if test_mode == False:
            drawing.drawing (obj, canvas, cwidth, cheight, dt)
            clock.tick(25)
        # advance one time step
        obj.time_step(dt)
        step += 1


if __name__ == "__main__":
    main()
