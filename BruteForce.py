import numpy as np

# Constants
G = np.float64(6.67430e-11)  # Gravitational constant in m^3/kg/s^2
M_sun = np.float64(1.989e30)  # Mass of the Sun in kg
distance_miles = np.float64(10e9)  # Distance in miles
distance = distance_miles * np.float64(1609.34)  # Convert distance to meters

# Time step for each iteration (in seconds)
time_step = np.float64(500)  # Adjust this as needed for accuracy

# Initialize variables
position = np.float64(distance)  # Initial position
velocity = np.float64(0)  # Initial velocity
time_elapsed = np.float64(0)

# Loop until the asteroid reaches the Sun
while position > 0:
    # Calculate the acceleration due to gravity at the current position
    acceleration = G * M_sun / np.power(position, 2)
    
    # Update the velocity (v = u + at)
    velocity += acceleration * time_step
    
    # Update the position (s = ut + 0.5at^2)
    position -= (velocity * time_step + 0.5 * acceleration * np.power(time_step, 2))
    
    # Update the time
    time_elapsed += time_step

    # Break if the position is less than or equal to zero (asteroid reaches the Sun)
    if position <= 0:
        break

# Output the total time in seconds and convert to days
time_in_days = time_elapsed / (60 * 60 * 24)
print("Time taken for the asteroid to hit the Sun:", time_in_days, "days")
