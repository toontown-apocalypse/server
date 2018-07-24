import os
import sys
from toontown.toonbase import toontown.toonbase.CilentStart
from toontown.launcher import ToontownLauncher.py
from toontown.launcher import ToontownLoader.py
from toontown.launcher import __builtin__.py


__builtin__.process = 'client'


# Temporary hack patch:
__builtin__.__dict__.update(__import__('pandac.PandaModules', fromlist=['*']).__dict__)
from direct.extensions_native import HTTPChannel_extensions
from direct.extensions_native import Mat3_extensions
from direct.extensions_native import VBase3_extensions
from direct.extensions_native import VBase4_extensions
from direct.extensions_native import NodePath_extensions


from panda3d.core import loadPrcFile

if __debug__:
    loadPrcFile('config/general.prc')
    loadPrcFile('config/release/dev.prc')


from direct.directnotify.DirectNotifyGlobal import directNotify


notify = directNotify.newCategory('ClientStart')
notify.setInfo(True)


from otp.settings.Settings import Settings


preferencesFilename = ConfigVariableString(
    'preferences-filename', 'preferences.json').getValue()
notify.info('Reading %s...' % preferencesFilename)
__builtin__.settings = Settings(preferencesFilename)
if 'fullscreen' not in settings:
    settings['fullscreen'] = False
if 'music' not in settings:
    settings['music'] = True
if 'sfx' not in settings:
    settings['sfx'] = True
if 'musicVol' not in settings:
    settings['musicVol'] = 1.0
if 'sfxVol' not in settings:
    settings['sfxVol'] = 1.0
if 'loadDisplay' not in settings:
    settings['loadDisplay'] = 'pandagl'
if 'toonChatSounds' not in settings:
    settings['toonChatSounds'] = True
loadPrcFileData('Settings: res', 'win-size %d %d' % tuple(settings.get('res', (1280, 720))))
loadPrcFileData('Settings: fullscreen', 'fullscreen %s' % settings['fullscreen'])
loadPrcFileData('Settings: music', 'audio-music-active %s' % settings['music'])
loadPrcFileData('Settings: sfx', 'audio-sfx-active %s' % settings['sfx'])
loadPrcFileData('Settings: musicVol', 'audio-master-music-volume %s' % settings['musicVol'])
loadPrcFileData('Settings: sfxVol', 'audio-master-sfx-volume %s' % settings['sfxVol'])
loadPrcFileData('Settings: loadDisplay', 'load-display %s' % settings['loadDisplay'])
loadPrcFileData('Settings: toonChatSounds', 'toon-chat-sounds %s' % settings['toonChatSounds'])


import os

from toontown.toonbase.ContentPacksManager import ContentPackError
from toontown.toonbase.ContentPacksManager import ContentPacksManager


contentPacksFilepath = ConfigVariableString(
    'content-packs-filepath', 'contentpacks/').getValue()
contentPacksSortFilename = ConfigVariableString(
    'content-packs-sort-filename', 'sort.yaml').getValue()
if not os.path.exists(contentPacksFilepath):
    os.makedirs(contentPacksFilepath)
__builtin__.ContentPackError = ContentPackError
__builtin__.contentPacksMgr = ContentPacksManager(
    filepath=contentPacksFilepath, sortFilename=contentPacksSortFilename)
contentPacksMgr.applyAll()

import time
import sys
import random
import __builtin__
try:
    launcher
except:
    from toontown.launcher.TTILauncher import TTILauncher
    launcher = TTILauncher()
    __builtin__.launcher = launcher


notify.info('Starting the game...')
if launcher.isDummy():
    http = HTTPClient()
else:
    http = launcher.http
tempLoader = Loader()
backgroundNode = tempLoader.loadSync(Filename('phase_3/models/gui/loading-background'))
from direct.gui import DirectGuiGlobals
from direct.gui.DirectGui import *
notify.info('Setting the default font...')
import ToontownGlobals
DirectGuiGlobals.setDefaultFontFunc(ToontownGlobals.getInterfaceFont)
launcher.setPandaErrorCode(7)
import ToonBase
ToonBase.ToonBase()
from pandac.PandaModules import *
if base.win is None:
    notify.error('Unable to open window; aborting.')
launcher.setPandaErrorCode(0)
launcher.setPandaWindowOpen()
ConfigVariableDouble('decompressor-step-time').setValue(0.01)
ConfigVariableDouble('extractor-step-time').setValue(0.01)
backgroundNodePath = aspect2d.attachNewNode(backgroundNode, 0)
backgroundNodePath.setPos(0.0, 0.0, 0.0)
backgroundNodePath.setScale(render2d, VBase3(1))
backgroundNodePath.find('**/fg').hide()
logo = OnscreenImage(
    image='phase_3/maps/toontown-logo.png',
    scale=(1.2 / (4.0/3.0), 1, 1 / (4.0/3.0)),
    pos=(backgroundNodePath.find('**/fg').getX(), backgroundNodePath.find('**/fg').getY(), backgroundNodePath.find('**/fg').getZ() + 0.1))
