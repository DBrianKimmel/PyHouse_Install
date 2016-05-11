"""
@name:      PyHouse_Install/src/Install/hostname.py
@author:    D. Brian Kimmel
@contact:   D.BrianKimmel@gmail.com
@copyright: (c) 2016-2016 by D. Brian Kimmel
@license:   MIT License
@note:      Created Jan 22, 2016
@Summary:   Set up the computers hostname

Hostname must be set up properly so that X509 certificates woll work as they should.

"""

#  Import system stuff
import os


class Private(object):
    """ This will get information from the file /etc/pyhouse/.private.config
    """

    def if_exists(self):
        return False


class Hostname(object):
    """
    """

    def get_existing(self):
        l_host = os.uname()[1]
        print('  Hostname: {}'.format(l_host))


if __name__ == "__main__":
    print(' Running hostname.py ...')
    l_host = Hostname()
    l_host.get_existing()
    print(' Finished hostname.py\n')

#  ## END DBK
