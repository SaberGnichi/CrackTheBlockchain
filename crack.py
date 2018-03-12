import ecdsa
import ecdsa.der
import ecdsa.util
import hashlib
import os
import re
import struct
import sys
import argparse

b58 = '123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'

def base58encode(n):
    result = ''
    while n > 0:
        result = b58[n%58] + result
        n /= 58
    return result

def base256decode(s):
    result = 0
    for c in s:
        result = result * 256 + ord(c)
    return result

def countLeadingChars(s, ch):
    count = 0
    for c in s:
        if c == ch:
            count += 1
        else:
            break
    return count

def base58CheckEncode(version, payload):
    s = chr(version) + payload
    checksum = hashlib.sha256(hashlib.sha256(s).digest()).digest()[0:4]
    result = s + checksum
    leadingZeros = countLeadingChars(result, '\0')
    return '1' * leadingZeros + base58encode(base256decode(result))

def privateKeyToWif(key_hex):    
    return base58CheckEncode(0x80, key_hex.decode('hex'))
    
def privateKeyToPublicKey(s):
    sk = ecdsa.SigningKey.from_string(s.decode('hex'), curve=ecdsa.SECP256k1)
    vk = sk.verifying_key
    return ('\04' + sk.verifying_key.to_string()).encode('hex')
    
def pubKeyToAddr(s):
    ripemd160 = hashlib.new('ripemd160')
    ripemd160.update(hashlib.sha256(s.decode('hex')).digest())
    return base58CheckEncode(0, ripemd160.digest())

def keyToAddr(s):
    return pubKeyToAddr(privateKeyToPublicKey(s))

def keyToSignature(s):
    sk = ecdsa.SigningKey.from_string(s.decode('hex'), curve=ecdsa.SECP256k1)
    return sk.verifying_key.to_string().encode('hex')[:64]

def lookup(key):
    address = keyToAddr(key)
    r = keyToSignature(key)
    if address in addresses:
        print 'founded / pwned : ' + key
    if r in rs:
        print 'founded / pwned : ' + key

def lookup_in_addresses(key):
    address = keyToAddr(key)
    if address in addresses:
        print 'founded / pwned : ' + key

def lookup_in_rs(key)
    r = keyToSignature(key)
    if r in rs:
        print 'founded / pwned : ' + key

def brainwallet1(passphrase):
    return hashlib.sha256(passphrase).hexdigest()


#print "Private Key     : %s " % privateKeyToWif(sys.argv[1])
#print "Address         : %s " % keyToAddr(sys.argv[1])

description = ''
parser = argparse.ArgumentParser(description=description)
parser.add_argument('-i','--images', help='the location of the file that contains the endpoints (addresses or Rs)', required=True)
parser.add_argument('-t','--type', help='the type of the endpoints addresses or signatures', required=True)
parser.add_argument('-w','--way', help='the way to generate private keys it can be equal to: random, fromfile or brainwallet', required=True)
parser.add_argument('-f','--file', help='the extra file in the case if it needed it can be the file that contains passphrases or the file that contains private keys', default='')
parser.add_argument('-tr','--tries', help='the number of tries if needed', default=1000)

args = vars(parser.parse_args())

imagesfile = args['images']
type = args['type']
way = args['way']
file = args['file']
tries = args['tries']
tries = int(tries)
addresses = []
rs = []
if type == 'addresses':
    with open(imagesfile, 'r') as ins:
        for line in ins:
            line = line.strip()
            addresses.append(line)
elif type == 'signatures':
    with open(imagesfile, 'r') as ins:
        for line in ins:
            line = line.strip()
            rs.append(line)
else:
    print 'Invalid type of endpoints'
    exit
if way == 'random':
    j = 0
    while j < tries:
        print j
        private_key = os.urandom(32).encode('hex')
        lookup(private_key)
        j += 1
elif way == 'fromfile':
    with open(file, 'r') as keys:
        for private_key in keys:
            private_key = private_key.strip()
            lookup(private_key)
elif way == 'brainwallet':
    with open(file, 'r') as passphrases:
        for passphrase in passphrases:
            passphrase = passphrase.strip()
            private_key = brainwallet1(passphrase)
            lookup(private_key)
