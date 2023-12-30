#read WAV and MP3 files to array
from pydub import AudioSegment
import numpy as np
from scipy.io import wavfile
from plotly.offline import init_notebook_mode
import plotly.graph_objs as go
import plotly

# read WAV files using scipy.io.wavfile
fs_wav, data_wav = wavfile.read("files/test.wav")

#read MP3 file using pudub
audiofile = AudioSegment.from_file("files/audio.mp3")
data_mp3 = np.array(audiofile.get_array_of_samples())
fs_mp3 = audiofile.frame_rate

print('Signal Duration = {} seconds'.
      format(data_wav.shape[0] / fs_wav))

time_wav = np.arange(0, len(data_wav)) / fs_wav
plotly.offline.iplot({ "data": [go.Scatter(x = time_wav,
                                            y = data_wav[:, 0],
                                            name = 'left channel'),
                     go.Scatter(x = time_wav,
                                            y = data_wav[:, 1],
                                            name = 'right channel')]})

# Normalization

data_wav_norm = data_wav / (2**15)
time_wav = np.arange(0, len(data_wav)) / fs_wav
plotly.offline.iplot({"data": [go.Scatter(x = time_wav, y = data_wav_norm, name = 'normalized audio signal')]})
