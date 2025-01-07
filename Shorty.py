from gtts import gTTS
import subprocess
import os
import random
def time(seconds):
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    seconds_int = int(seconds % 60)
    milliseconds = int((seconds - seconds_int) * 1000)
    return f"{hours:02}:{minutes:02}:{seconds_int:02},{milliseconds:03}"
def video(text, audio,video, backgroundfolder):
    tts = gTTS(text=text, lang='en')
    tts.save(audio)
    duration = float(subprocess.check_output(
        ['ffprobe', '-v', 'error', '-show_entries', 'format=duration', 
         '-of', 'default=noprint_wrappers=1:nokey=1', audio]
    ).decode('utf-8').strip())
    words = text.split()
    word_duration = duration / len(words)
    subtitle_file = 'subtitles.srt'
    with open(subtitle_file, 'w') as file:
        current_time = 0
        for idx, word in enumerate(words, 1):
            start_time = current_time
            end_time = current_time + word_duration
            start_time_str = time(start_time)
            end_time_str = time(end_time)
            file.write(f"{idx}\n")
            file.write(f"{start_time_str} --> {end_time_str}\n")
            file.write(f"{word}\n\n")
            current_time = end_time
    backgroundvideo = random.choice(os.listdir(backgroundfolder))
    command = [
        'ffmpeg', '-stream_loop', '-1', '-i', os.path.join(backgroundfolder, backgroundvideo), '-i', audio,
        '-map', '0:v', '-map', '1:a', '-t', str(duration), '-vf', f"subtitles={subtitle_file}:force_style='FontName=Arial,FontSize=24,PrimaryColour=&H0000A7F8&,Outline=3,Shadow=0,Alignment=10'",
        '-c:v', 'libx264', '-c:a', 'aac', '-strict', 'experimental', '-shortest', video
    ]
    subprocess.run(command, check=True)
    os.remove(subtitle_file)
    os.remove(audio)
def shorts(path, backgroundfolder, n):
    with open(path, 'r') as f:
        texts = f.read().strip().split('\n\n')
    for i, text in enumerate(texts[:n], n):
        output_audio = f'output_{i}.mp3'
        output_video = f'output_video_{i}.mp4'
        video(text, output_audio, output_video, backgroundfolder)
path = 'texts.txt'
backgroundfolder = 'back'  
shorts(path, backgroundfolder,2)