logo.setTransparency(TransparencyAttrib.MAlpha)
logo.setBin('fixed', 20)
logo.reparentTo(backgroundNodePath)
backgroundNodePath.find('**/bg').setBin('fixed', 10)
base.graphicsEngine.renderFrame()
DirectGuiGlobals.setDefaultRolloverSound(base.loadSfx('phase_3/audio/sfx/GUI_rollover.ogg'))
DirectGuiGlobals.setDefaultClickSound(base.loadSfx('phase_3/audio/sfx/GUI_create_toon_fwd.ogg'))
DirectGuiGlobals.setDefaultDialogGeom(loader.loadModel('phase_3/models/gui/dialog_box_gui'))
import TTLocalizer
from otp.otpbase import OTPGlobals
OTPGlobals.setDefaultProductPrefix(TTLocalizer.ProductPrefix)
if base.musicManagerIsValid:
    themeList = ('phase_3/audio/bgm/tt_theme.ogg')
    music = base.loadMusic('phase_3/audio/bgm/tt_theme.ogg')
    if music:
        music.setLoop(1)
        music.setVolume(0.9)
        music.play()
    notify.info('Loading the default GUI sounds...')
    DirectGuiGlobals.setDefaultRolloverSound(base.loadSfx('phase_3/audio/sfx/GUI_rollover.ogg'))
    DirectGuiGlobals.setDefaultClickSound(base.loadSfx('phase_3/audio/sfx/GUI_create_toon_fwd.ogg'))
else:
    music = None
import ToontownLoader
from direct.gui.DirectGui import *
serverVersion = base.config.GetString('server-version', 'no_version_set')
version = OnscreenText(serverVersion, pos=(-1.3, -0.975), scale=0.06, fg=Vec4(1, 1, 1, 1), align=TextNode.ALeft)
version.setPos(0.03,0.03)
version.reparentTo(base.a2dBottomLeft)
powered = OnscreenText("Powered by Toontown Infinite", pos=(-1.3, -0.975), scale=0.06, fg=Vec4(0.5, 0.5, 1, 1), align=TextNode.ARight)
powered.setPos(-0.03,-0.06)
powered.reparentTo(base.a2dTopRight)
cred = OnscreenText("RynoGG", pos=(-1.3, -0.975), scale=0.06, fg=Vec4(1, 1, 1, 1), align=TextNode.ALeft)
cred.setPos(0.03,-0.06)
cred.reparentTo(base.a2dTopLeft)
from toontown.suit import Suit
Suit.loadModels()
loader.beginBulkLoad('init', TTLocalizer.LoaderLabel, 138, 0, TTLocalizer.TIP_NONE, 0)
from ToonBaseGlobal import *
from direct.showbase.MessengerGlobal import *
from toontown.distributed import ToontownClientRepository
cr = ToontownClientRepository.ToontownClientRepository(serverVersion, launcher)
cr.music = music
del music
base.initNametagGlobals()
base.cr = cr
loader.endBulkLoad('init')
from otp.friends import FriendManager
from otp.distributed.OtpDoGlobals import *
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
del version
powered.cleanup()
del powered
cred.cleanup()
del cred
base.loader = base.loader
__builtin__.loader = base.loader
autoRun = ConfigVariableBool('toontown-auto-run', 1)
if autoRun:
    try:
        run()
    except SystemExit:
        raise
    except:
        from direct.showbase import PythonUtil
        print PythonUtil.describeException()
        raise

