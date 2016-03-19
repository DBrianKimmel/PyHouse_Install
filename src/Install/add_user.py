#! /usr/bin/env python3
"""
@name:      Install.add_user
@author:    D. Brian Kimmel
@contact:   D.BrianKimmel@gmail.com
@copyright: (c) 2015-2015 by D. Brian Kimmel
@license:   MIT License
@note:      Created Dec 8, 2015
@Summary:   Add a 'PyHouse' user.

"""

#  Import system stuff
import os
import platform
import pwd
import subprocess

SUDOERS = '/etc/sudoers'
SUDO_DIR = '/etc/sudoers.d/'


class AddUser(object):
    """
    """

    def _add_linux(self, p_username):
        subprocess.call(['sudo ', 'adduser ', '--disabled-login ', p_username])

    def _create_ssh(self):
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
        #  l_user = pwd.getpwnam('pyhouse')
        if not os.path.isdir(l_dir):
            print('Creating a directory {}'.format(l_dir))
            subprocess.call(['sudo', 'mkdir', l_dir])
            #  os.makedirs(l_dir)
            subprocess.call(['sudo', 'chown', p_user + ':' + p_user, l_dir])
            #  os.chown(l_dir, l_user.pw_uid, l_user.pw_gid)

    @staticmethod
    def _update_sudoers(p_user):
        """Put new user into the /etc/sudoers.d
        """
        l_dir = './PyHouse_Install/src/files/'
        print(' Allowing user "{}" FULL access to the system via sudo.'.format(p_user))
        try:
            for l_file in os.listdir(l_dir):
                if l_file.startswith('sudo-'):
                    l_from = os.path.join(l_dir, l_file)
                    l_to = os.path.join(SUDO_DIR, l_file[5:])
                    print('--files "{}" -- "{}"'.format(l_from, l_to))
                    subprocess.call(['sudo', 'cp', l_from, l_to])
                    subprocess.call(['sudo', 'chmod', '440', l_to])
        except (OSError, IOError) as e_err:
            print(' ** ERROR ** {}'.format(e_err))
        print(' ')

    @staticmethod
    def _add_user(p_user):
        """
        """
        subprocess.call(['sudo', 'adduser', '--disabled-login', 'pyhouse'])
        subprocess.call(['sudo', 'usermod', '-a', '--groups', 'dialout', 'pyhouse'])
        print('  Added user "{}"'.format(p_user))
        print('  You MUST change that users password.\n')

    @staticmethod
    def _do_user_create(p_user):
        """ Do everything to add a pyhouse user.
        """
        print('  Creating user: "{}"'.format(p_user))
        try:
            pwd.getpwnam(p_user)
            print('*** User "{}" already exixts!  Skipping Add'.format(p_user))
        except KeyError:
            User._add_user(p_user)

    @staticmethod
    def add_one_user(p_user):
        """ This will add the pyhouse user from setup.py
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
