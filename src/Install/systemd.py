#!/usr/bin/env python3
"""
@name:      PyHouse_Install/src/Install/systemd.py
@author:    D. Brian Kimmel
@contact:   D.BrianKimmel@gmail.com
@copyright: (c) 2015-2015 by D. Brian Kimmel
@license:   MIT License
@note:      Created on Oct 13, 2015
@Summary:

"""

#  Import system type stuff
import os
import shutil

#  Import PyHouseInstall files and modules.
from Install.Utility import Utilities

SYSTEMD_DIR = '/etc/systemd/system/'
TTY1_DIR = '/etc/systemd/system/getty@tty1.service.d/'
TTY1_FILE = '/etc/systemd/system/getty@tty1.service.d/autologin.conf'
HOME_DIR = '/home/pyhouse/'
SRC_FILE = HOME_DIR + 'workspace/PyHouse_Install/src/files/autologin.conf'


class AutoStartOnBoot(object):
    """
    This will set up the Raspi to auto login and start PyHouse on boot.

    mkdir -p /etc/systemd/system/getty@tty1.service.d/
    cp autologin.conf /etc/systemd/system/getty@tty1.service.d/autologin.conf
    """

    def detect_systemd(self):
        """ Find out if we are a systemd or sysVinit system
        """
        if os.path.isdir(SYSTEMD_DIR):
            self.m_systemd = True
            print('Running systemd')
            self.install_autologin()
        elif os.path.isfile('/sbin/init'):
            print('Running systemVinit')
        else:
            print('Not running something I can install my start on boot routines!')

    def install_autologin(self):
        """
        sudo systemctl disable getty@tty1
        sudo systemctl enable autologin@tty1
        sudo systemctl start autologin@tty1
        """
        if not os.path.isdir(TTY1_DIR):
            print('Creating a directory {}'.format(TTY1_DIR))
            os.makedirs(TTY1_DIR)
            # Utilities.MakeDir(TTY1_DIR, 'root')
        #  if not os.path.isfile(TTY1_FILE):
        shutil.copy(SRC_FILE, TTY1_DIR)  #  Overwrite
        print('  Installed file {}'.format(SRC_FILE))


if __name__ == "__main__":
    print(' Running Install/systemd.py ...')
    l_boot = AutoStartOnBoot()
    l_boot.detect_systemd()
    print(' Finished systemd.py\n')

#  ## END DBK
