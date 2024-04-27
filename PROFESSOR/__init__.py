from PROFESSOR.core.bot import PROF
from PROFESSOR.core.dir import dirr
from PROFESSOR.core.git import git
from PROFESSOR.core.userbot import Userbot
from PROFESSOR.misc import dbb, heroku

from SafoneAPI import SafoneAPI
from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = PROF()
api = SafoneAPI()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
