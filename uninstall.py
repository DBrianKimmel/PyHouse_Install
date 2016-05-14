"""
@name:      PyHouse_Install/src/uninstall.py
@author:    D. Brian Kimmel
@contact:   D.BrianKimmel@gmail.com
@copyright: (c) 2016-2016 by D. Brian Kimmel
@license:   MIT License
@note:      Created Jan 12, 2016
@Summary:

"""


import subprocess

def cleanup():
    #  sudo deluser pyhouse
    subprocess.call('sudo', 'deluser', 'pyhouse')

    #  sudo rm -rf /home/pyhouse/
    subprocess.call('sudo', 'rm', '-rf', '/home/pyhouse')

    #  sudo rm -rf PyHouse_Install
    subprocess.call('sudo', 'rm', '-rf', 'PyHouse_Install')


if __name__ == "__main__":
    print('Setup cleanup of PyHouse_Install.\n')
    cleanup()

#  ## END DBK
