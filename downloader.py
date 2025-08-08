import yt_dlp
import os
import argparse

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
        'format': 'bestaudio',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'flac',
            'preferredquality': '192',
        }],
        'outtmpl': os.path.join(output_dir, f'{song_name}.%(ext)s'),
        'noplaylist': True,
        'http_headers': {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
        }
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        return f"Success: Song '{song_name}' downloaded to the 'downloads' folder."
    except Exception as e:
        return f"Error: {e}"

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="Downloads a song from a URL (like YouTube) and saves it as a FLAC file.",
        epilog="Example: python downloader.py 'https://www.youtube.com/watch?v=dQw4w9WgXcQ' 'My-Favorite-Song'"
    )
    parser.add_argument(
        "url",
        help="The URL of the song to download."
    )
    parser.add_argument(
        "song_name",
        help="The name to save the song file as (without extension)."
    )

    args = parser.parse_args()

    result = download_song(args.url, args.song_name)
    print(result)
