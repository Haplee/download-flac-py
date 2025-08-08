# Music Downloader - A Special Gift

This is a simple command-line tool to download music from various websites (like YouTube) and save it in the high-quality FLAC format. It was created as a special gift for someone who loves music.

## Features

-   **Command-Line Interface:** A simple script to download songs directly from your terminal.
-   **High-Quality Downloads:** Downloads audio in FLAC format to preserve the best sound quality.
-   **Easy to Use:** Just provide a URL and a name.

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

1.  **Run the script from your terminal:**
    ```bash
    python downloader.py "<URL>" "<SONG_NAME>"
    ```

2.  **Replace the placeholders:**
    -   `<URL>`: The full URL of the song you want to download (e.g., from YouTube). Make sure to wrap it in quotes.
    -   `<SONG_NAME>`: The name you want to give the downloaded file (without the extension). If the name has spaces, wrap it in quotes.

3.  **Example:**
    ```bash
    python downloader.py "https://www.youtube.com/watch?v=y6120QOlsfU" "My Test Song"
    ```

4.  The song will be downloaded into a folder named `downloads`.

---

With love and code. ❤️
