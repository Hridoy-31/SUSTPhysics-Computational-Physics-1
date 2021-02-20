import pickle
import matplotlib.pyplot as plt

t, t1_data, t2_data, x_data_1, x_data_2, y_data_1, y_data_2, K_data, P_data, E_data  = [], [], [], [], [], [], [], [], [], []

def analysis(t, t1_data, t2_data, x_data_1, x_data_2, y_data_1, y_data_2, K_data, P_data, E_data):
    plt.figure()
    plt.title('x data')
    plt.plot(t,x_data_1, 'r', label='First Pendulum')
    plt.plot(t,x_data_2, 'b', label='Second Pendulum')
    plt.xlabel("Time")
    plt.ylabel("x position")
    plt.legend()
    plt.show()
    
    plt.title('y data')
    plt.plot(t,y_data_1, 'r', label='First Pendulum')
    plt.plot(t,y_data_2, 'b', label='Second Pendulum')
    plt.xlabel("Time")
    plt.ylabel("y position")
    plt.legend()
    plt.show()
    
    plt.title('t1 t2 data')
    plt.plot(t1_data,t2_data)
    plt.xlabel('theta 1')
    plt.ylabel('theta 2')
    plt.legend()
    plt.show()

    plt.title("Time vs angle(First Pendulum)")
    plt.plot(t, t1_data, 'r')
    plt.xlabel("Time")
    plt.ylabel("Theta_1")
    plt.legend()
    plt.show()
    
    plt.title("Time vs angle(Second Pendulum)")
    plt.plot(t, t2_data, 'b')
    plt.xlabel("Time")
    plt.ylabel("Theta_2")
    plt.legend()
    plt.show()
    
    plt.plot(t, K_data,'r', label = 'Kinetic Energy')
    plt.plot(t, P_data,'g', label = 'Potential Energy')
    plt.plot(t, E_data, 'black', label = 'Mechanical Energy')
    plt.xlabel('Time')
    plt.ylabel('Energy')
    plt.legend()
    plt.show()
    
    
if __name__ == '__main__':
    with open('filename.pickle', 'rb') as handle:
        b = pickle.load(handle)
        t, t1_data, t2_data, x_data_1, x_data_2, y_data_1, y_data_2, K_data, P_data, E_data= b['t'], b['t1_data'] ,b['t2_data'] ,  b['x_data_1'], b['x_data_2'], b['y_data_1'], b['y_data_2'], b['K_data'], b['P_data'], b['E_data']
    analysis(t, t1_data, t2_data, x_data_1, x_data_2, y_data_1, y_data_2, K_data, P_data, E_data)

    
