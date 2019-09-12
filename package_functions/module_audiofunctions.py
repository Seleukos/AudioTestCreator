
import pyaudio
import wave
import sys



def playback_audiofile(filepath):

    CHUNK = 1024
    #filepath = 'C:\\Users\\Tobi_SurfacePro\\PycharmProjects\\Test_PyAudio\\Jungle Windows Start.wav'

    if len(filepath) < 2:
        print("Plays a wave file.\n\nUsage: %s filename.wav" % filepath)
        sys.exit(-1)

    wf = wave.open(filepath, 'rb')

    print(wf.getnchannels())
    pyaudio.paASIO = 3


    # instantiate PyAudio (1)
    p = pyaudio.PyAudio()
    print(p.get_host_api_info_by_index(0))
    print(p.get_default_host_api_info())

    # open stream (2)
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True)

    # read data
    data = wf.readframes(CHUNK)

    # play stream (3)
    while len(data) > 0:
        stream.write(data)
        data = wf.readframes(CHUNK)

    # stop stream (4)
    stream.stop_stream()
    stream.close()

    # close PyAudio (5)
    p.terminate()

    for x in range(100):
        get_soundcard_dev_info()


def get_soundcard_dev_info():
   import pyaudio
   pad_sc = pyaudio.PyAudio()
   max_devs = pad_sc.get_device_count()
   input_devices_index = []
   output_devices_index = []

   for i in range(max_devs):
       devinfo = pad_sc.get_device_info_by_index(i)
       if "TUSBAudio ASIO Driver" in devinfo['name']:
           input_devices_index.append(int(devinfo['index']))
           output_devices_index.append(int(devinfo['index']))

   if not input_devices_index:
      print ("NONE")

   print(input_devices_index)