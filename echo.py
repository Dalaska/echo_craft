# !pip install TTS  # Run this in your environment if TTS is not installed

from TTS.api import TTS

# Load a Coqui TTS model that uses the VITS architecture from Hugging Face.
# "tts_models/en/ljspeech/vits" is one example of a high-quality VITS model.
tts = TTS("tts_models/en/ljspeech/vits")

# Define the text you want to convert to speech.
input_text = "Hello This is an example of using the Coqui TTS V2 model from Hugging Face."

# Convert the text to speech and save as a WAV file.
tts.tts_to_file(text=input_text, file_path="output.wav")

print("Speech synthesis complete! Check the 'output.wav' file.")
