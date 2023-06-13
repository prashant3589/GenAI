# Note: you need to be using OpenAI Python v0.27.0 for the code below to work
import openai
openai.api_key='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'

audio_file= open("C:/GenerativeAI/audio-summary/data/sampleaudio.mp3", "rb")
transcript = openai.Audio.transcribe("whisper-1", audio_file)
text = transcript["text"]
response = openai.Completion.create(
  model="text-davinci-003",
  prompt="Summarize this :\n{text}\n",
  temperature=1,
  max_tokens=64,
  top_p=1.0,
  frequency_penalty=0.0,
  presence_penalty=0.0
)
print(response["choices"][0]["text"])




