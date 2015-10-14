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

# Import system type stuff
import os
import shutil

# Import PyHouseInstall files and modules.

SYSTEMD_DIR = '/etc/systemd/system/'
TTY1_DIR = '/etc/systemd/system/getty@tty1.service.d/'
TTY1_FILE = '/etc/systemd/system/getty@tty1.service.d/autologin.conf'
SRC_FILE = '/home/pyhouse/workspace/PyHouse_Install/src/files/autologin.conf'


"""
    mkdir -p /etc/systemd/system/getty@tty1.service.d/

    cp autologin.conf /etc/systemd/system/getty@tty1.service.d/autologin.conf
"""

class AutoStartOnBoot(object):
    """
    This will set up tye Raspi to auto login and start PyHouse on boot.
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
        """
        if not os.path.isdir(TTY1_DIR):
            os.makedirs(TTY1_DIR)
        if not os.path.isfile(TTY1_FILE):
            shutil.copy(SRC_FILE, TTY1_DIR)


if __name__ == "__main__":
    print('Running...')
    l_boot = AutoStartOnBoot()
    l_boot.detect_systemd()

# ## END DBK
