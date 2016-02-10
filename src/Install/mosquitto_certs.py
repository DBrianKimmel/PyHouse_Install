"""
@name:      PyHouse_Install/src/Install/mosquitto_certs.py
@author:    D. Brian Kimmel
@contact:   D.BrianKimmel@gmail.com
@copyright: (c) 2016-2016 by D. Brian Kimmel
@license:   MIT License
@note:      Created Jan 24, 2016
@Summary:

"""

#  Import system stuff
#  import getpass
#  import os
import subprocess

#  Import PyHouse stuff
from Install.Utility import Utilities

RDN_CN = 'PyHouse.Org'
RDN_L = 'Beverly Hills'
RDN_ST = 'Florida'
RDN_C = 'US'
RDN_OU = 'IT_Devel'
RDN_O = 'PyHouse'

CERT_DIR = '/etc/pyhouse/ca_certs/'
EMAIL = 'NoReply@PyHouse.org'
DAYS = (365 * 8) + 2  #  8 years (Leap Years included)
MD = '-sha512'
KEY_BITS = 2048


class Certs(object):
    """
    """

    def create_client(self, p_file, p_out, p_addresslist):
        print("--- Creating and signing client certificate")
        subprocess.call(['openssl', 'x509', '-req', MD,
                        '-in', '$CLIENT.csr',
                        '-CA', p_file + '.crt',
                        '-CAkey', p_file + '.key',
                        '-CAcreateserial',
                        '-CAserial', "${DIR}/ca.srl",
                        '-out', p_out + '.crt',
                        '-days', DAYS,
                        '-extfile', p_addresslist,
                        '-extensions', 'JPMclientextensions'])
        subprocess.call(['chmod', '444', p_out + '.crt'])

    def step_1_create_root_key(self):
        """
        openssl genrsa
            -out rootCA.key
            2048


        # Create un-encrypted (!) key
        openssl req
            -newkey rsa:${keybits}
            -x509
            -nodes $defaultmd
            -days $days
            -extensions v3_ca
            -keyout $CACERT.key
            -out $CACERT.crt
            -subj "${CA_DN}"
        echo "Created CA certificate in $CACERT.crt"

        openssl x509
            -in $CACERT.crt
            -nameopt multiline
            -subject -noout
        chmod 400 $CACERT.key
        chmod 444 $CACERT.crt
        chown $MOSQUITTOUSER $CACERT.*
        echo "Warning: the CA key is not encrypted; store it safely!"

        """
        print('  Generating Private Root Key')
        subprocess.call(['sudo',
                         'openssl', 'genrsa',
                         '-out', CERT_DIR + 'rootCA.key',
                         KEY_BITS
                         ])
        subprocess.call(['sudo',
                         'openssl', 'genrsa',
                         '-out', CERT_DIR + 'server.key',
                         '2048'
                         ])
        subprocess.call(['sudo',
                         'openssl', 'genrsa',
                         '-out', CERT_DIR + 'client.key',
                         KEY_BITS
                         ])
        #  print(' ')

    def step_2_sign_root_key(self):
        """
        openssl req -x509 -new -nodes -key rootCA.key -days 1024 -out rootCA.pem
        """
        print('  Signing Private Root Key')
        subprocess.call(['sudo',
                         'openssl', 'req',
                         '-x509', '-new', '-nodes',
                         '-key', CERT_DIR + 'rootCA.key',
                         '-days', '1024',
                         '-out', CERT_DIR + 'rootCA.pem',
                         '-subj',
                            '/L=' + RDN_L +
                            '/ST=' + RDN_ST +
                            '/C=' + RDN_C +
                            '/O=' + RDN_O +
                            '/OU=' + RDN_OU +
                            '/CN=' + RDN_CN
                          ])
        #  print(' ')

    def step_3_generate_csr(self):
        """
        openssl req -new -key server.key -out server.csr
        """
        print('  Generate a certificate Signing Request (CSR).')
        subprocess.call(['sudo',
                         'openssl', 'req',
                         '-new',
                         '-key', CERT_DIR + 'server.key',
                         '-out', CERT_DIR + 'server.csr',
                        '-subj',
                            '/L=' + RDN_L +
                            '/ST=' + RDN_ST +
                            '/C=' + RDN_C +
                            '/O=' + RDN_O +
                            '/OU=' + RDN_OU +
                            '/CN=' + RDN_CN
                          ])
        subprocess.call(['sudo',
                         'openssl', 'req',
                         '-new',
                         '-key', CERT_DIR + 'client.key',
                         '-out', CERT_DIR + 'client.csr',
                        '-subj',
                            '/L=' + RDN_L +
                            '/ST=' + RDN_ST +
                            '/C=' + RDN_C +
                            '/O=' + RDN_O +
                            '/OU=' + RDN_OU +
                            '/CN=' + RDN_CN
                          ])
        #  print(' ')

    def step_4_remove_passphrase(self):
        print('  GRemove Passphrase.')
        #  print(' ')

    def create_server_crt(self):
        """
        sudo openssl x509 -req -days 365
                    -in "/etc/[webserver]/ssl/example.csr" \
                    -signkey "/etc/[webserver]/ssl/example.key"  \
                    -out "/etc/[webserver]/ssl/example.crt"
        """
        print('  Generate a Self Signed Certificate.')
        subprocess.call(['sudo',
                         'openssl', 'x509',
                         '-req',
                         '-days', str(DAYS),
                         '-in', CERT_DIR + 'server.csr',
                         '-signkey', CERT_DIR + 'rootCA.key',
                         '-out', CERT_DIR + 'server.crt'
                          ])

    def step_5_generate_self_signed_certificate(self):
        """
        sudo openssl x509 -req -days 365
                    -in "/etc/[webserver]/ssl/example.csr" \
                    -signkey "/etc/[webserver]/ssl/example.key"  \
                    -out "/etc/[webserver]/ssl/example.crt"
        """
        print('  Generate a Server Self Signed Certificate.')
        subprocess.call(['sudo', 'openssl', 'x509',
                         '-req',
                         '-days', str(DAYS),
                         '-in', CERT_DIR + 'server.csr',
                         '-signkey', CERT_DIR + 'rootCA.key',
                         '-out', CERT_DIR + 'server.crt'
                          ])
        print('  Generate a Client Self Signed Certificate.')
        subprocess.call(['sudo', 'openssl', 'x509',
                         '-req',
                         '-extensions', 'PyHouseExtensions',
                         '-CAcreateserial',
                         '-days', str(DAYS),
                         '-in', CERT_DIR + 'client.csr',
                         '-signkey', CERT_DIR + 'rootCA.key',
                         '-out', CERT_DIR + 'client.crt'
                          ])
        #  print(' ')

    def create_certs_dir(self):
        pass

    def create_certs(self):
        self.step_1_create_root_key()
        self.step_2_sign_root_key()
        self.step_3_generate_csr()
        self.step_4_remove_passphrase()
        self.step_5_generate_self_signed_certificate()

    def create_mosquitto(self):
        print('  Creating Mosquitto TLS files...')
        self.create_server_crt()

