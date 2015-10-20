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
import stat

# Import PyHouseInstall files and modules.

HOME_DIR = '/home/pyhouse/'
BIN_DIR = HOME_DIR + 'bin/'
INSTALL_DIR = HOME_DIR + 'workspace/PyHouse_Install/bin'


class Base(object):
    """
    """

    def make_bin_dir(self):
        l_user = pwd.getpwnam('pyhouse')
        if not os.path.isdir(BIN_DIR):
            print('Creating a directory {}'.format(BIN_DIR))
            os.makedirs(BIN_DIR)
            os.chown(BIN_DIR, l_user.pw_uid, l_user.pw_gid)
        for l_entry in os.listdir(INSTALL_DIR):
            l_file = os.path.join(INSTALL_DIR, l_entry)
            l_target = os.path.join(BIN_DIR, l_entry)
            shutil.copy(l_file, BIN_DIR)
            try:
                os.chmod(l_target, stat.S_IRUSR | stat.S_IWUSR | stat.S_IXUSR | stat.S_IRGRP | stat.S_IXGRP | stat.S_IROTH | stat.S_IXOTH)
                os.chown(l_target, l_user.pw_uid, l_user.pw_gid)
                print('  Installed file {}'.format(l_target))
            except Exception as e_err:
                print('Error in changing {} - {}'.format(l_target, e_err))
        # for entry in os.scandir(INSTALL_DIR):  # this requires Python 3.5
        #    if not entry.name.startswith('.') and entry.is_file():
        #        print(entry.name)
        #        shutil.copy(entry.name, BIN_DIR)  # Overwrite


if __name__ == "__main__":
    print('Running Update/update.py ...')
    l_base = Base()
    l_base.make_bin_dir()
    print('Finished update.py')

# ## END DBK
