#!/bin/bash

# This script launches two ROS launch files in different terminal windows

# Launch the first file in a new terminal
gnome-terminal -- bash -c "source ~/catkin_ws/devel/setup.bash; python3 /home/trinckets/catkin_ws/src/gazebo_multi_robot_spawn_ow/launch/multi_init.py; catkin_make; source ~/catkin_ws/devel/setup.bash; python3 /home/trinckets/catkin_ws/src/gazebo_multi_robot_spawn_ow/launch/multiparam.py; roslaunch gazebo_multi_robot_spawn gazebo_robots.launch; exec bash"

sleep 15
# Launch the second file iource n a new terminal
gnome-terminal -- bash -c "source ~/catkin_ws/devel/setup.bash; python3 /home/trinckets/catkin_ws/src/gazebo_multi_robot_spawn_ow/launch/multi_nav.py; roslaunch gazebo_multi_robot_spawn multi_nav.launch; exec bash"

sleep 10

gnome-terminal -- bash -c "source ~/catkin_ws/devel/setup.bash; rosrun rrt_star_path_planning_turtlebot multi_initial_pose; rosrun rrt_star_path_planning_turtlebot multi_goal_pose; exec bash"
# Alternatively, you can use xterm if gnome-terminal is not available
# xterm -hold -e "source /opt/ros/noetic/setup.bash; source ~/catkin_ws/devel/setup.bash; roslaunch package_name first_launch_file.launch" &
# xterm -hold -e "source /opt/ros/noetic/setup.bash; source ~/catkin_ws/devel/setup.bash; roslaunch package_name second_launch_file.launch" &

# Replace 'package_name', 'first_launch_file.launch', and 'second_launch_file.launch' with actual names
#python3 multiparam.py
#roslaunch gazebo_multi_robot_spawn gazebo_robots.launch
#python3 multi_nav.py
#roslaunch gazebo_multi_robot_spawn multi_nav.launch