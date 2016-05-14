#! /usr/bin/env python3
"""
@name:      src/install.py
@author:    D. Brian Kimmel
@contact:   D.BrianKimmel@gmail.com
@copyright: (c) 2016-2016 by D. Brian Kimmel
@license:   MIT License
@note:      Created May 11, 2016
@Summary:   Install.

This is run after the user 'pyhouse' is created and functional.



"""

#  Import system stuff
import os
import pwd


#  Import PyHouse_Install stuff
try:
    from Install import Utility
except ImportError as e_err:
    print('ERROR -1 {}'.format(e_err))
    try:
        from src.Install import Utility
    except ImportError as e_err:
        print('ERROR -2 {}'.format(e_err))


HOME_DIR = '/home/pyhouse/'
BIN_DIR = HOME_DIR + 'bin/'
WORK_DIR = HOME_DIR + 'workspace/'
INSTALL_DIR = WORK_DIR + 'PyHouse_Install/'
SRC_DIR = INSTALL_DIR + 'src/'


class User(object):
    """ Install the pyhouse user
    """

    @staticmethod
    def create_dir(p_dir):
        print(' ')
        l_user = pwd.getpwnam('pyhouse')
        if not os.path.isdir(p_dir):
            print('  Creating a directory {}'.format(p_dir))
            os.makedirs(p_dir)
            os.chown(p_dir, l_user.pw_uid, l_user.pw_gid)


class Sys(object):
    """ This is a director that will run various installation sections.
    """

    def make_bin(self):
        print("  Creating bin dir for commands.")
        User.create_dir('bin')

    def Install(self):
        """Install from scratch for a newly made jessie image.

        Fixes to install:
            /etc/apt/apt.conf.d/99timeout
            /etc/modprobe.d/8192cu.conf
            /usr/local/bin/update
        """

        print(" Running install.")
        self.make_bin()


if __name__ == "__main__":
    print('Part 2 of Setup install of PyHouse_Install.  This will set up your entire PyHouse system on this computer.\n')
    Sys().Install()

#  ## END DBK
