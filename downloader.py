import yt_dlp
import os

def download_song(url, song_name):
    """
    Downloads a song from a given URL and saves it as a FLAC file.

    Args:
        url (str): The URL of the video/song to download.
        song_name (str): The name of the song, used for the filename.
    """
    output_dir = 'downloads'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'flac',
            'preferredquality': '192',
        }],
        'outtmpl': os.path.join(output_dir, f'{song_name}.%(ext)s'),
        'noplaylist': True,
        'http_headers': {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
        }
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        return f"Song '{song_name}' downloaded successfully as FLAC."
    except Exception as e:
        return f"Error downloading song: {e}"

if __name__ == '__main__':
    # Example usage:
    # A different test video to avoid potential blocks.
    test_url = "https://www.youtube.com/watch?v=y6120QOlsfU"
    test_song_name = "Test-Song"
    print(download_song(test_url, test_song_name))
