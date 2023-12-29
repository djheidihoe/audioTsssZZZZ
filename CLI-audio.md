# part one of tutorial and personal testing with audio files in the CLI

[tutorial](https://hackernoon.com/audio-handling-basics-how-to-process-audio-files-using-python-cli-jo283u3y) 

## ffmpeg

### vimtipp - reverse order   
by tac util on mac/linux  
`'<,'>!tac`  
core Vim move all matches  
`:g/^/m0`  
offset and only on visual selection  
`:'<,'>g/^/m8`  
  
convert file to audio.mp3  
`ffmpeg -i file.webm audio.mp3`  
  
show meta data (Meta Data LiSt)  
`mdls audio.mp3`  
  
convert audio.mp3 into convert.mp3 with -ar(audio rate) 16000 samples and -ac(audio channel)  
`ffmpeg -i audio.mp3 -ar 8000 -ac 1 convert.mp3`  
`mdls convert.mp3`  
`open convert.mp3`  
`open -a VLC convert.mp3`  
`open -a VLC audio.mp3`  
`ffmpeg -i audio.mp3`  
`ffmpeg -i convert.mp3`  
  
trim the audio with -ss for 'start sample' and -t for time in sec. The -t 120 keeps the audio clip in original 19 sec length.  
`ffmpeg -i audio.mp3 -ss 02 -t 5 trim.mp3`  
`ffmpeg -i audio.mp3 -ss 02 -t 120 trimlong.mp3`  
  
ffmpeg -f concat can concatenate audio files similar to cat.  
see tutorial for further infos  
  
now slice ot down into really small chunks. On MPC sampler, that would have been done with slice tool.  
Here i sliced a 19 sec file into 1 sec or 0.01 sec files :-)  
`ffmpeg -i audio.mp3 -f segment -segment_time 1 -c copy out%05d.mp3`  
`ffmpeg -i audio.mp3 -f segment -segment_time 0.01 -c copy ultra%05d.mp3`  
`open -a VLC out*`  
`open -a VLC ultr*`  
  
Tutorial goes through some more stereo and mono in/outs.  
On the opposite direction, to split a stereo file into two mono (one for each channel):  
  
`ffmpeg -i stereo.wav -map_channel 0.0.0 left.wav -map_channel 0.0.1 right.wav`  
  
