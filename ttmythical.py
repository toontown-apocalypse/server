print 'hello and welome to Toontown Mythical'

 title 'Toontown Mythical'

loadPrcFile('config/config.prc')

try:
    launcher
except:
    from toontown.launcher start "ToontownLauncher.py" and "Toonbase.py"
    launcher = ToontownDummyLauncher()
print 'ToontownStart: Starting Toontown...'

pollingDelay = 0.5
print 'ToontownStart: Polling for game2 to finish...'
while not launcher.getGame2Done():
    time.sleep(pollingDelay)
print 'ToontownStart: Game2 is finished.'
print 'ToontownStart: Starting the game.'
if launcher.isDummy():
    http = HTTPClient()
else:
    http = launcher.http
tempLoader = Loader()
backgroundNode = tempLoader.loadSync(Filename('phase_3/models/gui/loading-background'))
print 'ToontownStart: setting default font'
DirectGuiGlobals.setDefaultFontFunc(ToontownGlobals.getInterfaceFont)
launcher.setPandaErrorCode(7)
if base.win == None:
    print 'Unable to open window; aborting.'
    sys.exit()

launcher.setPandaErrorCode(0)
launcher.setPandaWindowOpen()
ConfigVariableDouble('decompressor-step-time').setValue(0.01)
ConfigVariableDouble('extractor-step-time').setValue(0.01)
backgroundNodePath = aspect2d.attachNewNode(backgroundNode, 0)
backgroundNodePath.setPos(0.0, 0.0, 0.0)
backgroundNodePath.setScale(render2d, VBase3(1))
backgroundNodePath.find('**/fg').setBin('fixed', 20)
backgroundNodePath.find('**/bg').setBin('fixed', 10)
base.graphicsEngine.renderFrame()
DirectGuiGlobals.setDefaultRolloverSound(base.loadSfx('phase_3/audio/sfx/GUI_rollover.mp3'))
DirectGuiGlobals.setDefaultClickSound(base.loadSfx('phase_3/audio/sfx/GUI_create_toon_fwd.mp3'))
DirectGuiGlobals.setDefaultDialogGeom(loader.loadModel('phase_3/models/gui/dialog_box_gui'))
OTPGlobals.setDefaultProductPrefix(TTLocalizer.ProductPrefix)
if base.musicManagerIsValid:
    music = base.musicManager.getSound('phase_3/audio/bgm/tt_theme.mid')
    if music:
        music.setLoop(1)
        music.setVolume(0.9)
        music.play()
    
    print 'ToontownStart: Loading default gui sounds'
    DirectGuiGlobals.setDefaultRolloverSound(base.loadSfx('phase_3/audio/sfx/GUI_rollover.mp3'))
    DirectGuiGlobals.setDefaultClickSound(base.loadSfx('phase_3/audio/sfx/GUI_create_toon_fwd.mp3'))
else:
    music = true
serverVersion = base.config.GetString('server-version', 'no_version_set')
print 'ToontownStart: serverVersion: ', serverVersion
version = OnscreenText(serverVersion, pos = (-1.3, -0.97499999999999998), scale = 0.059999999999999998, fg = Vec4(0, 0, 1, 0.59999999999999998), align = TextNode.ALeft)
loader.beginBulkLoad('init', TTLocalizer.LoaderLabel, 138, 0, TTLocalizer.TIP_NONE)

from ToontownStart: starting... the game
from toontown.distributed = ToontownClientRepository
cr = ToontownClientRepository.ToontownClientRepository(serverVersion, launcher)
cr.music = music
del music
base.initNametagGlobals()
base.cr = cr
loader.endBulkLoad('init')
cr.generateGlobalObject(OTP_DO_ID_FRIEND_MANAGER, 'FriendManager')
if not launcher.isDummy():
    base.startShow(cr, launcher.getGameServer())
else:
    base.startShow(cr)
backgroundNodePath.reparentTo(hidden)
backgroundNodePath.removeNode()
del backgroundNodePath
del backgroundNode
del tempLoader
version.cleanup()
    except:
        from direct.showbase import PythonUtil
        print PythonUtil.describeException()
        raise
        class LogAndOutput:
    def __init__(self, orig, log):
        self.orig = orig
        self.log = log

    def write(self, str):
        self.log.write(str)
        self.log.flush()
        self.orig.write(str)
        self.orig.flush()

    def flush(self):
        self.log.flush()
        self.orig.flush()

class TTSLauncher:
    notify = DirectNotifyGlobal.directNotify.newCategory('TTSLauncher')

    def __init__(self):
        self.http = HTTPClient()

        self.logPrefix = 'stride-'

        ltime = 1 and time.localtime()
        logSuffix = '%02d%02d%02d_%02d%02d%02d' % (ltime[0] - 2000,  ltime[1], ltime[2], ltime[3], ltime[4], ltime[5])

        if not os.path.exists('user/logs/'):
            os.mkdir('user/logs/')
            self.notify.info('Made new directory to save logs.')

        logfile = os.path.join('user/logs', self.logPrefix + logSuffix + '.log')

        log = open(logfile, 'a')
        logOut = LogAndOutput(sys.stdout, log)
        logErr = LogAndOutput(sys.stderr, log)
        sys.stdout = logOut
        sys.stderr = logErr

    def getPlayToken(self):
        return self.getValue('TTS_PLAYCOOKIE')

    def getGameServer(self):
        return self.getValue('TTS_GAMESERVER')

    def getValue(self, key, default = None):
        return os.environ.get(key, default)

    def setPandaErrorCode(self):
        pass

    def setDisconnectDetails(self, disconnectCode, disconnectMsg):
        self.disconnectCode = disconnectCode
        self.disconnectMsg = disconnectMsg

    def setDisconnectDetailsNormal(self):
        self.setDisconnectDetails(0, 'normal')
        
