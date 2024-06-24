import ffmpeg


input_file = 'input.mp4'
output_file = 'output.mp3'

# Extract audio from the video
ffmpeg.input(input_file).output(output_file, format='mp3').run()

print('Audio extracted successfully!')
