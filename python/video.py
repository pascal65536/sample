import pafy
import youtube_dl
import requests

inst = "https://www.instagram.com/p/CU7thYSBkYw/"
vk = "https://vk.com/video-203236910_456239830"
youtube = "https://www.youtube.com/watch?v=Q4A-OgxEKxc"
ok = "https://ok.ru/video/3297912820168"
fb = "https://www.facebook.com/ibigdan/videos/687044195618434"
twitter = "https://twitter.com/OutUkraine/status/1463931010731720714"
rutube = "https://rutube.ru/video/44ae7e6d7fbe72cd2eedec09e80c0232/"


if __name__ == "__main__":
    print("-" * 10)
    ydl_opts = {}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([youtube])

    info_dict = dict()
    youtube = "https://www.youtube.com/watch?v=Mu4_zNCaymA"
    with youtube_dl.YoutubeDL({"quiet": True}) as ydl:
        info_dict = ydl.extract_info(youtube, download=False)
        video_url = info_dict.get("url", None)
        video_id = info_dict.get("id", None)
        video_title = info_dict.get("title", None)

    for formats in info_dict["formats"]:
        if int(formats["format"].split(" ")[0]) == 18 and formats["asr"]:
            print(f"{formats['format']=}")
            print(f"{formats['asr']=}")
            print(f"{formats['url']=}")
            print(f"{info_dict['title']=}")

# {'asr': 48000, 'filesize': 2350104, 'format_id': '249', 'format_note': 'tiny', 'fps': None, 'height': None, 'quality': 0,
# 'tbr': 49.917, 'url': '',
# 'width': None, 'ext': 'webm', 'vcodec': 'none', 'acodec': 'opus', 'abr': 49.917,
# 'downloader_options': {'http_chunk_size': 10485760}, 'container': 'webm_dash', 'format': '249 - audio only (tiny)',


# virtualenv -p /usr/bin/python3.9 .env
# source .env/bin/activate
