import turtle


class Planet:
    def __init__(self, name="Earth", initial_position=[0, 0], initial_velocity=[0, 0], mass=5.972 * pow(10, 24),
                 radius=6356, color="blue", show_path=True):
        self.solar_system = []  # Gives a reference to other orbiting planet.
        self.name = name
        self.mass = mass
        self.G = 6.67430 * pow(10, -20)  # Gravitational constant in km^3 kg^-1 s^-2
        self.radius = radius
        self.color = color
        self.position = initial_position  # Pass in a two entry list containing x and y coordinates in km
        self.velocity = initial_velocity  # Pass in a two entry list containing x and y components of velocity in km/s
        self.show_path = show_path  # Draws a line of it's orbital path if True

        self.planet_turtle = turtle.Turtle()
        self.planet_turtle.speed(0)
        self.planet_turtle.shape('circle')
        self.planet_turtle.color(self.color)
        self.planet_turtle.shapesize(stretch_len=self.radius / 6356, stretch_wid=self.radius / 6356)
        # self.planet_turtle.penup()
        # self.planet_turtle.goto(self.position[0][0]/400, self.position[0][1]/400)
        # if self.show_path:
        #     self.planet_turtle.pendown()

    def __eq__(self, other):
        try:
            return self.name == other.name
        except AttributeError:
            return False

    def update_position(self, dt):
        acceleration = [0, 0]
        for other_planet in self.solar_system.planets:
            if other_planet != self:
                vector = [other_planet.position[0] - self.position[0], other_planet.position[1] - self.position[1]]
                vector_length = pow(pow(vector[0],2) + pow(vector[1],2), 1/2)
                acceleration[0] += self.G * other_planet.mass * vector[0] / pow(vector_length, 3)
                acceleration[1] += self.G * other_planet.mass * vector[1] / pow(vector_length, 3)
        new_velocity = [
            dt * acceleration[0] + self.velocity[0],
            dt * acceleration[1] + self.velocity[1],
        ]
        new_position = [
            dt * self.velocity[0] + self.position[0],
            dt * self.velocity[1] + self.position[1],
        ]
        self.velocity = new_velocity
        self.position = new_position

        # self.planet_turtle.goto(new_position[0]/400, new_position[1]/400)

class SolarSystem:
    def __init__(self, planets=[], focus=None, scale=400):
        self.planets = planets
        if focus == None:
            self.focus_set = False
        else:
            self.focus_set = True
            self.focus = focus
        self.scale = scale # Kilometers per pixel
        for planet in planets:
            planet.solar_system = self
            planet.planet_turtle.penup()
            x = planet.position[0]
            y = planet.position[1]
            if self.focus_set:
                x -= self.focus.position[0]
                y -= self.focus.position[1]
            planet.planet_turtle.goto(x/self.scale, y/self.scale)
            if planet.show_path:
                planet.planet_turtle.pendown()

    def plot_solar_system(self):
        for planet in self.planets:
            if self.focus_set:
                x = (planet.position[0] - self.focus.position[0]) / self.scale
                y = (planet.position[1] - self.focus.position[1]) / self.scale
            else:
                x = planet.position[0] / self.scale
                y = planet.position[1] / self.scale
            planet.planet_turtle.goto(x, y)

    def update_solar_system(self, dt):
        for planet in self.planets:
            planet.update_position(dt)