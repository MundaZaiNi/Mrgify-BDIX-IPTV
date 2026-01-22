import requests

url = "https://raw.githubusercontent.com/abusaeeidx/Mrgify-BDIX-IPTV/refs/heads/main/playlist.m3u"
data = requests.get(url).text

with open("playlist.m3u", "w", encoding="utf-8") as f:
    f.write(data)