class ToonBase(OTPBase.OTPBase):
    notify = DirectNotifyGlobal.directNotify.newCategory('ToonBase')

    def __init__(self):
        OTPBase.OTPBase.__init__(self)

        # First, build a list of all possible resolutions:
        self.resList = [(800, 450), (1280, 720), (1600, 900), (1920, 1080)]
        displayInfo = self.pipe.getDisplayInformation()
        for i in xrange(displayInfo.getTotalDisplayModes()):
            width = displayInfo.getDisplayModeWidth(i)
            height = displayInfo.getDisplayModeHeight(i)
            if (width, height) not in self.resList:
                self.resList.append((width, height))

        # Next, separate the resolutions by their ratio:
        self.resDict = {}
        for res in self.resList:
            width = float(res[0])
            height = float(res[1])
            ratio = round(width / height, 2)
            self.resDict.setdefault(ratio, []).append(res)

        # Get the native width, height and ratio:
        if sys.platform == 'win32':  # Use displayInfo.
            self.nativeWidth = 1280
            self.nativeHeight = 720
        elif sys.platform == 'darwin':
            self.nativeWidth = 800
            self.nativeHeight = 600
        else:  # Use PyGTK.
            import gtk
            self.nativeWidth = gtk.gdk.screen_width()
            self.nativeHeight = gtk.gdk.screen_height()
        self.nativeRatio = round(
            float(self.nativeWidth) / float(self.nativeHeight), 2)

        # Finally, choose the best resolution if we're either fullscreen, or
        # don't have one defined in our preferences:
        fullscreen = settings.get('fullscreen', False)
        if ('res' not in settings) or fullscreen:
            if fullscreen:
                # If we're fullscreen, we want to fit the entire screen:
                res = (self.nativeWidth, self.nativeHeight)
            elif len(self.resDict[self.nativeRatio]) > 1:
                # We have resolutions that match our native ratio and fit it!
                # Let's use one:
                res = sorted(self.resDict[self.nativeRatio])[0]
            else:
                # Okay, we don't have any resolutions that match our native
                # ratio and fit it (besides the native resolution itself, of
                # course). Let's just use one of the second largest ratio's
                # resolutions:
                ratios = sorted(self.resDict.keys(), reverse=False)
                nativeIndex = ratios.index(self.nativeRatio)
                res = sorted(self.resDict[ratios[nativeIndex - 1]])[0]

            # Store our result:
            settings['res'] = res

            # Reload the graphics pipe:
            properties = WindowProperties()

            properties.setSize(res[0], res[1])
            properties.setFullscreen(fullscreen)
            properties.setParentWindow(0)

            # Store the window sort for later:
            sort = self.win.getSort()

            if self.win:
                currentProperties = WindowProperties(self.win.getProperties())
                gsg = self.win.getGsg()
            else:
                currentProperties = WindowProperties.getDefault()
                gsg = None
            newProperties = WindowProperties(currentProperties)
            newProperties.addProperties(properties)
            if (gsg is None) or (currentProperties.getFullscreen() != newProperties.getFullscreen()) or (currentProperties.getParentWindow() != newProperties.getParentWindow()):
                self.openMainWindow(props=properties, gsg=gsg, keepCamera=True)
                self.graphicsEngine.openWindows()
                self.disableShowbaseMouse()
            else:
                self.win.requestProperties(properties)
                self.graphicsEngine.renderFrame()

            self.win.setSort(sort)
            self.graphicsEngine.renderFrame()
            self.graphicsEngine.renderFrame()
        self.disableShowbaseMouse()
        self.addCullBins()
        self.debugRunningMultiplier /= OTPGlobals.ToonSpeedFactor
        self.baseXpMultiplier = self.config.GetFloat('base-xp-multiplier', 1.0)
        self.toonChatSounds = self.config.GetBool('toon-chat-sounds', 1)
        self.placeBeforeObjects = self.config.GetBool('place-before-objects', 1)
        self.endlessQuietZone = False
        self.wantDynamicShadows = 0
        self.exitErrorCode = 0
        camera.setPosHpr(0, 0, 0, 0, 0, 0)
        self.camLens.setMinFov(ToontownGlobals.DefaultCameraFov/(4./3.))
        self.camLens.setNearFar(ToontownGlobals.DefaultCameraNear, ToontownGlobals.DefaultCameraFar)
        self.musicManager.setVolume(0.65)
        self.setBackgroundColor(ToontownGlobals.DefaultBackgroundColor)
        tpm = TextPropertiesManager.getGlobalPtr()
        candidateActive = TextProperties()
        candidateActive.setTextColor(0, 0, 1, 1)
        tpm.setProperties('candidate_active', candidateActive)
        candidateInactive = TextProperties()
        candidateInactive.setTextColor(0.3, 0.3, 0.7, 1)
        tpm.setProperties('candidate_inactive', candidateInactive)
        self.transitions.IrisModelName = 'phase_3/models/misc/iris'
        self.transitions.FadeModelName = 'phase_3/models/misc/fade'
        self.exitFunc = self.userExit
        if 'launcher' in __builtins__ and launcher:
            launcher.setPandaErrorCode(11)
        globalClock.setMaxDt(0.2)
        if self.config.GetBool('want-particles', 1) == 1:
            self.notify.debug('Enabling particles')
            self.enableParticles()

        self.accept(ToontownGlobals.ScreenshotHotkey, self.takeScreenShot)

        # OS X Specific Actions
        if platform == "darwin":
            self.acceptOnce(ToontownGlobals.QuitGameHotKeyOSX, self.exitOSX)
            self.accept(ToontownGlobals.QuitGameHotKeyRepeatOSX, self.exitOSX)
            self.acceptOnce(ToontownGlobals.HideGameHotKeyOSX, self.hideGame)
            self.accept(ToontownGlobals.HideGameHotKeyRepeatOSX, self.hideGame)
            self.acceptOnce(ToontownGlobals.MinimizeGameHotKeyOSX, self.minimizeGame)
            self.accept(ToontownGlobals.MinimizeGameHotKeyRepeatOSX, self.minimizeGame)

        self.accept('f3', self.toggleGui)
        self.accept('f4', self.toggleOobe)
        self.accept('panda3d-render-error', self.panda3dRenderError)
        oldLoader = self.loader
        self.loader = ToontownLoader.ToontownLoader(self)
        __builtins__['loader'] = self.loader
        oldLoader.destroy()
        self.accept('PandaPaused', self.disableAllAudio)
        self.accept('PandaRestarted', self.enableAllAudio)
        self.friendMode = self.config.GetBool('switchboard-friends', 0)
        self.wantPets = self.config.GetBool('want-pets', 1)
        self.wantBingo = self.config.GetBool('want-fish-bingo', 1)
        self.wantKarts = self.config.GetBool('want-karts', 1)
        self.wantNewSpecies = self.config.GetBool('want-new-species', 0)
        self.wantAchievements = self.config.GetBool('want-achievements', 1)
        self.inactivityTimeout = self.config.GetFloat('inactivity-timeout', ToontownGlobals.KeyboardTimeout)
        if self.inactivityTimeout:
            self.notify.debug('Enabling Panda timeout: %s' % self.inactivityTimeout)
            self.mouseWatcherNode.setInactivityTimeout(self.inactivityTimeout)
        self.mouseWatcherNode.setEnterPattern('mouse-enter-%r')
        self.mouseWatcherNode.setLeavePattern('mouse-leave-%r')
        self.mouseWatcherNode.setButtonDownPattern('button-down-%r')
        self.mouseWatcherNode.setButtonUpPattern('button-up-%r')
        self.randomMinigameAbort = self.config.GetBool('random-minigame-abort', 0)
        self.randomMinigameDisconnect = self.config.GetBool('random-minigame-disconnect', 0)
        self.randomMinigameNetworkPlugPull = self.config.GetBool('random-minigame-netplugpull', 0)
        self.autoPlayAgain = self.config.GetBool('auto-play-again', 0)
        self.skipMinigameReward = self.config.GetBool('skip-minigame-reward', 0)
        self.wantMinigameDifficulty = self.config.GetBool('want-minigame-difficulty', 0)
        self.minigameDifficulty = self.config.GetFloat('minigame-difficulty', -1.0)
        if self.minigameDifficulty == -1.0:
            del self.minigameDifficulty
        self.minigameSafezoneId = self.config.GetInt('minigame-safezone-id', -1)
        if self.minigameSafezoneId == -1:
            del self.minigameSafezoneId
        cogdoGameSafezoneId = self.config.GetInt('cogdo-game-safezone-id', -1)
        cogdoGameDifficulty = self.config.GetFloat('cogdo-game-difficulty', -1)
        if cogdoGameDifficulty != -1:
            self.cogdoGameDifficulty = cogdoGameDifficulty
        if cogdoGameSafezoneId != -1:
            self.cogdoGameSafezoneId = cogdoGameSafezoneId
        ToontownBattleGlobals.SkipMovie = self.config.GetBool('skip-battle-movies', 0)
        self.creditCardUpFront = self.config.GetInt('credit-card-up-front', -1)
        if self.creditCardUpFront == -1:
            del self.creditCardUpFront
        else:
            self.creditCardUpFront = self.creditCardUpFront != 0
        self.housingEnabled = self.config.GetBool('want-housing', 1)
        self.cannonsEnabled = self.config.GetBool('estate-cannons', 0)
        self.fireworksEnabled = self.config.GetBool('estate-fireworks', 0)
        self.dayNightEnabled = self.config.GetBool('estate-day-night', 0)
        self.cloudPlatformsEnabled = self.config.GetBool('estate-clouds', 0)
        self.greySpacing = self.config.GetBool('allow-greyspacing', 0)
        self.goonsEnabled = self.config.GetBool('estate-goon', 0)
        self.restrictTrialers = self.config.GetBool('restrict-trialers', 1)
        self.roamingTrialers = self.config.GetBool('roaming-trialers', 1)
        self.slowQuietZone = self.config.GetBool('slow-quiet-zone', 0)
        self.slowQuietZoneDelay = self.config.GetFloat('slow-quiet-zone-delay', 5)
        self.killInterestResponse = self.config.GetBool('kill-interest-response', 0)
        self.forceSkipTutorial = self.config.GetBool('force-skip-tutorial', 0)
        tpMgr = TextPropertiesManager.getGlobalPtr()
        WLDisplay = TextProperties()
        WLDisplay.setSlant(0.3)
        WLEnter = TextProperties()
        WLEnter.setTextColor(1.0, 0.0, 0.0, 1)
        tpMgr.setProperties('WLDisplay', WLDisplay)
        tpMgr.setProperties('WLEnter', WLEnter)
        del tpMgr
        self.lastScreenShotTime = globalClock.getRealTime()
        self.accept('InputState-forward', self.__walking)
        self.canScreenShot = 1
        self.glitchCount = 0
        self.walking = 0
        self.oldX = max(1, base.win.getXSize())
        self.oldY = max(1, base.win.getYSize())
        self.aspectRatio = float(self.oldX) / self.oldY
        self.localAvatarStyle = None

        self.filters = CommonFilters(self.win, self.cam)

        # Free black/white Toons:
        self.wantYinYang = config.GetBool('want-yin-yang', False)

    def openMainWindow(self, *args, **kw):
        result = OTPBase.OTPBase.openMainWindow(self, *args, **kw)
        self.setCursorAndIcon()
        return result

    def windowEvent(self, win):
        OTPBase.OTPBase.windowEvent(self, win)

        MarginGlobals.updateMarginVisibles()

    def setCursorAndIcon(self):
        tempdir = tempfile.mkdtemp()
        atexit.register(shutil.rmtree, tempdir)
        vfs = VirtualFileSystem.getGlobalPtr()

        searchPath = DSearchPath()
        if __debug__:
            searchPath.appendDirectory(Filename('resources/phase_3/etc'))
        searchPath.appendDirectory(Filename('/phase_3/etc'))

        for filename in ['toonmono.cur', 'icon.ico']:
            p3filename = Filename(filename)
            found = vfs.resolveFilename(p3filename, searchPath)
            if not found:
                return # Can't do anything past this point.

            with open(os.path.join(tempdir, filename), 'wb') as f:
                f.write(vfs.readFile(p3filename, False))

        wp = WindowProperties()
        wp.setCursorFilename(Filename.fromOsSpecific(os.path.join(tempdir, 'toonmono.cur')))
        wp.setIconFilename(Filename.fromOsSpecific(os.path.join(tempdir, 'icon.ico')))
        self.win.requestProperties(wp)

    def addCullBins(self):
        cbm = CullBinManager.getGlobalPtr()
        cbm.addBin('ground', CullBinManager.BTUnsorted, 18)
        cbm.addBin('shadow', CullBinManager.BTBackToFront, 19)
        cbm.addBin('gui-popup', CullBinManager.BTUnsorted, 60)

    def disableShowbaseMouse(self):
        self.useDrive()
        self.disableMouse()
        if self.mouseInterface: self.mouseInterface.detachNode()
        if self.mouse2cam: self.mouse2cam.detachNode()

    def __walking(self, pressed):
        self.walking = pressed

    def toggleGui(self):
        if aspect2d.isHidden():
            aspect2d.show()
        else:
            aspect2d.hide()
    
    def toggleOobe(self):
        base.oobe()

    def takeScreenShot(self):
        if not os.path.exists(TTLocalizer.ScreenshotPath):
            os.mkdir(TTLocalizer.ScreenshotPath)
            self.notify.info('Made new directory to save screenshots.')

        namePrefix = TTLocalizer.ScreenshotPath + launcher.logPrefix + 'screenshot'
        timedif = globalClock.getRealTime() - self.lastScreenShotTime
        if self.glitchCount > 10 and self.walking:
            return
        if timedif < 1.0 and self.walking:
            self.glitchCount += 1
            return
        if not hasattr(self, 'localAvatar'):
            self.screenshot(namePrefix=namePrefix)
            self.lastScreenShotTime = globalClock.getRealTime()
            return
        coordOnScreen = self.config.GetBool('screenshot-coords', 0)
        self.localAvatar.stopThisFrame = 1
        ctext = self.localAvatar.getAvPosStr()
        self.screenshotStr = ''
        messenger.send('takingScreenshot')
        if coordOnScreen:
            coordTextLabel = DirectLabel(pos=(-0.81, 0.001, -0.87), text=ctext, text_scale=0.05, text_fg=VBase4(1.0, 1.0, 1.0, 1.0), text_bg=(0, 0, 0, 0), text_shadow=(0, 0, 0, 1), relief=None)
            coordTextLabel.setBin('gui-popup', 0)
            strTextLabel = None
            if len(self.screenshotStr):
                strTextLabel = DirectLabel(pos=(0.0, 0.001, 0.9), text=self.screenshotStr, text_scale=0.05, text_fg=VBase4(1.0, 1.0, 1.0, 1.0), text_bg=(0, 0, 0, 0), text_shadow=(0, 0, 0, 1), relief=None)
                strTextLabel.setBin('gui-popup', 0)
        self.graphicsEngine.renderFrame()
        self.screenshot(namePrefix=namePrefix, imageComment=ctext + ' ' + self.screenshotStr)
        self.lastScreenShotTime = globalClock.getRealTime()
        if coordOnScreen:
            if strTextLabel is not None:
                strTextLabel.destroy()
            coordTextLabel.destroy()
        return

    def addScreenshotString(self, str):
        if len(self.screenshotStr):
            self.screenshotStr += '\n'
        self.screenshotStr += str

    def initNametagGlobals(self):
        NametagGlobals.setMe(base.cam)

        NametagGlobals.setCardModel('phase_3/models/props/panel.bam')
        NametagGlobals.setArrowModel('phase_3/models/props/arrow.bam')
        NametagGlobals.setChatBalloon3dModel('phase_3/models/props/chatbox.bam')
        NametagGlobals.setChatBalloon2dModel('phase_3/models/props/chatbox_noarrow.bam')
        NametagGlobals.setThoughtBalloonModel('phase_3/models/props/chatbox_thought_cutout.bam')

        chatButtonGui = loader.loadModel('phase_3/models/gui/chat_button_gui.bam')
        NametagGlobals.setPageButton(
            chatButtonGui.find('**/Horiz_Arrow_UP'), chatButtonGui.find('**/Horiz_Arrow_DN'),
            chatButtonGui.find('**/Horiz_Arrow_Rllvr'), chatButtonGui.find('**/Horiz_Arrow_UP'))
        NametagGlobals.setQuitButton(
            chatButtonGui.find('**/CloseBtn_UP'), chatButtonGui.find('**/CloseBtn_DN'),
            chatButtonGui.find('**/CloseBtn_Rllvr'), chatButtonGui.find('**/CloseBtn_UP'))
        chatButtonGui.removeNode()

        rolloverSound = DirectGuiGlobals.getDefaultRolloverSound()
        if rolloverSound is not None:
            NametagGlobals.setRolloverSound(rolloverSound)
        clickSound = DirectGuiGlobals.getDefaultClickSound()
        if clickSound is not None:
            NametagGlobals.setClickSound(clickSound)

        self.marginManager = MarginManager()
        self.margins = self.aspect2d.attachNewNode(
            self.marginManager, DirectGuiGlobals.MIDGROUND_SORT_INDEX + 1)
        self.leftCells = [
            self.marginManager.addCell(0.1, -0.6, self.a2dTopLeft),
            self.marginManager.addCell(0.1, -1.0, self.a2dTopLeft),
            self.marginManager.addCell(0.1, -1.4, self.a2dTopLeft)
        ]
        self.bottomCells = [
            self.marginManager.addCell(0.4, 0.1, self.a2dBottomCenter),
            self.marginManager.addCell(-0.4, 0.1, self.a2dBottomCenter),
            self.marginManager.addCell(-1.0, 0.1, self.a2dBottomCenter),
            self.marginManager.addCell(1.0, 0.1, self.a2dBottomCenter)
        ]
        self.rightCells = [
            self.marginManager.addCell(-0.1, -0.6, self.a2dTopRight),
            self.marginManager.addCell(-0.1, -1.0, self.a2dTopRight),
            self.marginManager.addCell(-0.1, -1.4, self.a2dTopRight)
        ]

    def setCellsActive(self, cells, active):
        for cell in cells:
            cell.setActive(active)
        self.marginManager.reorganize()

    def cleanupDownloadWatcher(self):
        self.downloadWatcher.cleanup()
        self.downloadWatcher = None

    def startShow(self, cr, launcherServer = None):
        self.cr = cr
        base.graphicsEngine.renderFrame()
        self.downloadWatcher = ToontownDownloadWatcher.ToontownDownloadWatcher(TTLocalizer.LauncherPhaseNames)
        if launcher.isDownloadComplete():
            self.cleanupDownloadWatcher()
        else:
            self.acceptOnce('launcherAllPhasesComplete', self.cleanupDownloadWatcher)
        gameServer = os.environ.get('TTI_GAMESERVER', 'localhost')
        # Get the base port.
        serverPort = base.config.GetInt('server-port', 7199)

        # Get the number of client-agents.
        clientagents = base.config.GetInt('client-agents', 1) - 1

        # Get a new port.
        serverPort += (random.randint(0, clientagents) * 100)

        serverList = []
        for name in gameServer.split(';'):
            url = URLSpec(name, 1)
            if base.config.GetBool('server-force-ssl', False):
                url.setScheme('s')
            if not url.hasPort():
                url.setPort(serverPort)
            serverList.append(url)

        if len(serverList) == 1:
            failover = base.config.GetString('server-failover', '')
            serverURL = serverList[0]
            for arg in failover.split():
                try:
                    port = int(arg)
                    url = URLSpec(serverURL)
                    url.setPort(port)
                except:
                    url = URLSpec(arg, 1)

                if url != serverURL:
                    serverList.append(url)

        cr.loginFSM.request('connect', [serverList])
        self.ttAccess = ToontownAccess.ToontownAccess()
        self.ttAccess.initModuleInfo()

        # Start detecting speed hacks:
        self.lastSpeedHackCheck = time.time()
        self.lastTrueClockTime = TrueClock.getGlobalPtr().getLongTime()
        taskMgr.add(self.__speedHackCheckTick, 'speedHackCheck-tick')
        
        

    def __speedHackCheckTick(self, task):
        elapsed = time.time() - self.lastSpeedHackCheck
        tcElapsed = TrueClock.getGlobalPtr().getLongTime() - self.lastTrueClockTime

        if tcElapsed > (elapsed + 0.05):
            # The TrueClock is running faster than it should. This means the
            # player may have sped up the process. Disconnect them:
            self.cr.stopReaderPollTask()
            self.cr.lostConnection()
            return task.done

        self.lastSpeedHackCheck = time.time()
        self.lastTrueClockTime = TrueClock.getGlobalPtr().getLongTime()

        return task.cont

    def removeGlitchMessage(self):
        self.ignore('InputState-forward')

    def exitShow(self, errorCode = None):
        self.notify.info('Exiting Toontown: errorCode = %s' % errorCode)
        if errorCode:
            launcher.setPandaErrorCode(errorCode)
        else:
            launcher.setPandaErrorCode(0)
        sys.exit()

    def setExitErrorCode(self, code):
        self.exitErrorCode = code
        if os.name == 'nt':
            exitCode2exitPage = {OTPLauncherGlobals.ExitEnableChat: 'chat',
             OTPLauncherGlobals.ExitSetParentPassword: 'setparentpassword',
             OTPLauncherGlobals.ExitPurchase: 'purchase'}
            if code in exitCode2exitPage:
                launcher.setRegistry('EXIT_PAGE', exitCode2exitPage[code])

    def getExitErrorCode(self):
        return self.exitErrorCode

    def userExit(self):
        try:
            self.localAvatar.d_setAnimState('TeleportOut', 1)
        except:
            pass

        if hasattr(self, 'ttAccess'):
            self.ttAccess.delete()
        if self.cr.timeManager:
            self.cr.timeManager.setDisconnectReason(ToontownGlobals.DisconnectCloseWindow)
        base.cr._userLoggingOut = False
        try:
            localAvatar
        except:
            pass
        else:
            messenger.send('clientLogout')
            self.cr.dumpAllSubShardObjects()

        self.cr.loginFSM.request('shutdown')
        self.notify.warning('Could not request shutdown; exiting anyway.')
        self.ignore(ToontownGlobals.QuitGameHotKeyOSX)
        self.ignore(ToontownGlobals.QuitGameHotKeyRepeatOSX)
        self.ignore(ToontownGlobals.HideGameHotKeyOSX)
        self.ignore(ToontownGlobals.HideGameHotKeyRepeatOSX)
        self.ignore(ToontownGlobals.MinimizeGameHotKeyOSX)
        self.ignore(ToontownGlobals.MinimizeGameHotKeyRepeatOSX)
        self.exitShow()

    def panda3dRenderError(self):
        launcher.setPandaErrorCode(14)
        if self.cr.timeManager:
            self.cr.timeManager.setDisconnectReason(ToontownGlobals.DisconnectGraphicsError)
        self.cr.sendDisconnect()
        sys.exit()

    def getShardPopLimits(self):
        return (
            config.GetInt('shard-low-pop', ToontownGlobals.LOW_POP),
            config.GetInt('shard-mid-pop', ToontownGlobals.MID_POP),
            config.GetInt('shard-high-pop', ToontownGlobals.HIGH_POP)
        )

    def playMusic(self, music, looping = 0, interrupt = 1, volume = None, time = 0.0):
        OTPBase.OTPBase.playMusic(self, music, looping, interrupt, volume, time)

    # OS X Specific Actions
    def exitOSX(self):
        self.confirm = TTDialog.TTGlobalDialog(doneEvent='confirmDone', message=TTLocalizer.OptionsPageExitConfirm, style=TTDialog.TwoChoice)
        self.confirm.show()
        self.accept('confirmDone', self.handleConfirm)

    def handleConfirm(self):
        status = self.confirm.doneStatus
        self.ignore('confirmDone')
        self.confirm.cleanup()
        del self.confirm
        if status == 'ok':
            self.userExit()

    def hideGame(self):
        # Hacky, I know, but it works
        hideCommand = """osascript -e 'tell application "System Events"
                                            set frontProcess to first process whose frontmost is true
                                            set visible of frontProcess to false
                                       end tell'"""
        os.system(hideCommand)

    def minimizeGame(self):
        wp = WindowProperties()
        wp.setMinimized(True)
        base.win.requestProperties(wp)
