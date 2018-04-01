input_file = open('audio.mp3','rb')
output_file = open('audio_output.mp3','wb')

for line in input_file.readlines():
	output_file.write(line)
	#print(line)
	#break

input_file.close()
output_file.close()