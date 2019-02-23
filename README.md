What do the files do:
-- generatePPkeys.py: This program generates public and private keys. It will ask the user for the primes used and write the keys to public-key.txt & private-key.txt. It was just included incase you want to change the keys provided.

-- public-key.txt : Has Bob's public key generated with p = 131 & q = 71. Can be changed with generatePPkeys.py. Is used to encrypt the keys.

-- private-key.txt : Has Bob's private key generated with p = 131 & q = 71. Can be changed with generatePPkeys.py. Is used to decrypt the keys.

-- asymmetrickey_encr.py : Is a python program that needs public-key.txt and <keys>.txt to generate wrapped keys which is written to wrapped-keys.cipher.

-- asymmetrickey_decr.py : Is a python program that needs private-key.txt and <wrapped-keys file>.cipher to decrypt the unwrapped.txt file.

-- transposition-encr.py : Is a python program that takes in <plain-text>.txt file and <keys>.txt file to encrypt the message in <plain-text>.txt and creates a new file with the encrypted message called <plain-text>.cipher.

-- transposition-decr.py : Is a python program that takes in <plain-text>.cipher file and <keys>.txt file to decrypt the encrypter message in <plain-text>.cipher and creates a new file with the encrypted message called <plain-text>-decrypted.txt with the original messgae capatilized and without spaces.

=====
How to run each program:

[Optional to create new public & private keys]
generatePPkeys.py:
-It will ask the user for p and q values
-It will produce files called public-key.txt and private-key.txt.

asymmetrickey_encr.py:
- [in the command line pass]: python3 asymmetrickey_encr.py public-key.txt <keys>.txt
- Will produce: wrapped-keys.cipher with the encrypted keys

asymmetrickey_decr.py:
- [in the command line pass]: python3 asymmetrickey_decr.py private-key.txt wrapped-keys.cipher
- Will produce: unwrapped.txt with decrypted keys

transposition-encr.py:
- [in the command line pass]: python3 transposition-encr.py <text-to-encrypt>.txt <keys>.txt
- Will produce: Encrypted file called <text-to-encrypt>.cipher

transposition-decr.py:
- [in the command line pass]: python transposition-decr.py <text-to-decrypt>.cipher <keys.txt>
- Will produce: Decrypted file called <text-to-decrypt>-decrypted.txt
