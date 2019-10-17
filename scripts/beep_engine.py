#!/usr/bin/env python

import os, sys
import rospy
from sound_play.msg import SoundRequest
from sound_play.libsoundplay import SoundClient

from hands_msgs.msg import Beep

class BeepEngine():
    def __init__(self):
        rospy.init_node('beep_engine')
        self.soundhandle = SoundClient()
        rospy.Subscriber("~beep", Beep, self.callback)
        self.beep_dir = rospy.get_param("~beep_dir")
        rospy.on_shutdown(self.shutdown)
        rospy.spin()

    def beep(self, filename, volume):
        self.soundhandle.playWave(filename, volume)
    
    def callback(self, data):
        ## data.header
        filename = os.path.join(self.beep_dir, data.tone_name)
        self.beep(filename, data.volume)
    def shutdown(self):
        self.soundhandle.stopAll()


if __name__ == '__main__':
    BeepEngine()

    
    
