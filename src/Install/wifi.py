"""
@name:      /home/briank/workspace/PyHouse_Install/src/Install/wifi.py
@author:    D. Brian Kimmel
@contact:   D.BrianKimmel@gmail.com
@copyright: (c) 2016-2016 by D. Brian Kimmel
@license:   MIT License
@note:      Created Feb 4, 2016
@Summary:   Fix the WiFi adapter

On Raspis the wireless adapter sometimes goes to sleep and takes almost a minute to wake up
to an incoming connection.  This attempts to fix the problem for the WIFI adapters I have.

"""

#  Import system stuff
import subprocess


class WiFi8192cu(object):
    """
    """

    def add_file(self):
        l_file = '/etc/modprobe.d/8192cu.conf'
        l_text = 'options 8192cu rtw_power_mgnt=0 rtw_enusbss=0\n'
        pass


class WiFi(object):
    """
    """

    def find_modules(self):
        l_modules = subprocess.check_output(['sudo', 'lsmod']).decode('utf-8')
        l_lines = l_modules.split('\n')
        for l_line in l_lines:
            print(l_line)
            if l_line.startswith('8192cu'):
                print('  WiFi module is 8192cu - Edimax')


if __name__ == "__main__":
    print(' Running  Install/wifi.py ...')
    l_api = WiFi()
    l_api.find_modules()
    print(' Finished wifi.py\n')

#  ## END DBK
