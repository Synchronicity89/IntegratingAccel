import rebound
import numpy as np

def simulate_fall_into_sun(distance_in_au, time_step=1e3, max_time=1e10):
    sim = rebound.Simulation()  # Create a new simulation
    sim.units = ('AU', 'yr', 'Msun')  # Set units to Astronomical Units, years, and Solar masses

    sim.add(m=1)  # Add the Sun (mass = 1 in Solar masses)
    sim.add(a=distance_in_au, e=0.99999)  # Add the asteroid with a very high eccentricity

    sim.integrator = 'ias15'  # A high-accuracy integrator, good for handling close encounters

    sim.move_to_com()  # Move to the center of mass frame

    # Integrate the system
    try:
        sim.integrate(max_time, exact_finish_time=0)  # Integrate up to a maximum time
        orbital_period = sim.particles[1].P  # Get the orbital period of the asteroid
        return orbital_period
    except rebound.Escape:
        return "Object Escaped"

# Distance from the Sun in Astronomical Units (1 AU is approximately 149.6 million kilometers)
distance_in_au = 10e9 / 149.6e6

# Simulate
orbital_period = simulate_fall_into_sun(distance_in_au)
print(f"Orbital Period: {orbital_period} years")