from pandac.PandaModules import *
from direct.directnotify.DirectNotifyGlobal import *
from direct.showbase import Loader
from toontown.toontowngui import ToontownLoadingScreen
from toontown.dna.DNAParser import *

class ToontownLoader(Loader.Loader):
    TickPeriod = 0.2

    def __init__(self, base):
        Loader.Loader.__init__(self, base)
        self.inBulkBlock = None
        self.blockName = None
        self.loadingScreen = ToontownLoadingScreen.ToontownLoadingScreen()
        return

    def destroy(self):
        self.loadingScreen.destroy()
        del self.loadingScreen
        Loader.Loader.destroy(self)

    def loadDNAFile(self, dnastore, filename):
        return loadDNAFile(dnastore, filename)

    def beginBulkLoad(self, name, label, range, gui, tipCategory, zoneId):
        self._loadStartT = globalClock.getRealTime()
        Loader.Loader.notify.info("starting bulk load of block '%s'" % name)
        if self.inBulkBlock:
            Loader.Loader.notify.warning("Tried to start a block ('%s'), but am already in a block ('%s')" % (name, self.blockName))
            return None
        self.inBulkBlock = 1
        self._lastTickT = globalClock.getRealTime()
        self.blockName = name
        self.loadingScreen.begin(range, label, gui, tipCategory, zoneId)
        return None

    def endBulkLoad(self, name):
        if not self.inBulkBlock:
            Loader.Loader.notify.warning("Tried to end a block ('%s'), but not in one" % name)
            return None
        if name != self.blockName:
            Loader.Loader.notify.warning("Tried to end a block ('%s'), other then the current one ('%s')" % (name, self.blockName))
            return None
        self.inBulkBlock = None
        expectedCount, loadedCount = self.loadingScreen.end()
        now = globalClock.getRealTime()
        Loader.Loader.notify.info("At end of block '%s', expected %s, loaded %s, duration=%s" % (self.blockName,
         expectedCount,
         loadedCount,
         now - self._loadStartT))
        return

    def abortBulkLoad(self):
        if self.inBulkBlock:
            Loader.Loader.notify.info("Aborting block ('%s')" % self.blockName)
            self.inBulkBlock = None
            self.loadingScreen.abort()
        return

    def tick(self):
        if self.inBulkBlock:
            now = globalClock.getRealTime()
            if now - self._lastTickT > self.TickPeriod:
                self._lastTickT += self.TickPeriod
                self.loadingScreen.tick()
                try:
                    base.cr.considerHeartbeat()
                except:
                    pass

    def loadModel(self, *args, **kw):
        ret = Loader.Loader.loadModel(self, *args, **kw)
        if ret:
            gsg = base.win.getGsg()
            if gsg:
                ret.prepareScene(gsg)
        self.tick()
        return ret

    def loadFont(self, *args, **kw):
        ret = Loader.Loader.loadFont(self, *args, **kw)
        self.tick()
        return ret

    def loadTexture(self, texturePath, alphaPath = None, okMissing = False):
        ret = Loader.Loader.loadTexture(self, texturePath, alphaPath, okMissing=okMissing)
        self.tick()
        if alphaPath:
            self.tick()
        return ret

    def pdnaModel(self, *args, **kw):
        ret = Loader.Loader.loadModel(self, *args, **kw)
        if ret:
            gsg = base.win.getGsg()
            if gsg:
                ret.prepareScene(gsg)
        return ret

    def pdnaFont(self, *args, **kw):
        return Loader.Loader.loadFont(self, *args, **kw)

    def pdnaTexture(self, texturePath, alphaPath = None, okMissing = False):
        return Loader.Loader.loadTexture(self, texturePath, alphaPath, okMissing=okMissing)

    def loadSfx(self, soundPath):
        ret = Loader.Loader.loadSfx(self, soundPath)
        self.tick()
        return ret

    def loadMusic(self, soundPath):
        ret = Loader.Loader.loadMusic(self, soundPath)
        self.tick()
        return ret
