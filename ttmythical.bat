@echo off

cd ..

'title' 'Toontown Mythical'

from panda3d.core import *
from direct.directnotify import DirectNotifyGlobal
import os
import sys
import time

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

class TTLauncher:
    notify = DirectNotifyGlobal.directNotify.newCategory('TTLauncher')

    def __init__(self):
        self.http = HTTPClient()

        self.logPrefix = 'tt2-'

        ltime = 1 and time.localtime()
        logSuffix = '%02d%02d%02d_%02d%02d%02d' % (ltime[0] - 2000,  ltime[1], ltime[2], ltime[3], ltime[4], ltime[5])
	
    def loadDNAFile(self, dnastore, file):
        self.notify.info('Loading DNA file %s' % file)
        self.tick()
        
        if config.GetBool('use-libpandadna', False):
            f = Filename(str(file))
            f.setExtension('pdna')
            f = localizerAgent.findDNA(f)
            ret = C2.loadDNAFile(self, dnastore, f)
            
            if ret.getChild(0).getNumChildren() > 0:
                ret = ret.getChild(0).getChild(0).getNode(0)
                
            else:
                ret = None
            
        else:
            f = Filename(filename)
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
        return self.getValue('TT_PLAYCOOKIE')

    def getGameServer(self):
        return self.getValue('TT_GAMESERVER')

    def getValue(self, key, default = None):
        return os.environ.get(key, default)

    def setPandaErrorCode(self):
        pass
            f = Filename('etc/dnabkp/' + f.getBasename())
            ret = loadDNAFile(dnastore, f)
            
        self.notify.info('DNA file loaded')
        return ret
        
    def loadDNAFileAI(self, dnastore, filename):
        self.tick()
        
        f = Filename('../resources/' + str(filename))
        f.setExtension('pdna')
        return C2.loadDNAFileAI(self, dnastore, f)

    def beginBulkLoad(self, name, label, range, gui, tipCategory, zoneId):
        self._loadStartT = globalClock.getRealTime()
        Loader.Loader.notify.info("starting bulk load of block '%s'" % name)
        if self.inBulkBlock:
            Loader.Loader.notify.warning("Tried to start a block ('%s'), but am already in a block ('%s')" % (name, self.blockName))
            return None
        self.inBulkBlock = 1
	        self.loadingScreen.begin(range, label, gui, tipCategory, zoneId)

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
