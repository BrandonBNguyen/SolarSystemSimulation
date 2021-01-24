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

```class Planet.Planet```

The `Planet` class is used to model an object in the solar system and is initialized with a unique name for the object, initial position, initial velocity, mass, radius, and color. Additionally, it can be configured to draw a line representing the path traversed during the simulation. This configuration is on by default.

``` def __init__(self, name="Earth", initial_position=[0, 0], initial_velocity=[0, 0], mass=5.972 * pow(10, 24),
                 radius=6356, color="blue", show_path=True):```

## Skills Demonstrated

