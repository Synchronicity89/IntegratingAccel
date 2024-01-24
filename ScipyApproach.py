import numpy as np
from scipy.integrate import quad

# Constants
G = 6.67430e-11  # Gravitational constant in m^3/kg/s^2
M_sun = 1.989e30  # Mass of the Sun in kg
distance_miles = 10e9  # Distance in miles
distance = distance_miles * 1609.34  # Convert distance to meters

# Function to calculate the integrand of the time integral
def integrand(r):
    return np.sqrt(1 / (G * M_sun / r**2))

# Integrating from a small value close to 0 (to avoid division by zero) to the initial distance
epsilon = 1.0  # Small value to avoid division by zero at the lower limit of integration

# Numerical integration using SciPy's quad function for more accuracy
time_seconds, _ = quad(integrand, epsilon, distance)

# Convert time to days
time_days = time_seconds / (60 * 60 * 24)
print("Time taken for the asteroid to hit the Sun:", time_days, "days")