ltime = 1 and time.localtime()
logSuffix = '%02d%02d%02d_%02d%02d%02d' % (ltime[0] - 2000,  ltime[1], ltime[2],
                                           ltime[3], ltime[4], ltime[5])

logfile = 'toontownD-' + logSuffix + '.log'

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

log = open(logfile, 'a')
logOut = LogAndOutput(sys.__stdout__, log)
logErr = LogAndOutput(sys.__stderr__, log)
sys.stdout = logOut
sys.stderr = logErr

print('\n\nStarting Toontown...')

if 1:
    print 'Current time: ' + time.asctime(time.localtime(time.time())) + ' ' + time.tzname[0]
    print 'sys.path = ', sys.path
    print 'sys.argv = ', sys.argv

from otp.launcher.LauncherBase import LauncherBase
from otp.otpbase import OTPLauncherGlobals
from panda3d.core import *
from toontown.toonbase import TTLocalizer

class ToontownLauncher(LauncherBase):
    GameName = 'Toontown'
    LauncherPhases = [3, 3.5, 4, 5, 5.5, 6, 7, 8, 9, 10, 11, 12, 13]
    TmpOverallMap = [0.25, 0.15, 0.12, 0.17, 0.08, 0.07, 0.05, 0.05, 0.017,
                     0.011, 0.01, 0.012, 0.01]
    RegistryKey = 'Software\\Disney\\Disney Online\\Toontown'
    ForegroundSleepTime = 0.01
    Localizer = TTLocalizer
    VerifyFiles = 1
    DecompressMultifiles = True

    def __init__(self):
        if sys.argv[2] == 'Phase2.py':
            sys.argv = sys.argv[:1] + sys.argv[3:]
        if len(sys.argv) == 5 or len(sys.argv) == 6:
            self.gameServer = sys.argv[2]
            self.accountServer = sys.argv[3]
            self.testServerFlag = int(sys.argv[4])
        else:
            print 'Error: Launcher: incorrect number of parameters'
            sys.exit()

        self.toontownBlueKey = 'TOONTOWN_BLUE'
        self.toontownPlayTokenKey = 'TTI_PLAYCOOKIE'
        self.launcherMessageKey = 'LAUNCHER_MESSAGE'
        self.game1DoneKey = 'GAME1_DONE'
        self.game2DoneKey = 'GAME2_DONE'
        self.tutorialCompleteKey = 'TUTORIAL_DONE'
        self.toontownRegistryKey = 'Software\\Disney\\Disney Online\\Toontown'
        if self.testServerFlag:
            self.toontownRegistryKey = '%s%s' % (self.toontownRegistryKey, 'Test')
        self.toontownRegistryKey = '%s%s' % (self.toontownRegistryKey, self.getProductName())
        LauncherBase.__init__(self)
        self.webAcctParams = 'WEB_ACCT_PARAMS'
        self.parseWebAcctParams()
        self.mainLoop()

    def getValue(self, key, default=None):
        try:
            return self.getRegistry(key, default)
        except:
            return self.getRegistry(key)

    def setValue(self, key, value):
        self.setRegistry(key, value)

    def getVerifyFiles(self):
        return 1

    def getTestServerFlag(self):
        return self.testServerFlag

    def getGameServer(self):
        return self.gameServer

    def getLogFileName(self):
        return 'toontown'

    def parseWebAcctParams(self):
        s = config.GetString('fake-web-acct-params', '')
        if not s:
            s = self.getRegistry(self.webAcctParams)
        self.setRegistry(self.webAcctParams, '')
        l = s.split('&')
        length = len(l)
        dict = {}
        for index in xrange(0, len(l)):
            args = l[index].split('=')
            if len(args) == 3:
                [name, value] = args[-2:]
                dict[name] = int(value)
            elif len(args) == 2:
                [name, value] = args
                dict[name] = int(value)

        self.secretNeedsParentPasswordKey = 1
        if 'secretsNeedsParentPassword' in dict:
            self.secretNeedsParentPasswordKey = dict['secretsNeedsParentPassword']
        else:
            self.notify.warning('no secretNeedsParentPassword token in webAcctParams')
        self.notify.info('secretNeedsParentPassword = %d' % self.secretNeedsParentPasswordKey)

        self.chatEligibleKey = 0
        if 'chatEligible' in dict:
            self.chatEligibleKey = dict['chatEligible']
        else:
            self.notify.warning('no chatEligible token in webAcctParams')
        self.notify.info('chatEligibleKey = %d' % self.chatEligibleKey)

    def getBlue(self):
        blue = self.getValue(self.toontownBlueKey)
        self.setValue(self.toontownBlueKey, '')
        if blue == 'NO BLUE':
            blue = None
        return blue

    def getPlayToken(self):
        playToken = self.getValue(self.toontownPlayTokenKey)
        self.setValue(self.toontownPlayTokenKey, '')
        if playToken == 'NO PLAYTOKEN':
            playToken = None
        return playToken

    def setRegistry(self, name, value):
        if not self.WIN32:
            return

        t = type(value)
        if t == types.IntType:
            WindowsRegistry.setIntValue(self.toontownRegistryKey, name, value)
        elif t == types.StringType:
            WindowsRegistry.setStringValue(self.toontownRegistryKey, name, value)
        else:
            self.notify.warning('setRegistry: Invalid type for registry value: ' + `value`)

    def getRegistry(self, name, missingValue=None):
        self.notify.info('getRegistry%s' % ((name, missingValue),))
        if not self.WIN32:
            if missingValue == None:
                missingValue = ''
            value = os.environ.get(name, missingValue)
            try:
                value = int(value)
            except: pass
            return value

        t = WindowsRegistry.getKeyType(self.toontownRegistryKey, name)
        if t == WindowsRegistry.TInt:
            if missingValue == None:
                missingValue = 0
            return WindowsRegistry.getIntValue(self.toontownRegistryKey,
                                                name, missingValue)
        elif t == WindowsRegistry.TString:
            if missingValue == None:
                missingValue = ''
            return WindowsRegistry.getStringValue(self.toontownRegistryKey,
                                                    name, missingValue)
        else:
            return missingValue

    def getCDDownloadPath(self, origPath, serverFilePath):
        return '%s/%s%s/CD_%d/%s' % (origPath, self.ServerVersion, self.ServerVersionSuffix, self.fromCD, serverFilePath)

    def getDownloadPath(self, origPath, serverFilePath):
        return '%s/%s%s/%s' % (origPath, self.ServerVersion, self.ServerVersionSuffix, serverFilePath)

    def getPercentPatchComplete(self, bytesWritten):
        if self.totalPatchDownload:
            return LauncherBase.getPercentPatchComplete(self, bytesWritten)
        else:
            return 0

    def hashIsValid(self, serverHash, hashStr):
        return serverHash.setFromDec(hashStr) or serverHash.setFromHex(hashStr)

    def launcherMessage(self, msg):
        LauncherBase.launcherMessage(self, msg)
        self.setRegistry(self.launcherMessageKey, msg)

    def getAccountServer(self):
        return self.accountServer

    def setTutorialComplete(self):
        self.setRegistry(self.tutorialCompleteKey, 0)

    def getTutorialComplete(self):
        return self.getRegistry(self.tutorialCompleteKey, 0)

    def getGame2Done(self):
        return self.getRegistry(self.game2DoneKey, 0)

    def setPandaErrorCode(self, code):
        self.pandaErrorCode = code
        if self.WIN32:
            self.notify.info('setting panda error code to %s' % code)
            exitCode2exitPage = {
                OTPLauncherGlobals.ExitEnableChat: 'chat',
                OTPLauncherGlobals.ExitSetParentPassword: 'setparentpassword',
                OTPLauncherGlobals.ExitPurchase: 'purchase'}
            if code in exitCode2exitPage:
                self.setRegistry('EXIT_PAGE', exitCode2exitPage[code])
                self.setRegistry(self.PandaErrorCodeKey, 0)
            else:
                self.setRegistry(self.PandaErrorCodeKey, code)
        else:
            LauncherBase.setPandaErrorCode(self, code)

    def getNeedPwForSecretKey(self):
        return self.secretNeedsParentPasswordKey

    def getParentPasswordSet(self):
        return self.chatEligibleKey

    def MakeNTFSFilesGlobalWriteable(self, pathToSet=None):
        if not self.WIN32:
            return
        LauncherBase.MakeNTFSFilesGlobalWriteable(self, pathToSet)

    def startGame(self):
        try:
            os.remove('Phase3.py')
        except: pass

        import Phase3

        self.newTaskManager()

        from direct.showbase.EventManagerGlobal import eventMgr
        eventMgr.restart()

        from toontown.toonbase import ToontownStart
pause

goto server
