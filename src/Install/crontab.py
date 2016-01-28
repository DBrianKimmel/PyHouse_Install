#!/usr/bin/env python3
"""
@name:      PyHouse_Install/src/Install/crontab.py
@author:    D. Brian Kimmel
@contact:   D.BrianKimmel@gmail.com
@copyright: (c) 2015-2015 by D. Brian Kimmel
@license:   MIT License
@note:      Created on Oct 19, 2015
@Summary:   Installs a crontab for a PyHouse Node

Crontab to reboot once a week

"""


if __name__ == "__main__":
    print(' Running crontab.py ...')
    l_boot = AutoStartOnBoot()
    l_boot.detect_systemd()
    print(' Finished crontab.py\n')

#  ## END DBK
