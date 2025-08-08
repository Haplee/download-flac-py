import yt_dlp
import os
import argparse
import re

def sanitize_filename(name):
    """
    Removes characters that are not allowed in filenames and limits length.
    """
    name = name.replace('/', '_').replace('\\', '_')
    name = re.sub(r'[<>:"|?*]', '', name)
    name = name.strip()
    return name[:150]

def get_video_title(url, opts):
    """
    Fetches the title of a video from a URL using yt-dlp.
    """
    try:
        with yt_dlp.YoutubeDL(opts) as ydl:
            info = ydl.extract_info(url, download=False)
            return info.get('title', None)
    except Exception as e:
        print(f"    [Warning] Could not fetch title for URL: {url}. Reason: {e}")
        return None

def download_song(url, song_name, base_opts):
    """
    Downloads a song from a given URL and saves it as a FLAC file.
    """
    output_dir = 'downloads'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    ydl_opts = base_opts.copy()
    ydl_opts['outtmpl'] = os.path.join(output_dir, f'{song_name}.%(ext)s')

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        return f"Success: Downloaded to 'downloads/{song_name}.flac'"
    except Exception as e:
        return f"Error: {e}"

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="Downloads songs in FLAC format from a list of URLs in a text file.",
        epilog="Example: python downloader.py my_songs.txt"
    )
    parser.add_argument(
        "file_path",
        help="Path to a .txt file containing URLs, one per line."
    )

    args = parser.parse_args()

    try:
        with open(args.file_path, 'r') as f:
            urls = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print(f"Error: The file '{args.file_path}' was not found.")
        exit(1)

    if not urls:
        print(f"Error: The file '{args.file_path}' is empty or contains no valid URLs.")
        exit(1)

    print(f"Found {len(urls)} URL(s) in '{args.file_path}'. Starting download process...\n")

    base_ydl_opts = {
        'format': 'bestaudio',
        'postprocessors': [{'key': 'FFmpegExtractAudio', 'preferredcodec': 'flac'}],
        'noplaylist': True,
        'http_headers': {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
        },
        'quiet': True,
        'no_warnings': True,
    }

    title_fetch_opts = {
        'quiet': True,
        'no_warnings': True,
        'http_headers': base_ydl_opts['http_headers'],
    }

    for i, url in enumerate(urls, 1):
        print(f"[{i}/{len(urls)}] Processing: {url}")

        title = get_video_title(url, title_fetch_opts)

        if title:
            sanitized_title = sanitize_filename(title)
            print(f"  > Title: {title}")
            print(f"  > Filename: {sanitized_title}.flac")

            result = download_song(url, sanitized_title, base_ydl_opts)
            print(f"  > Status: {result}")
        else:
            print(f"  > Status: Error - Could not fetch title. Skipping download.")
        print("-" * 20)

    print("\nBatch download process finished.")
