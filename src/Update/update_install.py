"""
@name:      PyHouse_Install/src/Update/update_install.py
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
# from Install.Utility import Utilities as utilUtil

HOME_DIR = '/home/pyhouse/'
BIN_DIR = HOME_DIR + 'bin/'
INSTALL_DIR = HOME_DIR + 'workspace/PyHouse_Install/bin'


class Utilities(object):
    """
    """

    @staticmethod
    def get_user_ids(p_user_name):
        l_user = pwd.getpwnam(p_user_name)
        l_uid = l_user.pw_uid
        l_gid = l_user.pw_gid
        return l_uid, l_gid

    @staticmethod
    def is_dir(p_path):
        return os.path.isdir(p_path)

    @staticmethod
    def MakeDir(p_dir_name, p_user_name):
        l_uid, l_gid = Utilities.get_user_ids(p_user_name)
        if not os.path.isdir(p_dir_name):
            print('Creating a directory {}'.format(p_dir_name))
            os.makedirs(p_dir_name)
            os.chown(p_dir_name, l_uid, l_gid)


class Api(object):
    """
    """

    def make_pyhouse_dialout(self):
        pass

    def make_etc_dir(self):
        Utilities.MakeDir('/etc/pyhouse/', 'pyhouse')

    def make_log_dir(self):
        Utilities.MakeDir('/var/log/pyhouse/', 'pyhouse')

    def make_bin_dir(self):
        Utilities.MakeDir('bin', 'pyhouse')
        l_user = pwd.getpwnam('pyhouse')

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

    def copy_pyhouse_service(self):
        """ Install in ~/.config/systemd/user/pyhouse.service
        """
        l_user = pwd.getpwnam('pyhouse')
        l_file = 'pyhouse.service'
        l_dir = HOME_DIR + '.config/systemd/user/'
        l_src = HOME_DIR + 'workspace/PyHouse_Install/src/files/' + l_file
        l_dest = os.path.join(l_dir, l_file)
        if not os.path.isdir(l_dir):
            print('Creating a directory {}'.format(l_dir))
            os.makedirs(l_dir)
            os.chown(l_dir, l_user.pw_uid, l_user.pw_gid)
        shutil.copy(l_src, l_dir)
        os.chown(l_dest, l_user.pw_uid, l_user.pw_gid)
        print('  Copied file "{}" to "{}"'.format(l_src, l_dest))

    def update(self):
        self.make_bin_dir()
        self.copy_pyhouse_service()
        self.make_etc_dir()
        self.make_log_dir()


if __name__ == "__main__":
    print('---Running Update/update_install.py ...')
    l_api = Api()
    l_api.update()
    print('---Finished update_install.py\n')

# ## END DBK
