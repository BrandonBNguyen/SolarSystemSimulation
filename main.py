import turtle
from Planet import Planet
from Planet import Solar_system

win = turtle.Screen()
win.title("N-Body Problem Simulation")
win.bgcolor("black")
win.setup(width=800, height=800)

Earth = Planet()
Moon = Planet(name="Moon", mass=7.3477 * pow(10, 22), color="gray",
              initial_position=[384400, 0], initial_velocity=[0, 1])
small_satellite = Planet(name="Satellite", mass=1500, color="yellow",
                         initial_position=[410000, 0], initial_velocity=[0, 0.5])
sol = Solar_system(planets=[Earth, Moon, small_satellite], focus=Earth, scale=1200)

dt = 10
running = True
while running:
    win.update()
    loops_per_plot = 300
    t_i = 0
    while t_i < loops_per_plot:
        sol.update_solar_system(dt)
        t_i += 1
    sol.plot_solar_system()