if __name__ == "__main__":
    print(' Running  Install/mosquitto_certs.py ...')
    Utilities.must_not_be_root()
    #  print(getpass.getuser())
    l_api = Certs()
    l_api.create_certs()
    print(' Finished mosquitto_certs.py\n')

"""
#!/bin/bash

# Create CA key-pair and server key-pair signed by CA

# Usage:
#       ./generate-CA.sh                creates ca.crt and server.{key,crt}
#       ./generate-CA.sh hostname       creates hostname.{key,crt}
#       ./generate-CA.sh client email   creates email.{key,crt}
#
# Set the following optional environment variables before invocation
# to add the specified IP addresses and/or hostnames to the subjAltName list
# These contain white-space-separated values
#
#       IPLIST="172.13.14.15 192.168.1.1"
#       HOSTLIST="a.example.com b.example.com"

set -e
export LANG=C
kind=server
if [ $# -ne 2 ]; then
        kind=server
        host=$(hostname -f)
        if [ -n "$1" ]; then
                host="$1"
        fi
else
        kind=client
        CLIENT="$2"
fi

[ -z "$USER" ] && USER=root

DIR=${TARGET:='.'}
# A space-separated list of alternate hostnames (subjAltName)
# may be empty ""
ALTHOSTNAMES=${HOSTLIST}
ALTADDRESSES=${IPLIST}
CA_ORG='/O=OwnTracks.org/OU=generate-CA/emailAddress=nobody@example.net'
CA_DN="/CN=An MQTT broker${CA_ORG}"
CACERT=${DIR}/ca
SERVER="${DIR}/${host}"
SERVER_DN="/CN=${host}$CA_ORG"
keybits=2048
openssl=$(which openssl)
MOSQUITTOUSER=${MOSQUITTOUSER:=$USER}

# Signature Algorithm. To find out which are supported by your
# version of OpenSSL, run `openssl dgst -help` and set your
# signature algorithm here. For example:
#
#       defaultmd="-sha256"
#
defaultmd="-sha512"

function maxdays() {
        nowyear=$(date +%Y)
        years=$(expr 2032 - $nowyear)
        days=$(expr $years '*' 365)
        echo $days
}

function getipaddresses() {
# returns the following on my laptop:
#    192.168.1.91
#    2604:8800:100:8268:4225:c2ff:fee4:fcd8
#    2604:8800:100:8268:34b9:7ab0:4941:2bd0
#    fe80::4225:c2ff:fee4:fcd8

        /sbin/ifconfig |
                grep -v tunnel |
                sed -En '/inet6? /p' |
                sed -Ee 's/inet6? (addr:)?//' |
                awk '{print $1;}' |
                sed -e 's/[%/].*//' |
                egrep -v '(::1|127\.0\.0\.1)'   # omit loopback to add it later
}

function addresslist() {
        ALIST=""
        for a in $(getipaddresses); do
                ALIST="${ALIST}IP:$a,"
        done
        ALIST="${ALIST}IP:127.0.0.1,IP:::1,"
        for ip in $(echo ${ALTADDRESSES}); do
                ALIST="${ALIST}IP:${ip},"
        done
        for h in $(echo ${ALTHOSTNAMES}); do
                ALIST="${ALIST}DNS:$h,"
        done
        ALIST="${ALIST}DNS:localhost"
        echo $ALIST
}

days=$(maxdays)
if [ -n "$CAKILLFILES" ]; then
        rm -f $CACERT.??? $SERVER.??? $CACERT.srl
fi
if [ ! -f $CACERT.crt ]; then
        #    ____    _
        #   / ___|  / \
        #  | |     / _ \
        #  | |___ / ___ \
        #   \____/_/   \_\
        #
        # Create un-encrypted (!) key
        $openssl req -newkey rsa:${keybits} -x509 -nodes $defaultmd -days $days -extensions v3_ca -keyout $CACERT.key -out $CACERT.crt -subj "${CA_DN}"
        echo "Created CA certificate in $CACERT.crt"
        $openssl x509 -in $CACERT.crt -nameopt multiline -subject -noout
        chmod 400 $CACERT.key
        chmod 444 $CACERT.crt
        chown $MOSQUITTOUSER $CACERT.*
        echo "Warning: the CA key is not encrypted; store it safely!"
fi

if [ $kind == 'server' ]; then
        #   ____
        #  / ___|  ___ _ ____   _____ _ __
        #  \___ \ / _ \ '__\ \ / / _ \ '__|
        #   ___) |  __/ |   \ V /  __/ |
        #  |____/ \___|_|    \_/ \___|_|
        #
        if [ ! -f $SERVER.key ]; then
                echo "--- Creating server key and signing request"
                $openssl genrsa -out $SERVER.key $keybits
                $openssl req -new $defaultmd \
                        -out $SERVER.csr \
                        -key $SERVER.key \
                        -subj "${SERVER_DN}"
                chmod 400 $SERVER.key
                chown $MOSQUITTOUSER $SERVER.key
        fi

        if [ -f $SERVER.csr -a ! -f $SERVER.crt ]; then
                # There's no way to pass subjAltName on the CLI so
                # create a cnf file and use that.
                CNF=`mktemp /tmp/cacnf.XXXXXXXX` || { echo "$0: can't create temp file" >&2; exit 1; }
                sed -e 's/^.*%%% //' > $CNF <<\!ENDconfig
                %%% [ JPMextensions ]
                %%% basicConstraints        = critical,CA:false
                %%% nsCertType              = server
                %%% keyUsage                = nonRepudiation, digitalSignature, keyEncipherment
                %%% nsComment               = "Broker Certificate"
                %%% subjectKeyIdentifier    = hash
                %%% authorityKeyIdentifier  = keyid,issuer:always
                %%% subjectAltName          = $ENV::SUBJALTNAME
                %%% # issuerAltName           = issuer:copy
                %%% ## nsCaRevocationUrl       = http://mqttitude.org/carev/
                %%% ## nsRevocationUrl         = http://mqttitude.org/carev/
                %%% certificatePolicies     = ia5org,@polsection
                %%%
                %%% [polsection]
                %%% policyIdentifier        = 1.3.5.8
                %%% CPS.1                   = "http://localhost"
                %%% userNotice.1            = @notice
                %%%
                %%% [notice]
                %%% explicitText            = "This CA is for a local MQTT broker installation only"
                %%% organization            = "OwnTracks"
                %%% noticeNumbers           = 1
!ENDconfig

                SUBJALTNAME="$(addresslist)"
                export SUBJALTNAME              # Use environment. Because I can. ;-)
                echo "--- Creating and signing server certificate"
                $openssl x509 -req $defaultmd \
                        -in $SERVER.csr \
                        -CA $CACERT.crt \
                        -CAkey $CACERT.key \
                        -CAcreateserial \
                        -CAserial "${DIR}/ca.srl" \
                        -out $SERVER.crt \
                        -days $days \
                        -extfile ${CNF} \
                        -extensions JPMextensions
                rm -f $CNF
                chmod 444 $SERVER.crt
                chown $MOSQUITTOUSER $SERVER.crt
        fi
else
        #    ____ _ _            _
        #   / ___| (_) ___ _ __ | |_
        #  | |   | | |/ _ \ '_ \| __|
        #  | |___| | |  __/ | | | |_
        #   \____|_|_|\___|_| |_|\__|
        #

        if [ ! -f $CLIENT.key ]; then
                echo "--- Creating client key and signing request"
                $openssl genrsa -out $CLIENT.key $keybits
                CNF=`mktemp /tmp/cacnf-req.XXXXXXXX` || { echo "$0: can't create temp file" >&2; exit 1; }
                # Mosquitto's use_identity_as_username takes the CN attribute
                # so we're populating that with the client's name
                sed -e 's/^.*%%% //' > $CNF <<!ENDClientconfigREQ
                %%% [ req ]
                %%% distinguished_name  = req_distinguished_name
                %%% prompt                      = no
                %%% output_password             = secret
                %%%
                %%% [ req_distinguished_name ]
                %%% # O                       = OwnTracks
                %%% # OU                      = MQTT
                %%% # CN                      = Suzie Smith
                %%% CN                        = $CLIENT
                %%% # emailAddress            = $CLIENT
!ENDClientconfigREQ

                $openssl req -new $defaultmd \
                        -out $CLIENT.csr \
                        -key $CLIENT.key \
                        -config $CNF
                chmod 400 $CLIENT.key
        fi

        if [ -f $CLIENT.csr -a ! -f $CLIENT.crt ]; then
                CNF=`mktemp /tmp/cacnf-cli.XXXXXXXX` || { echo "$0: can't create temp file" >&2; exit 1; }
                sed -e 's/^.*%%% //' > $CNF <<\!ENDClientconfig
                %%% [ JPMclientextensions ]
                %%% basicConstraints        = critical,CA:false
                %%% subjectAltName          = email:copy
                %%% nsCertType              = client,email
                %%% extendedKeyUsage        = clientAuth,emailProtection
                %%% keyUsage                = digitalSignature, keyEncipherment, keyAgreement
                %%% nsComment               = "Client Broker Certificate"
                %%% subjectKeyIdentifier    = hash
                %%% authorityKeyIdentifier  = keyid,issuer:always

!ENDClientconfig

                SUBJALTNAME="$(addresslist)"
                export SUBJALTNAME              # Use environment. Because I can. ;-)
                echo "--- Creating and signing client certificate"
                $openssl x509 -req $defaultmd \
                        -in $CLIENT.csr \
                        -CA $CACERT.crt \
                        -CAkey $CACERT.key \
                        -CAcreateserial \
                        -CAserial "${DIR}/ca.srl" \
                        -out $CLIENT.crt \
                        -days $days \
                        -extfile ${CNF} \
                        -extensions JPMclientextensions
                rm -f $CNF
                chmod 444 $CLIENT.crt
        fi
fi

"""
#  ## END DBK
