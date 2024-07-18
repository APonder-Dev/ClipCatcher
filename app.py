from flask import Flask, request, send_file, render_template
from pytube import YouTube
from pydub import AudioSegment
import os

# Import the configuration class
from instance.config import DevelopmentConfig  # Use the appropriate config class here

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)  # Use the appropriate config class here

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download():
    url = request.form['url']
    download_format = request.form['format']
    yt = YouTube(url)
    title = yt.title

    if download_format == 'mp3':
        audio_stream = yt.streams.filter(only_audio=True).first()
        download_path = audio_stream.download(filename="temp_audio")
        audio = AudioSegment.from_file(download_path)
        output_path = f"{title}.mp3"
        audio.export(output_path, format="mp3")
        os.remove(download_path)
    else:  # mp4
        video_stream = yt.streams.filter(file_extension='mp4').first()
        output_path = video_stream.download(filename=f"{title}.mp4")

    return send_file(output_path, as_attachment=True, attachment_filename=os.path.basename(output_path))

if __name__ == '__main__':
    app.run()
