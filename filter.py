import requests

SOURCE = "https://iptv-org.github.io/iptv/index.m3u"

with open("channels.txt") as f:
    wanted = [x.strip().lower() for x in f]

data = requests.get(SOURCE).text.splitlines()

output = ["#EXTM3U"]

for i,line in enumerate(data):
    if line.startswith("#EXTINF"):
        for ch in wanted:
            if ch in line.lower():
                output.append(line)
                if i+1 < len(data):
                    output.append(data[i+1])

with open("myplaylist.m3u","w") as f:
    f.write("\n".join(output))
