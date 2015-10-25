#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@name:      PyHouse_Install/setup.py
@author:    D. Brian Kimmel
@contact:   D.BrianKimmel@gmail.com
@copyright: (c) 2015-2015 by D. Brian Kimmel
@note:      Created on Oct 16, 2015
@license:   MIT License
@summary:   This installs on a new jessie system

It must be run as root:

    sudo python setup install

Examine the code closely

Jessie uses systemd and not the old SystemV init system so this will not work on anything earlier than jessie (Debian 8)

"""

# Import system type stuff
import crypt
import fileinput
import os
import pwd
import subprocess
import sys


class Jessie(object):
    """
    """

    def _update(self):
        try:
            retcode = call("apt-get" + " update", shell = True)
            if retcode < 0:
                print("Child was terminated by signal {}".format(retcode))
            else:
                print >> sys.stderr, "Child returned", retcode
        except OSError as e:
            print >> sys.stderr, "Execution failed:", e

    def _upgrade(self):
        pass

    def upgrade(self):
        print('Jessis is being updated/upgraded next.')
        self._update()
        self._upgrade()


class Firewalls(object):
    """
    """

    def _v4(self):
        pass

    def _v6(self):
        pass

    def add_both(self):
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
        pass

    def add_all(self):
        print('Adding all PyHouse repositories from github')
        self._create_workspace()


class User(object):
    """ Install the pyhouse user
    """
    SUDOERS = '/etc/sudoers'

    def _change_users(self):
        pass

    def _add_sudoers(self):
        """Put new user into the sudoers file
        """
        processing_briank = False
        processing_pyhouse = False
        for line in fileinput.input(SUDOERS, inplace = 1):
            if line.startswith('briank'):
                processing_briank = True
            if line.startswith('pyhouse'):
                processing_pyhouse = True
            print(line)
        if not processing_briank:
            print('brink ALL=(ALL) NOPASSWD: ALL')
        if processing_pyhouse:
            print('pyhouse ALL=(ALL) NOPASSWD: ALL')

    def _add_pyhouse(self):
        """
        """
        l_passwd = 'ChangeMe'
        l_encrypted = crypt.crypt(l_passwd, '3a')
        os.system('useradd --password ' + l_encrypted + ' --create-home pyhouse')
        os.system('passwd -e pyhouse')
        print('Added user "pyhouse"')

    def _do_user(self):
        """ Do everything to add a pyhouse user.
        """
        try:
            pwd.getpwnam('pyhouse')
        except KeyError:
            self._add_user()
            self._add_sudoers()
        self._change_users()

    def add_user(self):
        print('Adding user "pyhouse" now.')
        self._do_user()


class Sys(object):
    """ This is a director that will run various installation sections.
    """

    @staticmethod
    def Scratch():
        """Install from scratch for a newly made jessie image.
        """
        print("Running - setup install.")
        # test then install a 'pyhouse' user
        Jessie().upgrade()
        User().add_user()
        Repositories().add_all()
        AutoStart().configure()
        Firewalls().add_both()


if __name__ == "__main__":
    print('Setup install of PyHouse_Install.  This will set up your entire system.')
    Sys.Scratch()

# ## END DBK
