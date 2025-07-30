from vpython import sphere, vector, rate, color, label
import math

# Constants
planet_data = [
    {"name": "Mercury", "radius": 0.2, "distance": 4, "color": color.gray(0.5), "speed": 0.02},
    {"name": "Venus",   "radius": 0.3, "distance": 7, "color": color.orange, "speed": 0.015},
    {"name": "Earth",   "radius": 0.35,"distance": 10,"color": color.blue, "speed": 0.012},
    {"name": "Mars",    "radius": 0.3, "distance": 13,"color": color.red, "speed": 0.01},
    {"name": "Jupiter", "radius": 0.7, "distance": 17,"color": color.orange, "speed": 0.008},
    {"name": "Saturn",  "radius": 0.6, "distance": 21,"color": color.yellow, "speed": 0.006},
    {"name": "Uranus",  "radius": 0.5, "distance": 25,"color": color.cyan, "speed": 0.004},
    {"name": "Neptune", "radius": 0.5, "distance": 29,"color": color.blue, "speed": 0.003}
]

# Create the Sun
sun = sphere(pos=vector(0,0,0), radius=1.5, color=color.yellow, emissive=True)

# Create planets
planets = []
angles = []
labels_list = []

for p in planet_data:
    planet = sphere(pos=vector(p["distance"], 0, 0), radius=p["radius"], color=p["color"], make_trail=True)
    name_tag = label(pos=planet.pos, text=p["name"], xoffset=10, yoffset=10, space=30, height=10, border=4, font='sans')
    planets.append(planet)
    angles.append(0)
    labels_list.append(name_tag)

# Animate
while True:
    rate(100)
    for i in range(len(planets)):
        angles[i] += planet_data[i]["speed"]
        x = planet_data[i]["distance"] * math.cos(angles[i])
        y = planet_data[i]["distance"] * math.sin(angles[i])
        planets[i].pos = vector(x, 0, y)
        labels_list[i].pos = planets[i].pos
