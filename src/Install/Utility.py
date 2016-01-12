"""
@name:      PyHouse_Install/src/Install/Utility.py
@author:    D. Brian Kimmel
@contact:   D.BrianKimmel@gmail.com
@copyright: (c) 2015-2015 by D. Brian Kimmel
@license:   MIT License
@note:      Created on Oct 13, 2015
@Summary:

"""

# Import system type stuff
import os
try:
    import pwd
except ImportError:
    import Install.test.win_pwd as pwd


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

# ## END DBK
