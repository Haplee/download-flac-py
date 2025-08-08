# Music Downloader - A Special Gift

This is a simple command-line tool to download music from various websites (like YouTube) and save it in the high-quality FLAC format. It was created as a special gift for someone who loves music.

## Features

-   **Batch Downloading:** Provide a text file with a list of URLs to download multiple songs at once.
-   **Automatic Naming:** The script automatically uses the video title as the filename for each song.
-   **High-Quality Downloads:** Downloads audio in FLAC format to preserve the best sound quality.

## How to Use

### Prerequisites

Before you start, you need to have two things installed on your computer:

1.  **Python 3:** If you don't have it, you can download it from [python.org](https://www.python.org/downloads/).
2.  **FFmpeg:** This is a crucial tool that the script uses to convert the downloaded audio to FLAC.
    -   **Windows:** Follow this [guide to install FFmpeg](https://www.geeksforgeeks.org/how-to-install-ffmpeg-on-windows/).
    -   **macOS:** You can install it using Homebrew: `brew install ffmpeg`
    -   **Linux:** Use your package manager, for example on Debian/Ubuntu: `sudo apt-get install ffmpeg`

### Installation

1.  **Download the script:**
    - Download the `downloader.py` script to your computer.

2.  **Install the Python dependency:**
    - Open your terminal or command prompt.
    - Navigate to the directory where you saved `downloader.py`.
    - Install the required `yt-dlp` library by running:
    ```bash
    pip install yt-dlp
    ```

### Running the Tool

1.  **Create a text file** (e.g., `my_songs.txt`) and add the URLs of the songs you want to download, with one URL per line. For example:
    ```
    https://www.youtube.com/watch?v=dQw4w9WgXcQ
    https://www.youtube.com/watch?v=y6120QOlsfU
    ```

2.  **Run the script from your terminal**, providing the path to your text file:
    ```bash
    python downloader.py my_songs.txt
    ```

3.  The script will read each URL from the file, download the song, and save it using the video's title as the filename. All songs will be placed in a folder named `downloads`.

---

With love and code. ❤️
