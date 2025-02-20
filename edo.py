import numpy as np
import matplotlib.pyplot as plt

# Physical constants
g = 9.8
L = 15
mu = 0.9

THETA_0 = np.pi / 3  # 60 degrees
THETA_DOT_0 = 0

# Definition of ODE
def get_Theta_double_dot(theta, theta_dot):
    return -mu * theta_dot - (g / L) * np.sin(theta)

# Solution to the differential equation using Euler's method
def theta(t, delta_t=0.01):
    # Initialize changing values
    theta_val = THETA_0
    theta_dot = THETA_DOT_0

    # Time evolution
    for time in np.arange(0, t, delta_t):
        theta_double_dot = get_Theta_double_dot(theta_val, theta_dot)
        theta_val += theta_dot * delta_t
        theta_dot += theta_double_dot * delta_t

    return theta_val

# Plot the evolution over time
time_points = np.arange(0, 10, 0.01)
theta_values = [theta(t) for t in time_points]

plt.plot(time_points, theta_values)
plt.title('Pendulum Angle Over Time (Euler Method)')
plt.xlabel('Time (s)')
plt.ylabel('Theta (rad)')
plt.grid(True)
plt.show()
