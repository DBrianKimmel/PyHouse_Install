#! /usr/bin/env python
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
        pass


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

    def add_all(self):
        pass


class User(object):
    """ Install the pyhouse user
    """

    def _add_sudoers(self):
        pass

    def _add_user(self):
        l_passwd = 'ChangeMe'
        l_encrypted = crypt.crypt(l_passwd, '3a')
        os.system('useradd --password ' + l_encrypted + ' --create-home pyhouse')

    def _test_user(self):
        try:
            pwd.getpwnam('pyhouse')
        except KeyError:
            self._add_user()

    def add_user(self):
        self._test_user()


class Sys(object):
    """ This is a director that will run various installation sections.
    """

    @staticmethod
    def Scratch():
        """Install from scratch for a newly made jessie image.
        """
        print("Running - Scratch install.")
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
