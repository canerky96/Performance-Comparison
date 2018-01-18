
from Crypto.PublicKey import RSA
from Crypto import Random

random_generator = Random.new().read
key = RSA.generate(1024, random_generator)
pub_key = key.publickey()

text = '1' * 131072 # 128 kilobyte data
enc_data = pub_key.encrypt(int(text),32)