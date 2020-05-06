import sys
import subprocess
import argparse
import os
import shutil
import time
import error
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
DEVELOPER_KEY = 'AIzaSyCxkYklkRaGr6wq_ISt3DPwR9Ipil_xiXU'
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'
f=open("videos.txt", "a+")
def implicit():
    from google.cloud import storage
    storage_client = storage.Client()
    buckets = list(storage_client.list_buckets())
def youtube_search(options):
  youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
    developerKey=DEVELOPER_KEY)
  search_response = youtube.search().list(
    q=options.q,
    part='id,snippet',
    maxResults=options.max_results
  ).execute()
  for search_result in search_response.get('items', []):
   if search_result['id']['kind'] == 'youtube#video':
       f.write("https://www.youtube.com/watch?v=%s\r\n" % (search_result['id']['videoId']))

def transcribe_gcs(gcs_uri,fname):
    """Asynchronously transcribes the audio file specified by the gcs_uri."""
    from google.cloud import speech
    from google.cloud.speech import enums
    from google.cloud.speech import types
    client = speech.SpeechClient()
    audio = types.RecognitionAudio(uri=gcs_uri)
    config = types.RecognitionConfig(
        encoding=enums.RecognitionConfig.AudioEncoding.FLAC,
        sample_rate_hertz=44100,
        language_code='en-US')
    operation = client.long_running_recognize(config, audio)
    #print('Waiting for operation to complete...')
    response = operation.result(timeout=90)
    for result in response.results:
        ftxt = fname.replace(".flac",".txt")
        #print(ftxt)
	filetxt = open(ftxt,"a+")
        content = result.alternatives[0].transcript
        ans = ('curl -d' "text=%s" 'http://bark.phon.ioc.ee/punctuator'% content)
        #filetxt.write(result.alternatives[0].transcript)
        filetxt.write(ans)
        #filetxt.replace("\n"," ")
        filetxt.flush()
        #filetext.close()
        
       # with open (ftxt, "r") as contentfile:
        # content=contentfile.read().replace('\n',' ')
        #subprocess.call('curl -d "text=%s" http://bark.phon.ioc.ee/punctuator'% content,shell=True)
        

        #print('{}'.format(result.alternatives[0].transcript))
files = os.listdir("/home/kajol/Desktop/BE")
for f in files:
    if(f.startswith('--q') and f.endswith('.txt')):
        shutil.move("/home/kajol/Desktop/BE"+"/"+f,args.q)
if __name__ == '__main__':
 parser = argparse.ArgumentParser()
 parser.add_argument('--q', help='Search term', default='Google')
 parser.add_argument('--max-results', help='Max results', default=1)
 args = parser.parse_args()
 os.makedirs(args.q)
 try:
    youtube_search(args)
 except HTTPError as e:
  print ('An HTTP error %d occurred:\n%s' % (e.resp.status, e.content))
f.close()
f=open("videos.txt", "r")
f1 = f.readlines()
for x in f1:
  subprocess.call('youtube-dl -x --audio-format flac %s '% x, shell=True)
files = os.listdir("/home/kajol/Desktop/BE")
for f in files:
    if(f.endswith('.flac')):
        shutil.move("/home/kajol/Desktop/BE"+"/"+f,args.q)
files = os.listdir("/home/kajol/Desktop/BE/"+args.q)
os.chdir("/home/kajol/Desktop/BE/"+args.q)
for f in files:
 print(f)
 newfilename = "new" + f
 command = ['sox', f, '-c', '1', newfilename]
 subprocess.Popen(command)
time.sleep(10)
os.chdir("/home/kajol/Desktop/BE/")
os.chdir("/home/kajol/Desktop/BE/"+args.q)
files1 = os.listdir("/home/kajol/Desktop/BE/"+args.q)
i=0
for f1 in files1:
 if(f1.startswith('new')):
  i = i+1
 else:
  os.remove(f1) 
os.chdir("/home/kajol/Desktop/BE/")
subprocess.call('gsutil cp -R "%s" gs://analysiss' % args.q, shell=True)
#os.chdir("/home/kajol/Desktop/BE/"+args.q)
files = os.listdir("/home/kajol/Desktop/BE/"+args.q)
for f in files: 
 #print(f)
 fname = args.q 
 transcribe_gcs('gs://analysiss/'+fname+'/'+f,f)
 
