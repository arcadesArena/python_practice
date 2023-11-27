from pytube import YouTube,Playlist
from pathlib import Path
import tkinter,argparse,os

def download_playlist(link,location):
    pList = Playlist(url=link)
    title = pList.title
    location=location+('\\' if os.name=='nt' else '/')+title if location!=None else title
    Path(location).mkdir(parents=True, exist_ok=True)
    idx_pad = len(str(len(pList.videos)))
    for idx,video in enumerate(pList.video_urls,start=1):
        download_video(video,location,str(idx).rjust(idx_pad,'0')+' ')

def download_video(link,location,index=''):
    video = YouTube(link)
    quality = video.streams.get_highest_resolution()
    quality.download(output_path=location,filename_prefix=index)
    print(f"Done....{str(quality.resolution).ljust(8,'.')}{video.title}")

def main():
    parser = argparse.ArgumentParser(description='YTD')
    op = parser.add_mutually_exclusive_group(required=True)
    op.add_argument('-v','--video', help='download one video',action='store_true')
    op.add_argument('-p','--playlist', help='download a playlists',action='store_true')
    parser.add_argument('-u','--link',help='link of video/playlist',required=True,dest='url')
    parser.add_argument('-l','--location',help='directory where to download',default=None,dest='location')
    args = vars(parser.parse_args())
    
    if args['video']:
        download_video(args['url'],args['location'])
    elif args['playlist']:
        download_playlist(args['url'],args['location'])



if __name__=='__main__':
    main()