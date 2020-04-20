## Linear_Systems_Reduction  [![forthebadge](https://forthebadge.com/images/badges/makes-people-smile.svg)](https://forthebadge.com)
A gentle intro to reduction of linear systems block diagrams using series, parallel and feedback configuration

##### Why Python?
The guide of this lab uses MATLAB. However,compared to MATLAB python is a lot easier to get, setup, and requires minimal system resources.
This makes it very convenient for any of us eager to see the control commands at work and not spend much wondering how to get started.


## Setup
If you encounter any issue or unclarity during this setup, don't hesitate to reach out to [@mugoh](https://github.com/hogum)

### Package
This part assumes you are unfamiliar with git and [pip](https://pypi.org/project/pip/). If that's not you, go straight ahead to **Minimal Setup**.
1. Get a clone zipped-copy of this repo by clicking [here](https://github.com/hogum/Linear_Systems_Reduction/archive/master.zip)
2. Extract the zip file and move the file to Downloads. This is important. We will be using the downloads folder.

### Windows Platform

#### Dependencies
1. You will need python3 installed. [Click here to install python3](https://www.python.org/ftp/python/3.7.3/python-3.7.3-amd64.exe)
- Ensure to check the box **`Add python to path`** on the first installation window.
- Open a command prompt window and checkout the Downloads folder using the command below
```shell
    cd Downloads
```
2. Install the package manager
  
  [ Deprecated ] Skip this step(By default installing python installs `pip` for you).
- Download get-pip from [here](https://bootstrap.pypa.io/get-pip.py). Save the file to Downloads.

- Install pip (Ensure to have installed python first)
```shell
    python get-pip.py
```
3. Navigate to the cloned repo
```shell
    cd Linear_Systems_Reduction
```
4. Install the project dependencies
```shell
    pip install -r requirements.txt
```

#### Minimal Setup
_Done the Windows Platform part? Skip this_
1. Access a clone copy of the repo
```shell
    git clone git@github.com:hogum/Linear_Systems_Reduction.git
```
2. Navigate to the project directory
```shell
    cd Linear_Systems_Reduction
 ```
 3. Install the project dependencies
```shell
    pip install -r requirements.txt
```

## Usage
The LAB has five examples and exercises
1. Running the [examples](https://github.com/hogum/Linear_Systems_Reduction/tree/master/linearSystems/examples)
- To run an example, pass the name of that example as an argument as shown below


Example No. | How to run | Block Activity
--- | --- | ---
Example 1 | python run.py example1 | Series
Example 2 | python run.py example2 | Parallel
Example 3 | python run.py example3 | Unity Feedback
Example 4 | python run.py example4 | Non-Unity Feedback
Example 5 | python run.py example5 | Zeros and Poles

### Sample Result
Feedback example ouput

![alt text](https://github.com/hogum/Linear_Systems_Reduction/blob/master/linearSystems/examples/data/tf.jpeg)



Poles and Zeros

![alt text](https://github.com/hogum/Linear_Systems_Reduction/blob/master/linearSystems/examples/data/poles_zrs.png)

2. Running Exercises


Exercise No. | How to run 
--- | ---
Exercise 1 | python run.py exercise1 
Exercise 2 | python run.py exercise2
Exercise 3 | python run.py exercise3
Exercise 4 | python run.py exercise4 



---

# Running the Examples section
- Find all the examples in [this directory](https://github.com/hogum/Linear_Systems_Reduction/tree/master/linearSystems/examples)

## Obective
The objective of this exercise will be to learn commands in MATLAB that would be used to reduce linear systems block diagram using series, parallel and feedback configuration.

### Example 1: Series Configuration

Given the transfer functions of individual blocks generate the system transfer
function of the block combinations.

![alt text](https://github.com/hogum/Linear_Systems_Reduction/blob/master/linearSystems/examples/data/example1.jpg)

### Example 2: Parallel Configuration
If the two blocks are connected as shown below then the blocks are said to be in parallel. It would like adding two transfer functions.

![alt text](https://github.com/hogum/Linear_Systems_Reduction/blob/master/linearSystems/examples/data/example2.jpg)


### Example 3: Feedback
Given a unity feedback system as shown in the figure, obtain the overall transfer function.

![alt text](https://github.com/hogum/Linear_Systems_Reduction/blob/master/linearSystems/examples/data/example3.jpg)

### Example 4: FeedBack Non-Unity
Given a non-unity feedback system as shown in the figure, obtain the overall transfer function.

![alt text](https://github.com/hogum/Linear_Systems_Reduction/blob/master/linearSystems/examples/data/example4.jpg)

### Example 5: Zeros and Poles
Given a system transfer function plot the location of the system zeros and poles

![alt text](https://github.com/hogum/Linear_Systems_Reduction/blob/master/linearSystems/examples/data/example5.jpg)


---


# Solutions to the exercises
- Find the solutions to the exercises in [this directory](https://github.com/hogum/Linear_Systems_Reduction/tree/master/linearSystems/exercises). 

##### Exercise 1: 
For the following multi-loop feedback system, get closed loop transfer function and the corresponding pole-zero map of the system.


##### Exercise 2: Consider the feedback system depicted in the figure below 
    a. Compute the closed-loop transfer function using the ‘series’ and ‘feedback’ functions 
    b. Obtain the closed-loop system unit step response with the ‘step’ function and verify that final value of the output is 2/5.


##### Exercise  3:  A  satellite  single-axis  altitude  control  system  can  be  represented  by  the block diagram in the figure given. The variables ‘k’, ‘a’ and ‘b’ are controller parameters, and ‘J’ is the spacecraft moment of inertia. Suppose the nominal moment of inertia is ‘J’ = 10.8E8, and the controller parameters are k=10.8E8, a=1, and b=8.

    a. Develop an m-file script to compute the closed-loop transfer function  
    b. Compute and plot the step response to a 10o step input. 
    c. The exact moment of inertia is generally unknown and may change slowly with time. Compare the step response performance of the spacecraft when J is reduced by 20% and 50%. Discuss your results.




