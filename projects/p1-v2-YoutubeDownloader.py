from pytube import YouTube

link = "https://www.youtube.com/watch?v=ojFsmDqj9VI&ab_channel=TimerTopia"
yt = YouTube(link)


for res_mp4 in [stream for stream in yt.streams if stream.mime_type.startswith('video/mp4')]:
    print(res_mp4.resolution, res_mp4.codecs)
print("CUTTS")
for res_webm in [stream for stream in yt.streams if stream.mime_type.startswith('video/webm')]:
    print(res_webm.resolution, res_webm.codecs)
