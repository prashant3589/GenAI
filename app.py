from distutils.log import debug
from fileinput import filename
from flask import * 
from flask import Flask
import openai
from pydub import AudioSegment

app = Flask(__name__)
@app.route("/") 
def home():  
    return render_template("index.html")  
  
# @app.route('/success', methods = ['POST'])  
# def success():  
#     summary =''
#     if request.method == 'POST':  
#         f = request.files['file']
#         f.save(f.filename)  
#         openai.api_key='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'
#         print(f.filename)
#         audio_file= open(f.filename,'rb')
#         transcript = openai.Audio.transcribe("whisper-1", audio_file)
#         text = transcript["text"]
#         print(text)
#         response = openai.Completion.create(
#           model="text-davinci-003",
#           prompt="Summarize this :\n{text}\n",
#           temperature=1,
#           max_tokens=500,
#           top_p=1.0,
#           frequency_penalty=0.0,
#           presence_penalty=0.0
#         )
#         summary =response["choices"][0]["text"]
#         return render_template("summary.html", summary = summary)  
#     else :
#         return render_template("index.html")  


@app.route('/document', methods = ['POST'])  
def document():  
    summary =''
    if request.method == 'POST':  
        f = request.files['file']
        f.save(f.filename)  
        openai.api_key='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'
        print(f.filename)
        text_file= open(f.filename,'r')
        transcript = text_file.read()
        n = 300 # chunk length
        chunks = [transcript[i:i+n] for i in range(0, len(transcript), n)]
        #print(transcript)
        summary =''
        for chunck in chunks:
            #print(chunck)
            response = openai.Completion.create(
              model="text-davinci-003",
              #prompt="Summarize this :\n{chunck}\n",
              prompt = "Summarize : "+chunck,
              temperature=1,
              max_tokens=60,
              top_p=1.0,
              frequency_penalty=0.0,
              presence_penalty=1
            )
            print(summary)
            summary = summary+'\n '+ response["choices"][0]["text"]
        return render_template("summary.html", summary = summary)  
    else :
        return render_template("index.html")  
        
        
    
  
if __name__ == '__main__':  
    app.run()
