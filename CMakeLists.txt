cmake_minimum_required(VERSION 2.8.3)
project(hands_sound)

find_package(catkin REQUIRED COMPONENTS
  message_generation
  message_runtime
  std_msgs
  rospy
)
add_message_files(FILES Beep.msg)
generate_messages(DEPENDENCIES std_msgs)

include_directories(${catkin_INCLUDE_DIRS})

