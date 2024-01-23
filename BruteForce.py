# Re-running the simulation with the same parameters as before due to an execution state reset

# Constants
G = 6.67430e-11  # Gravitational constant in m^3/kg/s^2
M_sun = 1.989e30  # Mass of the Sun in kg
distance_miles = 10e9  # Distance in miles
distance = distance_miles * 1609.34  # Convert distance to meters

# Time step for each iteration (in seconds)
time_step = 100000 # Adjust this as needed for accuracy

# Initialize variables
position = distance  # Initial position
velocity = 0  # Initial velocity
time_elapsed = 0

# Loop until the asteroid reaches the Sun
while position > 0:
    # Calculate the acceleration due to gravity at the current position
    acceleration = G * M_sun / position**2
    
    # Update the velocity (v = u + at)
    velocity += acceleration * time_step
    
    # Update the position (s = ut + 0.5at^2)
    position -= (velocity * time_step + 0.5 * acceleration * time_step**2)
    
    # Update the time
    time_elapsed += time_step

    # Break if the position is less than or equal to zero (asteroid reaches the Sun)
    if position <= 0:
        break

# Output the total time in seconds and convert to days
time_in_days = time_elapsed / (60 * 60 * 24)
print("time in days:", time_in_days)
