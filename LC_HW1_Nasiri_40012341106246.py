import numpy as np
import matplotlib.pyplot as plt

dt = 0.01           
t_max = 5            
t = np.arange(0, t_max, dt)


M_alpha = -8.790     
M_q = -2.075        
M_deltaE = -11.87    


deltaE_list = [-5*np.pi/180, 0, 10*np.pi/180]
labels = ["δE = -5°", "δE = 0°", "δE = +10°"]

for deltaE, label in zip(deltaE_list, labels):
    theta = np.zeros_like(t)       
    theta_dot = np.zeros_like(t)   

    for i in range(1, len(t)):
        theta_ddot = M_alpha * theta[i-1] + M_q * theta_dot[i-1] + M_deltaE * deltaE
        theta_dot[i] = theta_dot[i-1] + theta_ddot * dt
        theta[i] = theta[i-1] + theta_dot[i] * dt

    plt.plot(t, theta * 180/np.pi, label=label)  

plt.title("Pitch Angle Change with Elevator Inputs")
plt.xlabel("Time (seconds)")
plt.ylabel("Pitch Angle θ (degrees)")
plt.grid(True)
plt.legend()
plt.show()
