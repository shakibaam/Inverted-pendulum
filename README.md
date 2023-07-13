# Inverted Pendulum Simulator

This project aims to solve the inverted pendulum problem using various controllers such as PID controller and Fuzzy controller.

## Problem Description

The inverted pendulum problem involves keeping a pendulum balanced in an inverted position. The initial state of the problem and the general state can be observed in the figures provided.

The variables of this problem include:
- Pendulum angle with respect to the vertical axis (Θ)
- Pendulum angular velocity (Ω)
- Cart position (cp)
- Cart velocity along the x-axis (cv)

The output of the problem is the force (F) applied to the cart in the x-axis direction.

## Implementation Steps

To implement the fuzzy control system, follow these steps:

1. **Fuzzification**: 
   - Fuzzify the input variables by mapping them to fuzzy sets.
   - Transform the crisp inputs (angle and angular velocity) into linguistic terms using membership functions.

2. **Inference**:
   - Use the predefined rules written in the `fcl.simple/controller` file.
   - Perform appropriate inference based on the fuzzified inputs to determine the fuzzy output.
   - The rules involve terms like Pv (Proportional Velocity) and Pa (Proportional Angle) to guide the inference process.

3. **Defuzzification**:
   - Convert the fuzzy output into a crisp value representing the absolute force.
   - Calculate the absolute force value based on the provided descriptions and guidelines.
   - Consider this value as the output of the `decide` function.


## Getting Started

To run this project, ensure that Python 2.7 is installed on your system. If not, you can download Python 2.7 from the org.python website.

Follow the steps below to set up the project environment:

1. Install `virtualenv` by running the following command:

2. Navigate to the project directory and create a Python 2 virtual environment using the following command:

3. Activate the virtual environment based on your operating system:
- Linux:
  ```
  source venv/bin/activate
  ```
- Windows:
  ```
  .\venv\Scripts\activate
  ```

4. Install the required libraries by executing the following command:

## Usage

To run the simulator, execute the following command:
python main.py

## Results
This is the picture of the result:

![Image 1](https://github.com/shakibaam/Inverted-pendulum/blob/master/result.png)
