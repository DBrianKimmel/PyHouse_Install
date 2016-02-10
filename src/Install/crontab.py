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

#  Import system stuff
import os

CRON_DIR = '/var/spool/cron/crontabs'


class Cron(object):
    """
    """

    def is_root_present(self):
        if not os.path.isdir(CRON_DIR):
            print('*** ERROR *** There is no cron path at {}'.format(CRON_DIR))
        else:
            if os.path.isfile(CRON_DIR + '/root'):
                pass
        pass

    def add_weekly_reboot(self):
        pass

if __name__ == "__main__":
    print(' Running crontab.py ...')
    l_boot = Cron()
    l_boot.add_weekly_reboot()
    print(' Finished crontab.py\n')

#  ## END DBK
