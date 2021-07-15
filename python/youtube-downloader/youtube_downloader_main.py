import youtube_dl
from youtubesearchpython import VideosSearch
from pprint import pprint

URL = 'https://www.youtube.com/watch?v=XUhVCoTsBaM'

YOUTUBE_DL_OPTS = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}

def download_video_as_mp3(url):
    with youtube_dl.YoutubeDL(YOUTUBE_DL_OPTS) as ydl:
        ydl.download([url])


def search_music_video(string_to_search):
    videosSearch = VideosSearch(string_to_search, limit = 2)

    result = videosSearch.result()

    first_song_result = result['result'][1]

    pprint(first_song_result)

    return first_song_result['link']


song = input('Enter the name/artist/title of the song you want to download: ')

video_url = search_music_video(song)

download_video_as_mp3(video_url)
