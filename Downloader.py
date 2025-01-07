import requests
import os
API_KEY = 'API'   #Pixabay API
API_ENDPOINT = 'https://pixabay.com/api/videos/'
def download_videos(n=5, folder='nature_videos'): #EXAMPLES
    if not os.path.exists(folder):
        os.makedirs(folder)
    video_count = 0
    page = 1
    while video_count < n:
        params = {
            'key': API_KEY,
            'q': 'nature',
            'video_type': 'film',
            'per_page': 50,  
            'page': page,
        }
        response = requests.get(API_ENDPOINT, params=params)   #Default query = Nature
        if response.status_code == 200:
            videos = response.json()['hits']
            for video in videos:
                video_duration = video['duration']
                video_width = video['videos']['large']['width']
                video_height = video['videos']['large']['height']
                if video_duration < 50 and video_width < video_height and video_height / video_width >= 1.7:
                    video_url = video['videos']['large']['url']
                    if video_url:
                        try:
                            video_file_path = f'{folder}/video_{video_count + 1}.mp4'
                            response = requests.get(video_url)
                            response.raise_for_status()
                            with open(video_file_path, 'wb') as f:
                                f.write(response.content)
                            print(f'Downloaded {video_file_path}')
                            video_count += 1
                            if video_count >= n:
                                break
                        except requests.exceptions.RequestException as e:
                            print(f'Failed to download video: {e}')
        else:
            print(f'Failed to fetch videos: {response.status_code}')
            break
        page += 1
download_videos(4)