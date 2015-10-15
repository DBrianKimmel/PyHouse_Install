"""
@name:      PyHouse_Install/src/Update/update.py
@author:    D. Brian Kimmel
@contact:   D.BrianKimmel@gmail.com
@copyright: (c) 2015-2015 by D. Brian Kimmel
@license:   MIT License
@note:      Created on Oct 14, 2015
@Summary:

"""

# Import system type stuff
import os
import pwd
import shutil

# Import PyHouseInstall files and modules.

HOME_DIR = '/home/pyhouse/'
BIN_DIR = HOME_DIR + 'bin/'
INSTALL_DIR = HOME_DIR + 'workspace/PyHouse_Install/bin'


class Base(object):
    """
    """

    def make_bin_dir(self):
        if not os.path.isdir(BIN_DIR):
            os.makedirs(BIN_DIR)
        for l_entry in os.listdir(INSTALL_DIR):
            l_file = os.path.join(INSTALL_DIR, l_entry)
            shutil.copy(l_file, BIN_DIR)
            os.chmod(l_file, 755)
            os.chown(l_file, pwd.getpwnam.pw_uid, pwd.getpwnam.pw_gid)
        # for entry in os.scandir(INSTALL_DIR):  # this requires Python 3.5
        #    if not entry.name.startswith('.') and entry.is_file():
        #        print(entry.name)
        #        shutil.copy(entry.name, BIN_DIR)  # Overwrite


if __name__ == "__main__":
    print('Running systemd.py ...')
    l_base = Base()
    l_base.make_bin_dir()

# ## END DBK
