#! /usr/bin/env python3
"""
@name:      Install.add_user
@author:    D. Brian Kimmel
@contact:   D.BrianKimmel@gmail.com
@copyright: (c) 2015-2015 by D. Brian Kimmel
@license:   MIT License
@note:      Created Dec 8, 2015
@Summary:   Deal with adding a user to the system.

"""

import crypt
import fileinput
import os
import platform
import pwd
import subprocess

SUDOERS = '/etc/sudoers'
SUDO_DIR = ' /etc/sudoers.d/'


class AddUser(object):
    """
    """

    def _add_linux(self, p_username):
        subprocess.call(['adduser', p_username])
        pass

    def add_one(self, p_username):
        l_sys = platform.system()
        print(l_sys)
        if l_sys == 'Linux':
            self._add_linux(p_username)

class User(object):
    """ Install the pyhouse user
    """

    @staticmethod
    def _create_workspace(p_user):
        print(' ')
        l_dir = '/home/' + p_user + '/workspace'
        l_user = pwd.getpwnam('pyhouse')
        if not os.path.isdir(l_dir):
            print('Creating a directory {}'.format(l_dir))
            os.makedirs(l_dir)
            os.chown(l_dir, l_user.pw_uid, l_user.pw_gid)

    @staticmethod
    def _update_sudoers(p_user):
        """Put new user into the sudoers file
        """
        print(' Allowing user {} FULL access to the system via sudo.'.format(p_user))
        processing_user = False
        for line in fileinput.input(SUDOERS, inplace = 1):
            if line.startswith(p_user):
                processing_user = True
            print(line)
        if processing_user:
            print('{} ALL=(ALL) NOPASSWD: ALL'.format(p_user))
        fileinput.close()
        print(' ')

    @staticmethod
    def _add_user(p_user):
        """
        """
        l_passwd = 'ChangeMe'
        l_encrypted = crypt.crypt(l_passwd, '3a')
        os.system('useradd --password {} --create-home {}'.format(l_encrypted, p_user))
        os.system('passwd -e {}'.format(p_user))
        print('  Added user "{}" with password {}'.format(p_user, l_passwd))
        print('  You MUST now change that password.\n')

    @staticmethod
    def _do_user_create(p_user):
        """ Do everything to add a pyhouse user.
        """
        print('  Creating user: {}'.format(p_user))
        try:
            pwd.getpwnam(p_user)
            print('*** User "{}" already exixts!  Skipping Add'.format(p_user))
        except KeyError:
            User._add_user(p_user)

    @staticmethod
    def add_one_user(p_user):
        """ This will add the pyhouse user
        """
        print(' Adding user "{}" now.'.format(p_user))
        User._do_user_create(p_user)
        User._update_sudoers(p_user)
        User._create_workspace(p_user)



if __name__ == "__main__":
    print(' Running  Install/add_user.py ...')
    l_api = AddUser()
    l_api.add_one('pyhouse')
    print(' Finished add_user.py\n')

#  ## END DBK
