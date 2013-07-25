# Perform platform-specific initializations
# On Android:
#     Set the volume control to Media Volume

from kivy.utils import platform

platform = platform()

class InitializePlatformBase():
    ''' Default platform initialization.
        Does nothing
    '''
    def __init__(self):
        pass


class InitializePlatformAndroid(InitializePlatformBase):
    def __init__(self):
        from jnius import autoclass
        PythonActivity = autoclass('org.renpy.android.PythonActivity')
        # Set the volume control to Media Volume
        AudioManager = autoclass('android.media.AudioManager')
        PythonActivity.mActivity.setVolumeControlStream(AudioManager.STREAM_MUSIC)


# Default to no platform-specific initialization
InitializePlatform = InitializePlatformBase

# Platform-specific searches
if platform == "android":
    InitializePlatform = InitializePlatformAndroid
