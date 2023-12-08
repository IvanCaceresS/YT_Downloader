from flask import Flask, request, render_template
from pytube import YouTube
import os
import webbrowser
from threading import Timer

app = Flask(__name__)

def open_browser():
      webbrowser.open_new('http://127.0.0.1:5000/')

@app.route('/', methods=['GET', 'POST'])
def index():
    download_info = []
    download_path = ''

    # Leer la ruta de descarga del archivo
    if os.path.exists('download_path.txt'):
        with open('download_path.txt', 'r') as file:
            download_path = file.read().strip()

    if request.method == 'POST' and download_path:
        urls = request.form.get('urls')
        formato = request.form.get('formato')
        calidad = request.form.get('calidad')

        for url in urls.split('\n'):
            url = url.strip()
            if url:
                yt = YouTube(url)
                if formato == 'mp4':
                    stream = yt.streams.filter(progressive=True, file_extension='mp4', resolution=calidad).first()
                    if stream:
                        stream.download(download_path)
                        download_info.append(f"Descarga completada para {url}")
                    else:
                        download_info.append(f"No se encontró stream de video adecuado para {url}")
                elif formato == 'mp3':
                    stream = yt.streams.filter(only_audio=True).first()
                    if stream:
                        audio_path = stream.download(download_path)
                        mp3_path = audio_path.replace('.mp4', '.mp3').replace('.webm', '.mp3')
                        audio_clip = AudioFileClip(audio_path)
                        audio_clip.write_audiofile(mp3_path)
                        audio_clip.close()
                        os.remove(audio_path)  # Remove the original audio file
                        download_info.append(f"Descarga de audio completada para {url}")
                    else:
                        download_info.append(f"No se encontró stream de audio adecuado para {url}")

    return render_template('index.html', download_info=download_info)

if __name__ == '__main__':
    if os.environ.get('WERKZEUG_RUN_MAIN') != 'true':
        Timer(1, open_browser).start()  # Abre una pestaña del navegador después de 1 segundo
    app.run(debug=True)