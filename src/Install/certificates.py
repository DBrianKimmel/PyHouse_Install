"""
-*- test-case-name:  path -*-

@name:      PyHouse_Install/src/install/certificates.py
@author:    D. Brian Kimmel
@contact:   d.briankimmel@gmail.com
@copyright: 2016-2016 by D. Brian Kimmel
@date:      Created on Jan 21, 2016
@licencse:  MIT License
@summary:


"""


class Certs(object):

    def root_cert(self):
        """
        openssl genrsa -out rootCA.key 2048

        this will make rootCAA.key - a private key
        """

    def Pem(self):
        """
        openssl req -x509 -new -nodes -key rootCA.key -days 1024 -out rootCA.pem
        """

    def Request(self):
        """
        openssl req -new -key server.key -out server.csr
        """

# ## END DBK
