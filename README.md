## Linear_Systems_Reduction
A gentle intro to reduction of linear systems block diagrams using series, parallel and feedback configuration

##### Why Python?
The guide of this lab uses MATLAB. However,compared to MATLAB python is a lot easier to get, setup, and requires minimal system resources.
This makes it very convenient for any of us eager to see the control commands at work and not spend much wondering how to get started.


## Setup
If you encounter any issue during setup, or unclarity, reach out to [@mugoh](https://github.com/hogum)

### Package
This part assumes you are unfamiliar with git and [pip](https://pypi.org/project/pip/). If that's not you go straight ahead to [Minimal Setup](https://github.com/hogum/Linear_Systems_Reduction/new/master?readme=1#minimal-setup).
1. Get a clone zipped-copy of this repo by clicking [here](https://github.com/hogum/Linear_Systems_Reduction/archive/master.zip)
2. Extract the zip file and move the fileto Downloads. This is important. We will be using the downloads folder.

### Windows Platform
1. You will need python3 installed. [Click here to install python3](https://www.python.org/ftp/python/3.7.3/python-3.7.3-amd64.exe)

#### Dependencies
1. Install the package manager
- Download get-pip from [here](https://bootstrap.pypa.io/get-pip.py). Save the file to Downloads.
- Open command prompt and checkout the Downloads folder
```shell
    cd Downloads
```
- Install pip (Ensure to have installed python first)
```shell
    python get-pip.py
```
- Navigate to the cloned repo
```shell
    cd Linear_Systems_Reduction
```
 - Install the project dependencies
```shell
    pip install -r requirements.txt
```

#### Minimal Setup
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
The LAB has four examples and exercises
1. Running the examples
- To run an example, pass the name of that example as an argument as shown below


Example No. | How to run | Block Activity
--- | --- | ---
Example 1 | python run.py example1 | Series
Example 2 | python run.py example2 | Parallel
Example 2 | python run.py example3 | Unity Feedback
Example 4 | python run.py example4 | Non-Unity Feedback


### Sample Result
![alt text](https://github.com/hogum/Linear_Systems_Reduction/blob/master/linearSystems/examples/data/tf.jpeg)
