from cryptography.fernet import Fernet
import time

cipher_key = Fernet.generate_key()
cipher = Fernet(cipher_key)

input_file = open('audio.mp3','rb')
output_file = open('audio_output_encrypted.mp3','wb')

print('Encrypting.....')

for line in input_file.readlines():
	encrypted_line = cipher.encrypt(line)
	output_file.write(encrypted_line+b'\n')

print('Encryption Done')
input_file.close()
output_file.close()

input_file = open('audio_output_encrypted.mp3','rb')
output_file = open('audio_output_decrypted.mp3','wb')

print('Decrypting.....')

for line in input_file.readlines():
	decrypted_line = cipher.decrypt(line[:-1])
	output_file.write(decrypted_line)

print('Decryption Done')
input_file.close()
output_file.close()