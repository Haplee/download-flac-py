# Music Downloader - A Special Gift

This is a simple web application to download music from various websites (like YouTube) and save it in the high-quality FLAC format. It was created as a special gift for someone who loves music.

## Features

-   **Web Interface:** A simple, beautiful web page to paste the song URL and give it a name.
-   **High-Quality Downloads:** Downloads audio in FLAC format to preserve the best sound quality.
-   **Easy to Use:** Just provide a URL and a name, and click download.

## How to Use

### Prerequisites

Before you start, you need to have two things installed on your computer:

1.  **Python 3:** If you don't have it, you can download it from [python.org](https://www.python.org/downloads/).
2.  **FFmpeg:** This is a crucial tool that the script uses to convert the downloaded audio to FLAC.
    -   **Windows:** Follow this [guide to install FFmpeg](https://www.geeksforgeeks.org/how-to-install-ffmpeg-on-windows/).
    -   **macOS:** You can install it using Homebrew: `brew install ffmpeg`
    -   **Linux:** Use your package manager, for example on Debian/Ubuntu: `sudo apt-get install ffmpeg`

### Installation

1.  **Clone or download this project.**

2.  **Navigate to the project directory** in your terminal.

3.  **Install the Python dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

### Running the Application

1.  **Run the Flask application:**
    ```bash
    python app.py
    ```

2.  **Open your web browser** and go to the following address:
    [http://127.0.0.1:8080](http://127.0.0.1:8080)

3.  **Enter the URL** of the song you want to download and give it a name.

4.  **Click "Download Song"**. The song will be downloaded and saved in a new folder called `downloads`.

---

With love and code. ❤️
