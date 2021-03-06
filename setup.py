#! /usr/bin/env python3
#  -*- coding: utf-8 -*-
"""
@name:      PyHouse_Install/setup.py
@author:    D. Brian Kimmel
@contact:   D.BrianKimmel@gmail.com
@copyright: (c) 2015-2016 by D. Brian Kimmel
@note:      Created on Oct 16, 2015
@license:   MIT License
@summary:   This installs on a new jessie system

This must NOT be run as root:

Login as any uer with sudo powers.
Clone the PyHouse Suite instalation software

    git clone https://github.com/DBrianKimmel/PyHouse_Install.git

Then run the software to install the the base.
It will create the 'pyhouse user, install the necessary debian packages, ...

    python PyHouse_Install/setup.py install

This will create the user 'pyhouse' and clone the two packages 'PyHouse' and 'PyHouse_Install.
Then you may claan up by removing the 'PyHouse_Install package.
Then change to the pyhouse user:

    sudo su pyhouse -l

and then run the pyhouse installation as that user:

    python workspace/PyHouse_Install/src/Install/install.py





Examine the code closely for your own ease of mind.

Jessie uses systemd and not the old SystemV init system so this will not work on anything earlier than jessie (Debian 8)

"""

__updated__ = '2017-08-18'

#  Import system type stuff
import crypt
import fileinput
import getpass
import os
import pwd
import subprocess
import sys

sys.path.append('/home/pyhouse/PyHouse_Install')
sys.path.append('/home/pyhouse/PyHouse_Install/src')
sys.path.append('/home/pyhouse/workspace/PyHouse_Install')
sys.path.append('/home/pyhouse/workspace/PyHouse_Install/src')
# print(sys.path)

#  Import PyHouse_Install stuff
try:
    from src.Install import add_user  # This one works best for me so it is first.
except ImportError as e_err:
    print('ERROR-1 - Not found "src.Install.add_user" {}'.format(e_err))
    try:
        from Install import add_user
    except ImportError as e_err:
        print('ERROR-2 - Not found "Install.add_user" {}'.format(e_err))
        try:
            import add_user
        except ImportError as e_err:
            print('ERROR-3 - Not found "add_user"{}'.format(e_err))


SUDOERS = '/etc/sudoers'
SUDO_DIR = ' /etc/sudoers.d/'
HOME_DIR = '/home/pyhouse/'
WORKSPACE_DIR = HOME_DIR + 'workspace/'

class cd:
    """Context manager for changing the current working directory
    """
    def __init__(self, p_new_path):
        self.m_new_path = os.path.expanduser(p_new_path)

    def __enter__(self):
        self.m_saved_path = os.getcwd()
        os.chdir(self.m_new_path)

    def __exit__(self, etype, value, traceback):
        os.chdir(self.m_saved_path)


class Wheezy(object):
    """ This is for the 'Wheezy' release of Raspbian 2013-08-01
    """


class Jessie(object):
    """ This is for the 'Jessie' release of Raspbian lite 2015-08-01
    """

    def _update(self):
        print('  Update Raspbian')
        subprocess.call(['sudo', 'apt-get', '-q', 'update'])

    def _upgrade(self):
        print('  Upgrade Raspbian')
        subprocess.call(['sudo', 'apt-get', '-yq', 'upgrade'])

    def _dist_upgrade(self):
        print('  Dist Upgrade Raspbian')
        subprocess.call(['sudo', 'apt-get', '-yq', 'dist-upgrade'])

    def _autoremove(self):
        print('  AutoRemove Raspbian')
        subprocess.call(['sudo', 'apt-get', '-yq', 'autoremove'])

    def upgrade(self):
        print(' Jessie is being updated/upgraded next.')
        self._update()
        self._upgrade()
        self._dist_upgrade()
        self._autoremove()


