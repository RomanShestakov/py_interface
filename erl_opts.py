### py_interface -- A Python-implementation of an Erlang node
###
### $Id$
###
### Copyright (C) 2002  Tomas Abrahamsson
###
### Author: Tomas Abrahamsson <tab@lysator.liu.se>
### 
### This file is part of the Py-Interface library
###
### This library is free software; you can redistribute it and/or
### modify it under the terms of the GNU Library General Public
### License as published by the Free Software Foundation; either
### version 2 of the License, or (at your option) any later version.
### 
### This library is distributed in the hope that it will be useful,
### but WITHOUT ANY WARRANTY; without even the implied warranty of
### MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
### Library General Public License for more details.
### 
### You should have received a copy of the GNU Library General Public
### License along with this library; if not, write to the Free
### Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA

### erl_opts.py -- holder class for options for the node

class ErlNodeOpts:
    def __init__(self,
                 netTickTime=60,
                 shortNodeNames=1,
                 cookie="",
                 distrVersion=5,
                 distrFlags=4):
        self._netTickTime = netTickTime
        self._shortNodeNames = shortNodeNames
        self._cookie = cookie
        self._distrVersion = distrVersion
        self._distrFlags = distrFlags

    def GetNetTickTime(self):
        return self._netTickTime
    def SetNetTickTime(self, netTickTime):
        self._netTickTime = netTickTime

    def GetShortNodeNames(self):
        return self._shortNodeNames
    def SetShortNodeNames(self, shortNodeNames):
        self._shortNodeNames = shortNodeNames

    def GetCookie(self):
        return self._cookie
    def SetCookie(self, cookie):
        self._cookie = cookie

    def GetDistrVersion(self):
        return self._distrVersion
    def SetDistrVersion(self, distrVersion):
        self._distrVersion = distrVersion

    def GetDistrFlags(self):
        return self._distrFlags
    def SetDistrFlags(self, distrFlags):
        self._distrFlags = distrFlags
