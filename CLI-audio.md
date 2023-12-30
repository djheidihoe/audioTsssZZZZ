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
  
## now lets explore sox.
Sox is like audacity in the CLI and can be automated nicely.
> SoX - Sound eXchange, the Swiss Army knife of audio manipulation

some nice statistics on the file can be seen with stat.  
Human readable information is done with soxi file.name

`sox audio.mp3 -n stat`
`soxi audio.mp3`
`soxi trim.mp3`

next to `sox` there is also `play` and `rec`
this plays a 3 sec organ synth.
`play -n -c1 synth sin %-12 sin %-9 sin %-5 sin %-2 fade h 0.1 3 0.1`
some command as simple as this will record into file
`rec file.wav`

from cht.sh, but i could not get this working on my machine. Not sure if this is the way to go here or rather use GUI. But nice to have such a low level way on audio in the future.

curl cht.sh/sox/rec
`rec snd.wav silence 1 .5 2.85% 1 1.0 3.0% vad gain -n  : newfile : restart`

speed up by 2x -- also apply pitch correction
`sox audio.mp3 speedup.mp3 speed 2.0`
`play speedup.mp3`
`sox audio.mp3 speedup2.mp3 speed 2.0 pitch -200`
