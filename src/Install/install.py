"""
-*- test-case-name: /home/briank/git/PyHouse_Install/src/Install/install.py -*-

@name:      /home/briank/git/PyHouse_Install/src/Install/install.py
@author:    D. Brian Kimmel
@contact:   D.BrianKimmel@gmail.com
@copyright: (c) 2016-2016 by D. Brian Kimmel
@note:      Created on Aug 26, 2016
@license:   MIT License
@summary:   Second stage install of PyHouse.

This is the second stage install of the PyHouse system.

    sudo su pyhouse -l

and then run the pyhouse installation as that user:

    python workspace/PyHouse_Install/src/Install/install.py





"""

__updated__ = '2016-08-26'

#  Import system type stuff
import os
import subprocess

HOME_DIR = '/home/pyhouse/'
WORKSPACE_DIR = HOME_DIR + 'workspace/'


class cm_cd:
    """ Context manager for changing the current working directory
    """
    def __init__(self, p_new_path):
        self.m_new_path = os.path.expanduser(p_new_path)

    def __enter__(self):
        self.m_saved_path = os.getcwd()
        os.chdir(self.m_new_path)

    def __exit__(self, etype, value, traceback):
        os.chdir(self.m_saved_path)


class AutoStart(object):
    """ Setup to make the PyHouse system start up right after booting,
    Also, setup to reboot weekly.

    First - Install autoboot.config in /etc/systemd/system/getty@tty1.service.d
    Next - Enable autoboot

    """

    def configure(self):
        pass

    def Install(self):
        """ Install or update the autostart
        """
        pass


class Repositories(object):
    """ Setup the repositories
    """

    def _create_workspace(self):
        with cm_cd(WORKSPACE_DIR):
            #  we are in ~/workspace
            print('  Current Directory: {}'.format(os.getcwd()))
            subprocess.call(['git', 'clone', 'https://github.com/DBrianKimmel/PyHouse_Install.git'])
            subprocess.call(['git', 'clone', 'https://github.com/DBrianKimmel/PyHouse.git'])
        #  outside the context manager we are back wherever we started.
        pass

    def add_all(self):
        print('  Adding all PyHouse repositories from github')
        if os.path.isdir(WORKSPACE_DIR):
            # Update
            os.system('cd {}'.format(WORKSPACE_DIR + 'PyHouse'))
            subprocess.call(['git', 'pull'])
            os.system('cd {}'.format(WORKSPACE_DIR + 'PyHouse_Install'))
            subprocess.call(['git', 'pull'])
        else:
            self._create_workspace()

    def Install(self):
        """ Install or update the repositories,
        """
        pass


if __name__ == "__main__":
    print(' Running  Install/install.py ...')
    Repositories().Install()
    AutoStart.Install()
    print(' Finished Install/install.py\n')

# ## END DBK
