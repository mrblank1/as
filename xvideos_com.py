
#coding=utf-8
import requests
import re
import os
import shutil
import time
#proxies={'https':'https://103.146.176.124:80'}
proxies = {'https': 'https://127.0.0.1:8080'}

#Play address
url_play = 'https://www.xxxxxxxxxxxxxxxxxxxxxxxxse_maids_in_my_house_part_1'
 
 #Low image quality download address, you need to log in to get the download address
url_down_low = 'https://xxxxxxxxxxxxxxxx9&download=1'
 
#url_play = input('Please enter the play address:\n')
#url_down_low =input("Please enter the low-quality download address:\n")
#url_play='https://www.xvideos.com/video36147283/horny_couple_making_out_and_having_passionate_sex'
url_play='https://www.youtube.com/'
url_down_low='https://video-hw.xvideos-cdn.com/videos/3gp/f/b/5/xvideos.com_fb5f03c069ef24f67d732600ff91ab00.mp4?e=1621289937&h=85dc53b1b7d8f8b50a7260787379723c&download=1'
 #Get request parameters
info = '?' + re.search('e=(.*)',url_down_low).group()
print(info)

 #Get the image quality list file address
res0 = requests.get(url_play,proxies=proxies).text
a1 = re.search('https://hls(.*)\'',res0)
url_m3u8 = a1.group().replace('\'','')
print(url_m3u8)
 
 #Get the 1080p quality name in the quality list
res1 = requests.get(url_m3u8).text
a2 = re.search('(.*)1080p.m3u8(.*)',res1).group()
print(a2)
 
 
 #Build to get ts list address
if '?' in a2:
    url_ts = url_m3u8.split('hls.m3u8')[0] + a2
    print(url_ts)
    print(1)
 
else:
    url_ts = url_m3u8.replace('hls.m3u8', a2) + info
    print(url_ts)
    print(2)
 
 #Get ts list content
res2 = requests.get(url_ts).text
 
 #Statistics number of ts
ts_list = re.findall('hls.*.ts.*',res2)
print('ts_list:',ts_list)
cont = len(ts_list) -1
# print(cont)
 
 #Build ts download address list
ts_url_list = []
for ts in ts_list:
    if '?' in ts:
        tsurl = url_m3u8.split('hls.m3u8')[0] + ts
    else:
        tsurl = url_m3u8.replace('hls.m3u8',ts) + info
    ts_url_list.append(tsurl)
print(ts_url_list)
 
###########################download#############################
 #Temporary directory
if os.path.exists('tmp'):
    shutil.rmtree('tmp')
    time.sleep(1)
    os.makedirs('tmp')
else:
    os.makedirs('tmp')
 
 #start download 
print('downloading...cont {}'.format(cont))
i = 0
for t,u in zip(ts_list,ts_url_list):
 
    if '?' in t:
        t = t.split('?')[0]
 
    print('downloading  {}'.format(t))
    try:
        res666 = requests.get(u)
 
        if i >= 9:
            with open('./tmp/{}'.format(t),'wb') as f:
                f.write(res666.content)
        else:
            tt = list(t)
            tt.insert(-4,'0')
            t = ''.join(tt)
            with open('./tmp/{}'.format(t), 'wb') as f:
                f.write(res666.content)
            i += 1
 
    except:
        print('download {} error'.format(t))
 
 ###########################merge###################### ###########
 #Merge into mp4 video file
os.system('copy /b  tmp\\*.ts ' + ' 1080p{}.mp4'.format(str(time.time())))