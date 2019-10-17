#!/usr/bin/env python

import sys
import rospy
from sound_play.msg import SoundRequest
from sound_play.libsoundplay import SoundClient
from std_msgs.msg import String

class SpeechEngine():
    def __init__(self):
        rospy.init_node('speech_engine', anonymous = True)
        self.soundhandle = SoundClient()
        
        self.voice = 'voice_kal_diphone'
        self.volume = 1.0

        rospy.Subscriber("/experiment/chatter", String, self.callback)
        rospy.spin()
        
    def set_volume(self, volume):
        self.volume = volume
    def set_voice(self, voice):
        self.voice = voice

    def say(self, text):
        self.soundhandle.say(text, self.voice, self.volume)
        rospy.loginfo("I am saying %s with volume %f and voice of '%s'", text, self.volume, self.voice)
    
    def callback(self, data):
        self.say(data.data)

if __name__ == '__main__':
    SpeechEngine()
