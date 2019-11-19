#!/usr/bin/env python

import rospy
# from std_msgs.msg import String
from sound_ros.msg import Beep

def beeper():
    pub = rospy.Publisher('/beep_engine/beep', Beep, queue_size=10)
    rospy.init_node('beeper', anonymous=True)
    rate = rospy.Rate(0.4) # 10hz
    
    while not rospy.is_shutdown():
        msg = Beep()
        # msg.header.frame_id = "emg"
        msg.header.stamp = rospy.get_rostime()
        msg.volume = 1.0
        msg.tone_name = "short_beep.wav"
        
        pub.publish(msg)
        rate.sleep()

if __name__ == '__main__':
    try:
        beeper()
    except rospy.ROSInterruptException:
        pass