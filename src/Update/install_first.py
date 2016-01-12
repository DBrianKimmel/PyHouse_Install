"""
@name:      PyHouse_Install/src/Install/install_first.py
@author:    D. Brian Kimmel
@contact:   D.BrianKimmel@gmail.com
@copyright: (c) 2015-2015 by D. Brian Kimmel
@license:   MIT License
@note:      Created on Oct 16, 2015
@Summary:   Install everything on a new jessie system

Must be run as root (sudo)

"""

class Hostname(object):
    """
    """
    
    HOSTNAMEFILE = '/etc/hostname'

    def change(self, p_name):
        CURRENT_HOSTNAME=$(cat /etc/hostname | tr -d " \t\n\r")
        NEW_HOSTNAME=$HOST_NAME
        echo $HOST_NAME > HOSTNAMEFILE
        sed -i "s|127.0.1.1.*$CURRENT_HOSTNAME|127.0.1.1\t$HOST_NAME|g" $HOSTSFILE
        pass


if __name__ == "__main__":
    print('Running Update/install_first.py ...')
    Hostname().change('pi2-01')
    print('Finished install_first.py\n')

# ## END DBK
