# yahoo電影(HLS)
import requests
import os
import glob

# 下載.m3u8
response_trailer = requests.get('https://edgecast-cf-prod.yahoo.net/cp-video-transcode/production/b6697eae-9a1a-30bb-afe9-d3993c5b6fad/2023-04-07/17-06-37/9df93b9d-d88f-50e8-9698-68daca25a796/stream_1280x720x733_v2.m3u8')
if not os.path.exists('videos'):
    os.mkdir('videos')

with open('videos//trailer.m3u8', 'wb') as f:
        f.write(response_trailer.content)
        
# 下載ts檔案
list_of_ts_url = []
with open('videos//trailer.m3u8', 'r', encoding='utf-8') as f:
    contents = f.readlines()
#     print(contents)
    
url_base = 'https://edgecast-cf-prod.yahoo.net/cp-video-transcode/production/b6697eae-9a1a-30bb-afe9-d3993c5b6fad/2023-04-07/17-06-37/9df93b9d-d88f-50e8-9698-68daca25a796/'

for content in contents:
    if content.endswith('ts\n'):
        ts_url = url_base + content.replace('\n', "")
        list_of_ts_url.append(ts_url)
# print(list_of_ts_url)

for index, url in enumerate(list_of_ts_url):
    print(url)
    reponse_ts = requests.get(url)
    
    with open(f'videos//{index+1}.ts', 'wb') as f:
        f.write(reponse_ts.content)

# 合併所有ts
ts_files = sorted(glob.glob('videos//*.ts'), key=os.path.getmtime)

with open('videos//trailer.mp4', 'wb') as f:
    for ts_file in ts_files:
        f.write(open(ts_file, 'rb').read())