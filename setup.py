#! /usr/bin/env python3
#  -*- coding: utf-8 -*-
"""
@name:      PyHouse_Install/setup.py
@author:    D. Brian Kimmel
@contact:   D.BrianKimmel@gmail.com
@copyright: (c) 2015-2015 by D. Brian Kimmel
@note:      Created on Oct 16, 2015
@license:   MIT License
@summary:   This installs on a new jessie system

It must be run as root:

    Login as any uer with sudo powers.\
    Copy this program to your home directory
    Run me by

        sudo python3 setup.py install

Examine the code closely

Jessie uses systemd and not the old SystemV init system so this will not work on anything earlier than jessie (Debian 8)

"""

#  Import system type stuff
import crypt
import fileinput
import getpass
import os
import pwd
import subprocess
import sys

SUDOERS = '/etc/sudoers'
SUDO_DIR = ' /etc/sudoers.d/'
HOME_DIR = '/home/pyhouse/'
WORKSPACE_DIR = HOME_DIR + 'workspace/'

class cd:
    """Context manager for changing the current working directory"""
    def __init__(self, p_new_path):
        self.m_new_path = os.path.expanduser(p_new_path)

    def __enter__(self):
        self.m_saved_path = os.getcwd()
        os.chdir(self.m_new_path)

    def __exit__(self, etype, value, traceback):
        os.chdir(self.m_saved_path)


class Jessie(object):
    """
    """

    def _update(self):
        print('  Update Raspbian')
        subprocess.call(['sudo', 'apt-get', 'q', 'update'])

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
        print(' Jessis is being updated/upgraded next.')
        self._update()
        self._upgrade()
        self._dist_upgrade()
        self._autoremove()


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
           #  we are in ~/Library
           print('  Current Directory: {}'.format(os.getcwd()))
           subprocess.call(['git', 'clone', 'http://github.com/DBrianKimmel/PyHouse_Install.git'])
           subprocess.call(['git', 'clone', 'http://github.com/DBrianKimmel/PyHouse.git'])
        #  outside the context manager we are back wherever we started.
        pass

    def add_all(self):
        print('  Adding all PyHouse repositories from github')
        self._create_workspace()



class Hostname(object):
    """
    """

    def change(self):
        pass


class User(object):
    """ Install the pyhouse user
    """

    @staticmethod
    def _create_workspace(p_user):
        print(' ')
        l_dir = WORKSPACE_DIR
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

    def add_one_user(self, p_user):
        """ This will add the pyhouse user
        """
        print(' Adding user "{}" now.'.format(p_user))
        User._do_user_create(p_user)
        User._update_sudoers(p_user)
        User._create_workspace(p_user)


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
        pass

    @staticmethod
    def SetupComputer():
        """
        Set up the computer:
            HostName
        """
        Computer().Hostname()

    @staticmethod
    def SetupTools():
        print('  Current Directory: {}'.format(os.getcwd()))
        subprocess.call(['wget', 'https://bootstrap.pypa.io/ez_setup.py'])
        subprocess.call(['echo ', 'sudo python'])

    def AddSoftware(self):
        print('  Add Software.')
        subprocess.call('sudo apt-get -y install gcc', shell = True)
        subprocess.call('sudo apt-get -y install python-pip', shell = True)

    def Install(self):
        """Install from scratch for a newly made jessie image.

        Fixes to install:
            /etc/apt/apt.conf.d/99timeout
            /etc/modprobe.d/8192cu.conf
            /usr/local/bin/update
        """

        print(" Running setup install.")
        self.CheckRoot()
        #  test then install a 'pyhouse' user
        #  Jessie().upgrade()
        User().add_one_user('pyhouse')
        #  Sys.SetupTools()
        self.AddSoftware()
        Repositories().add_all()
        AutoStart().configure()
        Firewalls().add_both()
        print(" Finished setup install.")


if __name__ == "__main__":
    print('Setup install of PyHouse_Install.  This will set up your entire PyHouse system on this computer.\n')
    Sys().Install()

#  ## END DBK
