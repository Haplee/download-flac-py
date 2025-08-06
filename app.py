from flask import Flask, render_template, request, redirect, url_for, flash
from downloader import download_song
import os

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Needed for flashing messages

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form['url']
        song_name = request.form['song_name']

        if not url or not song_name:
            flash('Please provide both a URL and a song name.', 'error')
            return redirect(url_for('index'))

        # To avoid blocking the request, we should run this in a background thread.
        # For simplicity in this example, we run it synchronously.
        # In a real-world application, consider using Celery or similar.
        result = download_song(url, song_name)
        flash(result, 'info')

        return redirect(url_for('index'))

    return render_template('index.html')

if __name__ == '__main__':
    if not os.path.exists('templates'):
        os.makedirs('templates')
    # A simple check to create a default index.html if it doesn't exist
    if not os.path.exists('templates/index.html'):
        with open('templates/index.html', 'w') as f:
            f.write('<h1>Song Downloader</h1>') # A placeholder

    app.run(debug=True, port=8080)
