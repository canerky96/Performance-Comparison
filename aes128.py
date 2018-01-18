from Crypto.Cipher import AES

key = 'a' * 16 #128 bit key
IV = 16 * '\x00'           # Initialization vector: discussed later
mode = AES.MODE_CBC
encryptor = AES.new(key, mode, IV=IV)

text = 'a' * 131072 # 128 kilobyte data
ciphertext = encryptor.encrypt(text)