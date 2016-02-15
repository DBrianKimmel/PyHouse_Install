"""
-*- test-case-name:  path -*-

@name:  name
@author:  D. Brian Kimmel
@contact:  d.briankimmel@gmail.com
@copyright:  2016 by D. Brian Kimmel
@date:  Created on Jan 20, 2016
@licencse:  MIT License
@summary:


Created on Jan 20, 2016

This is to document the Mosquitto installation on the NUC computers.
Requires mosquitto 1.4.7 or later

"""

# Import system things
import os


ETC_DIR = '/etc/mosquitto/'
LOG_DIR = '/var/log/mpsquitto/'


class Config(object):
    """
    """

    def __init__(self):
        pass

    def create_certs_dir(self):
        l_dir = ETC_DIR + 'certs'
        if not os.path.isdir(l_dir):
            print('Creating a directory {}'.format(l_dir))
            os.makedirs(l_dir)

    def do_config(self):
        self.create_certs_dir()


if __name__ == "__main__":
    print('\nRunning  Install/mosquitto.py ...')
    l_config = Config()
    l_config.do_config()
    print('Finished mosquitto.py\n')

# ## END DBK
