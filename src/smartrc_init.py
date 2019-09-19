from configparser import ConfigParser
from os import path
from slackclient import SlackClient
import sys
from smartrc import SmartRemoteControl

# from config import ReadSetting, InitializeSetting
# class InitializeSetting:
#     def __init__(self, smartrc_dir):
#         old_setting_filename =\
#             path.join(smartrc_dir, "setting/smartrc.cfg")
#         if not path.isfile(old_setting_filename):
#             raise FileNotFoundError("setting/smartrc.cfg is not found")
#         self.config = configparser.ConfigParser()
#
#         self.new_setting_filename =\
#             path.join(smartrc_dir, "setting/.smartrc.cfg")
#
#         self.config.read(old_setting_filename)
#         self.slack_token = self.config["SLACK"]["SLACK_API_TOKEN"]
#
#     def write_channel_id(self, channel_id):
#         self.config["SLACK"]["CHANNEL_ID"] = channel_id
#         with open(self.new_setting_filename, 'w') as configfile:
#             self.config.write(configfile)


class SmartRemoteControlInit(SmartRemoteControl):
    def __init__(self, smartrc_dir=None):
        if smartrc_dir is None:
            self.SMARTRC_DIR = sys.argv[1]
        else:
            self.SMARTRC_DIR = smartrc_dir
        super().__init__(self.SMARTRC_DIR)

        old_setting_filename =\
            path.join(self.SMARTRC_DIR, "setting/smartrc.cfg")
        if not path.isfile(old_setting_filename):
            raise FileNotFoundError("setting/smartrc.cfg is not found")
        self.new_setting_filename =\
            path.join(self.SMARTRC_DIR, "setting/.smartrc.cfg")

        self.config = ConfigParser()
        self.config.read(old_setting_filename)
        self.slack_token = self.config["SLACK"]["SLACK_API_TOKEN"]

    def write_channel_id(self, channel_id):
        self.config["SLACK"]["CHANNEL_ID"] = channel_id
        with open(self.new_setting_filename, 'w') as configfile:
            self.config.write(configfile.remove_section["GDRIVE"])

    def main(self):
        init_sc = SlackClient(self.slack_token)
        channel_id = self.get_smartrc_channel_id(init_sc)
        # <- Must be added exception for slackclient
        self.write_channel_id(channel_id)
        self.read_setting()
        msg =\
            "{} was added in '# smartrc' channel".format(self.setting.location)
        self.stool.send_a_message(msg)


if __name__ == "__main__":
    smrci = SmartRemoteControlInit()
    smrci.main()
