# **Shorty**

This Python script converts text from a file into a video with speech, subtitles, and a random background video. It uses **Google Text-to-Speech (gTTS)** to generate speech, **FFmpeg** for video and subtitle generation, and a random background video from a folder.

## **Requirements**

- **Python 3.x**
- **Libraries:**
  - `gtts`
  - `subprocess` (comes built-in with Python)
  - `os` (comes built-in with Python)
  - `random` (comes built-in with Python)
- **FFmpeg:** You must have FFmpeg installed and available in your system’s PATH to handle video processing and audio synchronization.
  
### **Installation of Dependencies**

To install the required libraries, you can use `pip`:

```bash
pip install gtts
```

For FFmpeg, download it from [FFmpeg.org](https://ffmpeg.org/download.html) or use a package manager depending on your operating system:

- **Windows:** Download the binaries and add them to your PATH.
- **macOS:** Use Homebrew: `brew install ffmpeg`
- **Linux:** Use your package manager, e.g., `sudo apt install ffmpeg` (for Ubuntu).

## **Script Workflow**

1. **Convert Text to Audio**:
   - The script converts the input text (from a file) into speech using **gTTS**.
   
2. **Generate Subtitles**:
   - It splits the input text into words and calculates the duration of each word in the generated speech, then generates **subtitles** (`.srt` file) corresponding to the timing.

3. **Select Random Background Video**:
   - A random video from the background folder is chosen.

4. **Generate Final Video**:
   - The script combines the background video with the speech and subtitles, then saves the output as an MP4 file.

## **File Structure**

Your project folder should be structured like this:

```
Text-to-Video-Generator/
│
├── back/                 # Folder containing background videos
│   ├── background1.mp4
│   ├── background2.mp4
│   └── ...               # Other background videos
│
├── texts.txt             # Text file with segments of text to convert
├── script.py             # Your main Python script
└── README.md             # This README file
```

- **texts.txt** should contain blocks of text separated by blank lines (e.g., each paragraph will be converted into one video).
  
Example of **texts.txt**:

```
Hello, welcome to the video! This is the first sentence.

This is another video segment. Enjoy watching!
```

- **back/** is the folder that contains your background videos. The script will randomly pick one for each video segment.

## **Usage**

### Step 1: Prepare your text and background folder

1. Create a `texts.txt` file that contains the text you want to convert into speech and video.
2. Create a `back/` folder and add background video files (e.g., `.mp4` files). These will be used as the background for each video.

### Step 2: Running the Script

Once you have everything set up, you can run the script using:

```bash
python script.py
```

The script will read the **texts.txt** file, generate speech for each segment, add subtitles, and combine them with a random background video. It will create output video files in the same folder.

### Step 3: Customize the Number of Shorts

In the script, there's a function `shorts()` that controls how many video segments to process. By default, it processes the first 2 segments from **texts.txt**:

```python
shorts(path, backgroundfolder, 2)
```

You can change the `2` to any number to control how many video segments you want to generate.

### Step 4: Check the Output

After the script runs, you'll see video files like `output_video_0.mp4`, `output_video_1.mp4`, etc., in the working directory.

## **Script Details**

- **`time(seconds)`**: A helper function that formats a given time in seconds to a subtitle-compatible format (`HH:MM:SS,MS`).
  
- **`video(text, audio, video, backgroundfolder)`**: The main function that generates audio from text, creates subtitles, and produces a video with background video and subtitles.

- **`shorts(path, backgroundfolder, n)`**: This function reads text from a file and processes the first `n` segments into individual videos.

---

## **Troubleshooting**

- **FFmpeg Errors**: Ensure FFmpeg is installed correctly and available in your system's PATH. You can check this by running `ffmpeg -version` in your terminal.
  
- **Missing Libraries**: If you encounter errors related to missing Python packages, ensure you have installed all dependencies (`gtts`).

- **Subtitles Not Syncing**: If the subtitles aren't syncing well with the speech, you may need to adjust the `word_duration` logic in the `video()` function.

---

## **License**

This project is licensed under the MIT License.

