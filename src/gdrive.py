import subprocess
from os import path
import sys

# CompletedProcess(args=['gdrive', 'sync', 'upload', filename, wrong_id],
# returncode=1, stdout=b'', stderr=b'')
# CompletedProcess(args=['gdrive', 'sync', 'content', wrong_id],
# returncode=1, stdout=b'', stderr=b'')
# CompletedProcess(args=['gdrive', 'sync', 'content', correct_id],
# returncode=0, stdout=b'', stderr=b'')
# gdrive sync download [GDRIVE_ID] [DIRNAME]
# gdrive sync upload [DIRNAME] [GDRIVE_ID]
# gdrive sync content [GDRIVE_ID]


class GDrive:
    def __init__(self, is_initialization=False, smartrc_dir=None):
        if smartrc_dir is None:
            self.SMARTRC_DIR = sys.argv[1]
        else:
            self.SMARTRC_DIR = smartrc_dir

        if is_initialization is False:
            self.DATA_DIR = path.join(self.SMARTRC_DIR, "data")
            from config import ReadSetting
            setting = ReadSetting(self.SMARTRC_DIR)
            self.GDRIVE_ID = setting.return_gdrive_id()

    def initialization(self):
        from smartrc_init import SmartRemoteControlInit
        smart_remote_control_init =\
            SmartRemoteControlInit(smartrc_dir=self.SMARTRC_DIR)
        unconfirmed_gdrive_id =\
            smart_remote_control_init.config["GDRIVE"]["ID"]
        command_content =\
            ("gdrive sync content"
             " {gdrive_id}".format(gdrive_id=unconfirmed_gdrive_id))
        completed_process = self.run_command(command_content)
        if completed_process.returncode == 0:
            from config import ReadSetting
            setting = ReadSetting(self.SMARTRC_DIR)
            setting.config["GDRIVE"] = {"ID": unconfirmed_gdrive_id}
            with open(smart_remote_control_init.new_setting_filename, 'w')\
                    as configfile:
                setting.config.write(configfile)

    def download(self):
        command_download =\
            ("gdrive sync download "
             "{dirname} {gdrive_id}".format(gdrive_id=self.GDRIVE_ID,
                                            dirname=self.DATA_DIR))
        self.run_command(command_download)

    def upload(self):
        command_upload =\
            ("gdrive sync donwload "
             "{gdrive_id} {dirname}".format(gdrive_id=self.GDRIVE_ID,
                                            dirname=self.DATA_DIR))
        self.run_command(command_upload)

    def run_command(self, command):
        completed_process =\
            subprocess.run(command.split(" "), stdout=subprocess.PIPE,
                           stderr=subprocess.PIPE)
        if completed_process.returncode == 1:
            print("Error: "
                  "{}".format(completed_process.stdout.decode()).strip())
        return completed_process


if __name__ == "__main__":
    gd = GDrive(is_initialization=True)
    gd.initialization()
