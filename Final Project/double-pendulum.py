#!/usr/bin/env python3

import drawing
import pygame
import math
import pickle
from analysis import analysis

def main():
    t, x_data_1, x_data_2, y_data_1, y_data_2, t1_data, t2_data, K_data, P_data, E_data  = [], [], [], [], [], [], [], [], [], []
    # default simulation parameter values
    g = 9.8
    dt = 0.025
    #m1 = float(input("Mass 1 : "))
    m1 = 2
    m2 = 2
    t1 = t2 = 0.5
    w1 = w2 = 0
    L1 = L2 = 1.0

    # default window dimensions
    cwidth = cheight = 500

    # by default, use the Euler-Lagrange equations to simulate the system
    lagrangian = False

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
        canvas = pygame.display.set_mode((cwidth, cheight))
        pygame.display.set_caption("double pendulum")

    # keep running the simulation until the user closes the window
    
    index = 0
    while True:
        should_quit = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                should_quit = 1
                
        if should_quit:
            save_data = {'t':t,'t1_data':t1_data,'t2_data':t2_data,'x_data_1':x_data_1,'y_data_1':y_data_1,'x_data_2':x_data_2,'y_data_2':y_data_2, 'K_data':K_data, 'P_data':P_data, 'E_data':E_data}
            with open('filename.pickle', 'wb') as handle:
                pickle.dump(save_data, handle)
            analysis(t, t1_data, t2_data, x_data_1, x_data_2, y_data_1, y_data_2, K_data, P_data, E_data)
            
            pygame.quit()
            break
        # redraw the double pendulum at a maximum rate of 25 fps
        if test_mode == False:
            y1 = -L1 * math.cos(obj.t1)
            y2 = y1 - L2 * math.cos(obj.t2)
            
            x1 = L1 * math.sin(obj.t1)
            x2 = x1 + L2 * math.sin(obj.t2)
            
            
            t.append(index*dt)
            index += 1
            x_data_1.append(x1)
            x_data_2.append(x2)
            y_data_1.append(y1)
            y_data_2.append(y2)
            t1_data.append(obj.t1)
            t2_data.append(obj.t2)
            K_data.append(obj.kinetic_energy())
            P_data.append(obj.potential_energy())
            E_data.append(obj.mechanical_energy())
            
            
            print(x1,x2)
            print(y1, y2)
            print('-----------------')
            # print(,obj.t2)
            
            drawing.drawing (obj, canvas, cwidth, cheight, dt)
            clock.tick(40)
        # advance one time step
        obj.time_step(dt)
        step += 1
    
    


if __name__ == "__main__":
    main()
