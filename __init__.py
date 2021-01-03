from mycroft import MycroftSkill, intent_file_handler
import os
import subprocess

class WhiteNoise(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('noise.white.intent')
    def handle_noise_white(self, message):
        self.speak_dialog("goodnight")
        os.system("/usr/bin/aplay /home/craghack/Downloads/white-noise.wav")

    @intent_file_handler('stop.noise.intent')
    def handle_stop_noise(self, message):
        cmd = subprocess.check_output("ps -aux | grep \"white\"", shell=True).decode("utf-8").rstrip()
        cmd = cmd.split('\n')
        stopped = False
        for c in cmd:
            if 'grep' in c:
                continue
            pid = c.split()
            os.system("kill " + pid[1])
            stopped = True
        if not stopped:
            self.speak_dialog("not.running")
        else:
            self.speak_dialog("stopped")

def create_skill():
    return WhiteNoise()

