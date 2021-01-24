# Solar System Simulation Project
 
This project was created to simulate the N-body problem. The program plots the Earth in the center, the Moon to the right, and a small satellite orbiting the Moon. The program keeps the Earth in focus and plots the path taken as the Moon and satellite orbit the Earth.

![N-Body Problem Simulation Screenshot](https://github.com/BrandonBNguyen/SolarSystemSimulation/blob/main/screenshots/showcase.PNG)

## Theory

For each time step and each object in the simulation, the net gravitational force due to the other objects in the system is calculated. This is used to find each object's acceleration which can be used to find its position in the following time step.

![Net force due to gravity equation](https://latex.codecogs.com/gif.latex?%5Clarge%20%5Cleft%28%20%5Cvec%7BF_%7B%5Ctext%7Bnet%7D%7D%7D%5Cright%29_i%20%3D%20%5Csum_%7B%5Csubstack%7Bj%3D1%5C%5Cj%5Cneq%20i%7D%7D%5En%20%5Cfrac%7BGm_im_j%7D%7B%7C%7C%5Cvec%7Br%7D_j-%5Cvec%7Br%7D_i%7C%7C%5E2%7D%20%5Cfrac%7B%5Cvec%7Br%7D_j-%5Cvec%7Br%7D_i%7D%7B%7C%7C%5Cvec%7Br%7D_j-%5Cvec%7Br%7D_i%7C%7C%7D%20%3D%5Csum_%7B%5Csubstack%7Bj%3D1%5C%5Cj%5Cneq%20i%7D%7D%5En%20%5Cfrac%7BGm_im_j%7D%7B%7C%7C%5Cvec%7Br%7D_j-%5Cvec%7Br%7D_i%7C%7C%5E3%7D%20%5Cleft%28%5Cvec%7Br%7D_j-%5Cvec%7Br%7D_i%20%5Cright%20%29)

## Implementation

## Skills Demonstrated

