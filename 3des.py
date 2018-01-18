
import time
from Crypto.Cipher import DES3
from Crypto import Random

key = 'Sixteen byte key'
iv = Random.new().read(DES3.block_size) #DES3.block_size==8
cipher_encrypt = DES3.new(key, DES3.MODE_OFB, iv)
plaintext = "a" * 131072


start__time_3des = time.time()

encrypted_text = cipher_encrypt.encrypt(plaintext)

end_time_3des = time.time()


exec_time_3des = end_time_3des - start__time_3des
print("Execution time : " + str(exec_time_3des))


"""
For MODE_ECB, MODE_CBC, and MODE_OFB, plaintext length (in bytes) must be a multiple of block_size.
For MODE_CFB, plaintext length (in bytes) must be a multiple of segment_size/8.
For MODE_CTR, plaintext can be of any length.
For MODE_OPENPGP, plaintext must be a multiple of block_size, unless it is the last chunk of the message.
key size (must be either 16 or 24 bytes long)
"""
"""
https://pythonhosted.org/pycrypto/Crypto.Cipher.DES3-module.html
https://en.wikipedia.org/wiki/Block_cipher_mode_of_operation
"""