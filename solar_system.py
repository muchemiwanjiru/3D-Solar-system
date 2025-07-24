from vpython import *

# Set the scene
scene.title = "3D Solar System"
scene.background = color.black

# Create the Sun
sun = sphere(pos=vector(0,0,0), radius=0.5, color=color.orange, emissive=True)

# Create a planet (Earth)
earth = sphere(pos=vector(1,0,0), radius=0.1, color=color.blue, make_trail=True)
earth.orbit_radius = 1
earth.orbit_speed = 0.02
earth.angle = 0

# Create another planet (Mars)
mars = sphere(pos=vector(1.5,0,0), radius=0.08, color=color.red, make_trail=True)
mars.orbit_radius = 1.5
mars.orbit_speed = 0.01
mars.angle = 0

# Animation loop
while True:
    rate(100)  # Controls the speed

    # Update Earth position
    earth.angle += earth.orbit_speed
    earth.pos = vector(earth.orbit_radius * cos(earth.angle), 0, earth.orbit_radius * sin(earth.angle))

    # Update Mars position
    mars.angle += mars.orbit_speed
    mars.pos = vector(mars.orbit_radius * cos(mars.angle), 0, mars.orbit_radius * sin(mars.angle))
