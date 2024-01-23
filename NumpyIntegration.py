import numpy as np

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
r = np.linspace(epsilon, distance, 10000)  # Array of distances
dr = np.diff(r)  # Differential elements of r
integral_values = integrand(r[:-1])  # Integrand values at each r

# Numerical integration using the trapezoidal rule
time_seconds = np.sum(integral_values * dr)

# Convert time to days
time_days = time_seconds / (60 * 60 * 24)
print("Time taken for the asteroid to hit the Sun:", time_days, "days")
