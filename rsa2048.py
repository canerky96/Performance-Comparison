import time
from Crypto.PublicKey import RSA
from Crypto import Random

random_generator = Random.new().read
key = RSA.generate(2048, random_generator)
pub_key = key.publickey()

text = '1' * 131072

start_time = time.time()

enc_data = pub_key.encrypt(int(text),32)

end_time = time.time()

print ("Execution time : " + str(end_time - start_time ))