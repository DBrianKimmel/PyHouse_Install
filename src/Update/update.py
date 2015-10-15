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
        for entry in os.scandir(INSTALL_DIR):
            if not entry.name.startswith('.') and entry.is_file():
                print(entry.name)
                shutil.copy(entry.name, BIN_DIR)  # Overwrite


if __name__ == "__main__":
    print('Running systemd.py ...')
    l_base = Base()
    l_base.make_bin_dir()

# ## END DBK
