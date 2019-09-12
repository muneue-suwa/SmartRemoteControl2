from slackclient import SlackClient
import sys
from smartrc import SmartRemoteControl
from config import ReadSetting, InitializeSetting


class SmartRemoteControlInit(SmartRemoteControl):
    def __init__(self):
        self.smartrc_dir = sys.argv[1]
        super().__init__(self.smartrc_dir)

    def main(self):
        init_setting = InitializeSetting(self.smartrc_dir)
        init_sc = SlackClient(init_setting.slack_token)
        channel_id = self.get_smartrc_channel_id(init_sc)
        init_setting.write_channel_id(channel_id)
        self.read_setting()
        msg =\
            "{} was added in '# smartrc' channel".format(self.setting.location)
        self.stool.send_a_message(msg)

if __name__ == "__main__":
    smrci = SmartRemoteControlInit()
    smrci.main()
