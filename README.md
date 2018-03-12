# CrackTheBlockchain

The private key is the "ticket" that allows someone to spend bitcoins and and the unique evidence to proof address/money ownership , it is important that these are kept secure. but if a hacker was able to steal or crack the private key then he can steal all the money in a bitcoin address/wallet

this is a simple tool that builded to combine many ways & methods for cracking private keys (offline attacks)

usage: crack.py [-h] -i IMAGES -t TYPE -w WAY [-f FILE] [-tr TRIES]

optional arguments:
  -h, --help            show this help message and exit
  -i IMAGES, --images IMAGES
                        the location of the file that contains the endpoints
                        (addresses or Rs)
  -t TYPE, --type TYPE  the type of the endpoints addresses or signatures
  -w WAY, --way WAY     the way to generate private keys it can be equal to:
                        random, fromfile or brainwallet
  -f FILE, --file FILE  the extra file in the case if it needed it can be the
                        file that contains passphrases or the file that
                        contains private keys
  -tr TRIES, --tries TRIES
                        the number of tries if needed

In the way brainwallet:

Brain wallets refer to private cryptographic keys that are despotically derived from passwords. Alternatively to other means for managing bitcoin’s cryptographic keys, such as securing them on a PC, or hardware wallets, brain wallets are much more convenient to users who can spend their coins via simply entering their passwords. Due to the fact that they don’t involve permanent storage of their private keys on a device, brain wallets cannot be phished by malware. However, a brain wallet is a very insecure way to store bitcoins, as an attacker who can successfully guess a user’s password, can steal them instantly.

Attackers successfully guessing a password can test if it matches any brain wallet via searching for usage of the derived public key on the blockchain, which records all transactions.

command line example:
python crack.py --way barinwallet --type addresses --images list1.txt --file passwords.txt

WHERE : 
      list1.txt a file that contains the addresses extracted from first 100000 block from the blockchain
      passwords.txt a file that contains passwords

The way random is very similar to the way brainwallet but instead of extracting private keys from SHA256 or any other deterministic trapdoor function the tool generate a private keys randomly based on the standard function random

command line example:
python crack.py --way random --type addresses --images list1.txt --tries 100000

In the way fromfile the tool read private keys from a text file directly
command line example:
python crack.py --way random --type addresses --images list1.txt --file keys.txt


NOTE THAT

* list1.txt contains only the addresses extracted from the first 100 000 block from the blockchain (addresses with a balance > 0)
* to launch an effective brute force attack you should download the full blockchain not only some blocks
* this tool is just a proof
* you don’t have to be a jerk


PROOF:
1)
private key (hex) : 0000000000000000000000000000000000000000000000000000000000000001
Private Key (base58) : 5HpHagT65TZzG1PH3CSu63k8DbpvD8s5ip4nEB3kEsreAnchuDf 
Address : 1EHNa6Q4Jz2uvNExL497mE43ikXhwF6kZm

https://blockchain.info/address/1EHNa6Q4Jz2uvNExL497mE43ikXhwF6kZm

No.Transactions 1201
Total Received 	$ 46,351.16
balance         $ 0

2) brainwallet password
private key (hex) : 5E884898DA28047151D0E56F8DC6292773603D0D6AABBDD62A11EF721D1542D8
private key (base58) : 5JXvHQfGHxUffo8BLRG1RBecRCZ2Jygtx5cNSiZoyk5Zcmhsdso
address : 16ga2uqnF1NqpAuQeeg7sTCAdtDUwDyJav

https://blockchain.info/address/16ga2uqnF1NqpAuQeeg7sTCAdtDUwDyJav

No.Transactions 45010
Total Received 	$ 3,373.91
Final Balance 	$ 0.00
