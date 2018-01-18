
import time
from Crypto.Cipher import DES

des = DES.new('01234567', DES.MODE_ECB) # 56bit (7byte) key
text = "a" * 131072 # generete 128 kilobyte data

start_time_des = time.time()

cipher_text = des.encrypt(text)

end_time_des = time.time()

print("Execution time of DES: " + str(end_time_des-start_time_des))
