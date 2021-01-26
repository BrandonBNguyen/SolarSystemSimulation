# Solar System Simulation Project
 
This project was created to simulate the N-body problem. The program plots the Earth in the center, the Moon to the right, and a small satellite orbiting the Moon. The program keeps the Earth in focus and plots the path taken as the Moon and satellite orbit the Earth.

![N-Body Problem Simulation Screenshot](https://github.com/BrandonBNguyen/SolarSystemSimulation/blob/main/screenshots/showcase.PNG)

## Theory

For each time step and each object in the simulation, the net gravitational force due to the other objects in the system is calculated.

![Net force due to gravity equation](https://latex.codecogs.com/gif.latex?%5Clarge%20%5Cleft%28%20%5Cvec%7BF_%7B%5Ctext%7Bnet%7D%7D%7D%5Cright%29_i%20%3D%20%5Csum_%7B%5Csubstack%7Bj%3D1%5C%5Cj%5Cneq%20i%7D%7D%5En%20%5Cfrac%7BGm_im_j%7D%7B%7C%7C%5Cvec%7Br%7D_j-%5Cvec%7Br%7D_i%7C%7C%5E2%7D%20%5Cfrac%7B%5Cvec%7Br%7D_j-%5Cvec%7Br%7D_i%7D%7B%7C%7C%5Cvec%7Br%7D_j-%5Cvec%7Br%7D_i%7C%7C%7D%20%3D%5Csum_%7B%5Csubstack%7Bj%3D1%5C%5Cj%5Cneq%20i%7D%7D%5En%20%5Cfrac%7BGm_im_j%7D%7B%7C%7C%5Cvec%7Br%7D_j-%5Cvec%7Br%7D_i%7C%7C%5E3%7D%20%5Cleft%28%5Cvec%7Br%7D_j-%5Cvec%7Br%7D_i%20%5Cright%20%29)

This is used to find each object's acceleration.

![Net acceleration due to net force](https://latex.codecogs.com/gif.latex?%5CLARGE%20%5Cvec%7Ba%7D_i%20%3D%20%5Cfrac%7B%5Cleft%28%20%5Cvec%7BF_%7B%5Ctext%7Bnet%7D%7D%7D%5Cright%29_i%7D%7Bm_i%7D)

With the acceleration found, the velocity and position of each object in the next time step is found using forward Euler.

![Forward euler algorithm](https://latex.codecogs.com/gif.latex?%5Chuge%20%5Cbegin%7Balign*%7D%20%5Cvec%7Bv%7D%28t_%7Bi&plus;1%7D%29%26%3D%5Cvec%7Ba%7D%28t_%7Bi&plus;1%7D%29%5C%3Bdt%20&plus;%20%5Cvec%7Bv%7D%28t_%7Bi%7D%29%5C%5C%20%5Cvec%7Bx%7D%28t_%7Bi&plus;1%7D%29%26%3D%5Cvec%7Bv%7D%28t_%7Bi&plus;1%7D%29%5C%3Bdt%20&plus;%20%5Cvec%7Bx%7D%28t_%7Bi%7D%29%20%5Cend%7Balign*%7D)

Running this algorithm continuously allows us to predict the motion of a set of bodies over time given initial positions and velocities.

## Implementation

### The Planet Class

```class SolarSystemSimulation.Planet```

The `Planet` class is used to model an object in the solar system and is initialized with a unique name for the object, initial position, initial velocity, mass, radius, and color. Additionally, it can be configured to draw a line representing the path traversed during the simulation. This configuration is on by default.

#### Constructor

```SolarSystemSimulation.Planet.__init__(self, name="Earth", initial_position=[0, 0], initial_velocity=[0, 0], mass=5.972 * pow(10, 24), radius=6356, color="blue", show_path=True):```

 - `name`: A unique identifier for the object. This is used to ensure
   that the program doesn't attempt to calculate the gravitational force
   between this object and itself.
   
 - `initial_position`: A two element list representing the position of
   the object in kilometers. The center of the screen represents the
   origin.
   
 - `initial_velocity`: A two element list representing the velocity of
   the object in kilometers per second.
   
 - `mass`: A positive scalar representing the mass of the object in
   kilograms.
   
 - `radius`: A positive scalar representing the radius of the planet in
   kilometers.
   
 - `color`: The color to be used when plotting the object in the program
   window.
   
 - `show_path`: A boolean that when set to `True` will draw a line
   representing the path traversed by the object.

#### update_position(dt)

```SolarSystemSimulation.Planet.update_position(dt)```

Calculates the net acceleration of the object by referencing the positions of other objects in the solar system and uses that net acceleration along with time step `dt` to calculate the position and velocity for the next time step using forward Euler.

### The SolarSystem Class

```class SolarSystemSimulation.SolarSystem```

The `SolarSystem` class is used to link all the `Planet` objects together, synchronize the updating of positions and velocities, and plot all objects to the program window.

#### Constructor

```SolarSystemSimulation.SolarSystem.__init__(self, planets=[], focus=None, scale=400)```

 - `planets`: A list containing all the `Planet` objects in the solar system.
   
 - `focus`: A single `Planet` object in the solar system for which to center the plot on. This planet will be stationary in the center of the screen and the paths of all other objects around this planet will be plotted.

 - `scale`: An integer representing the number of kilometers per pixel to scale the view of the simulation.

#### update_solar_system(dt)

```SolarSystemSimulation.SolarSystem.update_solar_system(dt)```

Updates the velocities and positions of all `Planet` objects in the solar system using a specified time step of `dt`. 

#### plot_solar_system()

```SolarSystemSimulation.SolarSystem.plot_solar_system()```

Updates the position of each object in the solar system on the program window.

### main.py

`main.py` is used to set up the solar system with the Earth in the center, Moon to the right, and a small satellite to the right of the Moon. The simulation focuses on the Earth, placing it in the center of the window throughout the simulation.

The Earth, Moon, and the small satellite are each modeled as `Planet` objects and placed into a `SolarSystem` object. A loop is then used to continuously call the `update_solar_system()` and `plot_solar_system()` methods to update the positions of the planets over time and display them to the screen. The package `turtle` is used to draw the simulation.

## Skills Demonstrated

 - Demonstrated strong understanding of object-oriented programming and familiarity with Python.
	 - Implemented classes and functions and provided well-written documentation to promote code reusability.
 - Showcased ability to create graphical representations of modeled systems.
 - Successfully implemented numerical methods in code to solve differential equations.
	 - Understanding and implementing forward Euler method.
 - Demonstrated ability to model astrodynamic system and apply fundamental laws of astrodynamics.
