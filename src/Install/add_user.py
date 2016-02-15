"""
@name:      Install.add_user
@author:    D. Brian Kimmel
@contact:   D.BrianKimmel@gmail.com
@copyright: (c) 2015-2015 by D. Brian Kimmel
@license:   MIT License
@note:      Created Dec 8, 2015
@Summary:   Add a 'PyHouse' user.

"""
import platform
import subprocess


class AddUser(object):
    """
    """

    def _add_linux(self, p_username):
        subprocess.call(['adduser', '--disabled-password', p_username])

    def _create_ssh(self):
        pass

    def add_one(self, p_username):
        l_sys = platform.system()
        print(l_sys)
        if l_sys == 'Linux':
            self._add_linux(p_username)


if __name__ == "__main__":
    print('Running  Install/add_user.py ...')
    l_api = AddUser()
    l_api.add_one('pyhouse')
    print('Finished add_user.py\n')

# ## END DBK