class Stretch(object):
    """ This is for the 'Stretch' release of Raspbian lite 2017-08-15
    """

    def _update(self):
        print('  Update Raspbian-lite "Stretch"')
        subprocess.call(['sudo', 'apt', 'q', 'update'])

    def _upgrade(self):
        print('  Upgrade Raspbian-lite "Stretch"')
        subprocess.call(['sudo', 'apt', '-yq', 'upgrade'])

    def _autoremove(self):
        print('  AutoRemove Raspbian')
        subprocess.call(['sudo', 'apt', '-yq', 'autoremove'])

    def upgrade(self):
        print(' Raspbian-lite Stretch is being updated/upgraded next.')
        self._update()
        self._upgrade()
        self._autoremove()


class Raspbian(object):
    """
    """

    def upgrade(self):
        # Get the version of the OS installed somehow...
        version = 9
        if version == 7:
            Wheezy().update()
        elif version == 8:
            Jessie().upgrade()
        elif version == 9:
            Stretch().upgrade()
        else:
            print('ERROR Unknown version of the OS ---')


class Firewalls(object):
    """
    """

    def _v4(self):
        print(' --IPv4 firewall programs missing.')

    def _v6(self):
        print(' --IPv4 firewall programs missing.')

    def add_both(self):
        print('')
        print('Firewall setup.')
        self._v4()
        self._v6()


class AutoStart(object):
    """ Setup to make the PyHouse system start up right after booting,
    Also, setup to reboot weekly.
    """

    def configure(self):
        pass


class Repositories(object):
    """ Setup the repositories
    """

    def _create_workspace(self):
        with cd(WORKSPACE_DIR):
           #  we are in ~/workspace
           print('  Current Directory: {}'.format(os.getcwd()))
           subprocess.call(['git', 'clone', 'https://github.com/DBrianKimmel/PyHouse_Install.git'])
           subprocess.call(['git', 'clone', 'https://github.com/DBrianKimmel/PyHouse.git'])
        #  outside the context manager we are back wherever we started.
        pass

    def add_all(self):
        print('  Adding all PyHouse repositories from github')
        if os.path.isdir('{}'.format(WORKSPACE_DIR + 'PyHouse')):
            print('   Updating Already installed repositories.')
            os.system('cd {}'.format(WORKSPACE_DIR + 'PyHouse'))
            subprocess.call(['git', 'pull'])
            os.system('cd {}'.format(WORKSPACE_DIR + 'PyHouse_Install'))
            subprocess.call(['git', 'pull'])
        else:
            self._create_workspace()


class Hostname(object):
    """
    """

    def change(self):
        pass


class Computer(object):
    """
    Set up the computer itself
    """

    def Hostname(self):
        """
        Display the current hostname - allow installer to change it.
        """
        pass


class Sys(object):
    """ This is a director that will run various installation sections.
    """

    def CheckRoot(self):
        l_user = getpass.getuser()
        if l_user == 'root':
            exit('You must not be root (no sudo)! - Aborting!')

    @staticmethod
    def SetupComputer():
        """
        Set up the computer:
            HostName
        """
        Computer().Hostname()

    @staticmethod
    def SetupTools():
        print('  SetupTools - Current Directory: {}'.format(os.getcwd()))
        subprocess.call(['wget', 'https://bootstrap.pypa.io/ez_setup.py'])
        subprocess.call(['echo ', 'sudo python'])

    def AddSoftware(self):
        print('  Add Software.')
        subprocess.call('sudo apt -y install gcc', shell=True)
        subprocess.call('sudo apt -y install python3-pip', shell=True)

    def Install(self):
        """Install from scratch for a newly made jessie image.

        Fixes to install:
            /etc/apt/apt.conf.d/99timeout
            /etc/modprobe.d/8192cu.conf
            /usr/local/bin/update
        """

        print(" Running setup.Sys().Install().")
        self.CheckRoot()
        Raspbian().upgrade()
        add_user.User().add_one_user('pyhouse')
        #  Sys.SetupTools()
        self.AddSoftware()
        Repositories().add_all()
        AutoStart().configure()
        Firewalls().add_both()
        print(" Finished setup install.")


if __name__ == "__main__":
    print('Setup install of PyHouse_Install.\nThis will set up your entire PyHouse system on this computer.\nDo not use sudo!\n')
    Sys().Install()
    print('\nFinished Installing the PyHouse Suites.\n')

#  ## END DBK
