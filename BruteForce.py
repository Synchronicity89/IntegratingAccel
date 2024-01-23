import numpy as np

# Constants
G = 6.674 * (10**-11)  # Gravitational constant in m^3/kg/s^2
M_sun = 1.989 * (10**30)  # Mass of the Sun in kg
d_miles = 10 * (10**9)  # Distance in miles
d_meters = d_miles * 1609.34  # Convert distance to meters
dt = 1000  # Time step in seconds, adjust for accuracy

# Initialize variables
distance = d_meters  # Initial distance from the Sun
velocity = 0  # Initial velocity
time = 0  # Initial time

# Simulation loop
while distance > 0:
    # Update the acceleration due to gravity
    acceleration = G * M_sun / distance**2

    # Update velocity and distance
    velocity += acceleration * dt
    distance -= velocity * dt

    # Update time
    time += dt

    # Optional: Print intermediate results (can be commented out for speed)
    # print(f"Time: {time} seconds, Distance: {distance} meters, Velocity: {velocity} m/s")

# Final time in days
time_days = time / (24 * 3600)
print(f"Time to fall into the Sun: {time_days:.2f} days")
