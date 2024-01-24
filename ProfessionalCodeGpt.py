import numpy as np

# Constants
G = 6.67430e-11  # Gravitational constant in m^3 kg^-1 s^-2
M = 1.989e+30    # Mass of the Sun in kg
distance = 10e9 * 1.60934e+6  # 10 billion miles to meters
mass_asteroid = 10000 * 1000  # 10,000 tons to kg

# Initial conditions
position = distance
velocity = 0
time = 0
dt = 10000000  # time step in seconds

while position > 0:
    force = G * M * mass_asteroid / position**2
    acceleration = force / mass_asteroid
    velocity += acceleration * dt
    position -= velocity * dt
    time += dt

    if position < 0:
        break

print(f"Time taken to fall into the Sun: {time / (3600 * 24)} days")

# Constants already defined: G, M
# semi_major_axis = distance / 2  # Approximate semi-major axis

# ensure the asteroid is captured by the Sun
perihelion_distance = 0.001 * distance  # Example value, can be adjusted
semi_major_axis = (distance + perihelion_distance) / 2
# Calculating the orbital period using Kepler's third law
orbital_period = np.sqrt((4 * np.pi**2 / (G * M)) * semi_major_axis**3)

print(f"Orbital period: {orbital_period / (3600 * 24)} days")

print("ratio:", orbital_period / time)