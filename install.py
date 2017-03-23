#! /usr/bin/env python
"""
@name:      src/install.py
@author:    D. Brian Kimmel
@contact:   D.BrianKimmel@gmail.com
@copyright: (c) 2016-2017 by D. Brian Kimmel
@license:   MIT License
@note:      Created May 11, 2016
@Summary:   Install.

This is run after the user 'pyhouse' is created and functional.



"""

#  Import system stuff
import os
import pwd
import shutil
import stat
import sys

sys.path.append('/home/pyhouse/PyHouse_Install/src')
sys.path.append('/home/pyhouse/workspace/PyHouse_Install')
sys.path.append('/home/pyhouse/workspace/PyHouse_Install/src')

#  Import PyHouse_Install stuff
from Install import Utility

HOME_DIR = '/home/pyhouse/'
HOME_BIN_DIR = HOME_DIR + 'bin/'
WORK_DIR = HOME_DIR + 'workspace/'
INSTALL_DIR = WORK_DIR + 'PyHouse_Install/'
INSTALL_BIN_DIR = INSTALL_DIR + 'bin/'
SRC_DIR = INSTALL_DIR + 'src/'
CONFIG_DIR = '/etc/pyhouse'
LOG_DIR = '/var/log/pyhouse'


class User(object):
    """ Install the pyhouse user
    """

    @staticmethod
    def _copy_bin_files():
        l_user = pwd.getpwnam('pyhouse')
        for l_entry in os.listdir(INSTALL_BIN_DIR):
            l_file = os.path.join(INSTALL_BIN_DIR, l_entry)
            l_target = os.path.join(HOME_BIN_DIR, l_entry)
            shutil.copy(l_file, HOME_BIN_DIR)
            try:
                os.chmod(l_target, stat.S_IRUSR | stat.S_IWUSR | stat.S_IXUSR | stat.S_IRGRP | stat.S_IXGRP | stat.S_IROTH | stat.S_IXOTH)
                os.chown(l_target, l_user.pw_uid, l_user.pw_gid)
                print('  Installed file {}'.format(l_target))
            except Exception as e_err:
                print('Error in changing {} - {}'.format(l_target, e_err))
        pass


class Sys(object):
    """ This is a director that will run various installation sections.
    """

    def Install(self):
        """Install from scratch for a newly made jessie image.

        Fixes to install:
            /etc/apt/apt.conf.d/99timeout
            /etc/modprobe.d/8192cu.conf
            /usr/local/bin/update
        """

        print(' Running install.')
        Utility.Utilities.MakeDir(HOME_BIN_DIR, 'pyhouse')
        Utility.Utilities.MakeDir(CONFIG_DIR, 'pyhouse')
        Utility.Utilities.MakeDir(LOG_DIR, 'pyhouse')
        User._copy_bin_files()


if __name__ == "__main__":
    print('Part 2 of Setup install of PyHouse_Install.  This will set up your entire PyHouse system on this computer.')
    Utility.Utilities().must_not_be_root()
    Sys().Install()

#  ## END DBK
