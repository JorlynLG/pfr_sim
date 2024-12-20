# About The Project
This package provides a simulation for the Precision Farming Rover. 

![image](https://github.com/user-attachments/assets/d7899369-1be4-4131-be92-5ce1d5d1cf89)


## Requirements

#### Install correct ubuntu, ROS2, and gazebo versions

To run this package, you'll need the following:

- [Linux Ubuntu 24.04](https://ubuntu.com/blog/tag/ubuntu-24-04-lts)
- [ROS2 Jazzy Jalisco](https://docs.ros.org/en/rolling/Releases/Release-Jazzy-Jalisco.html)
- [Gazebo Harmonic](https://gazebosim.org/docs/harmonic/getstarted/) [(easy to install it directly with ROS2 for the correct compatibility)](https://gazebosim.org/docs/latest/ros_installation/)


#### Install required ROS2 packages

Make sure to install the following ROS 2 Jazzy Jalisco packages:

```bash
sudo apt install -y                         \
    ros-jazzy-ros2-controllers              \
    ros-jazzy-ros-gz                        \
    ros-jazzy-ros-gz-bridge                 \
    ros-jazzy-joint-state-publisher         \
    ros-jazzy-xacro                         \
    ros-jazzy-teleop-twist-keyboard         \
    ros-jazzy-teleop-twist-joy              \
    ros-jazzy-joint-state-publisher-gui     \
    ros-jazzy-ros2-control                  \
    ros-jazzy-joy*

```
#### Source ROS2 to bashrc file

Recommended to source ROS2 directly in your bashrc file. This will ensure all ROS2 files are property setup each time you open a new terminal. 
```bash
echo "source /opt/ros/jazzy/setup.bash" >> ~/.bashrc
```
If you do not do this, you will need to source ROS2 each time you open a new terminal window. 
```bash
source /opt/ros/jazzy/setup.bash
```

## Usage


#### Clone the Repository

Clone this repository into to where ever you would like on your computer. 


```bash
git clone https://github.com/JorlynLG/pfr_sim.git
```
Before running each package make sure to return to the main pfr_sim directory

## PFR RVIZ vizualizer
![image](https://github.com/user-attachments/assets/0eb8b9d6-ee8e-4bc7-b435-e56494db9c2f)

This repository already has the ROS2 workspaces set up, but if you would like to learn more about how to create on, look at this [ROS2 workspace tutorial](https://docs.ros.org/en/jazzy/Tutorials/Beginner-Client-Libraries/Creating-A-Workspace/Creating-A-Workspace.html).

Ensure you are in the correct directory.
```bash
cd prf_urdf_ws
```
Build the package
```bash
colcon build
```
After building the package, launch the ```display.launch.py``` file from the ```pfr_urdf_ws``` package:

```bash
source install/setup.bash
ros2 launch pfr_urdf_ws display.launch.py
```

## Launch PFR in Gazebo with 4 Wheel Steering Control
![image](https://github.com/user-attachments/assets/d7899369-1be4-4131-be92-5ce1d5d1cf89)

**Launch PFR in Gazebo**

Ensure you are in the correct directory.
```bash
cd pfr_gz_control_ws
```
Build the package
```bash
colcon build
```

In a new terminal, source the environment and launch the ``robot_spawn.launch.py`` file from the ```robot_sim``` package.
```bash
source install/setup.bash
ros2 launch robot_sim robot_spawn.launch.py
```

**4-Wheel Control for PRF**
In a new terminal, source the environment and launch the ```four_ws_control.launch.py``` file from the ```velocity_pub``` package.

```bash
source install/setup.bash
ros2 launch velocity_pub four_ws_control.launch.py
```
This will launch a GUI Joystick that you can use to control the robot, howeever you can also update the code to work with a physical joystick.
