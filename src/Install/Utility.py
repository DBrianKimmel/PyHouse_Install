"""
@name:      PyHouse_Install/src/Install/Utility.py
@author:    D. Brian Kimmel
@contact:   D.BrianKimmel@gmail.com
@copyright: (c) 2015-2015 by D. Brian Kimmel
@license:   MIT License
@note:      Created on Oct 13, 2015
@Summary:

"""

# Import system type stuff
import os


class Directories(object):
    """
    """

    def is_dir(self, p_path):
        return os.path.isdir(p_path)

    def MakeDir(self, p_dir_name):
        pass


# ## END DBK
