"""
@name:      PyHouse_Install/src/Install/private.py
@author:    D. Brian Kimmel
@contact:   D.BrianKimmel@gmail.com
@copyright: (c) 2016-2016 by D. Brian Kimmel
@license:   MIT License
@note:      Created May 13, 2016
@Summary:   Create .private

Create the /etc/pyhouse/.private.yaml file that will hold the secret information used by the pyhouse system.

HOSTNAME: hostname
MQTT: true
NODE_RED: false


"""

import yaml


Y_FILE = '/etc/pyhouse/.private.yaml'

class Private(object):
    def __init__(self):
        self.hostname = None


class API(object):
    """
    """

    def __init__(self):
        self.m_private = Private()
        self.read_yaml()

    def read_yaml(self):
        l_file = open(Y_FILE)
        #  use safe_load instead load
        self.m_private = yaml.safe_load(l_file)
        l_file.close()

    def write_yaml(self):
        l_file = open('newtree.yaml', "w")
        yaml.dump(self.m_private, l_file)
        l_file.close()


if __name__ == '__main--':
    API()

#  ## END DBK
