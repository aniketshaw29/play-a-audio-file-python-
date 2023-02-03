#pip install pydub

from pydub import AudioSegment
from pydub.playback import play

filename = "D:/Documents/4_Projects/2_Uploaded_in_github/play-a-audio-file(python)/BadtameezDil.mp3"
#The pydub library can play many audio formats, including MP3, WAV, and AIFF, among others.

try:
    sound = AudioSegment.from_mp3(filename)
    play(sound)
except FileNotFoundError:
    print("Error: The specified file could not be found. Please make sure the file path is correct.")
except PermissionError:
    print("Error: The specified file could not be written to. Please make sure you have write permissions for the file.")