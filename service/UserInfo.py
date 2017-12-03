#!/usr/bin/python
import sublime

class user():
    def __init__(self):
    		curSetting = sublime.load_settings("CHelper.sublime-settings")
    		tmpInfo =curSetting.get("chelper_user", ["default","default","default","All rights resverd"])
    		self._name=tmpInfo[0]
    		self._company=tmpInfo[1]
    		self._email=tmpInfo[2]
    		self._copyrights=tmpInfo[3]



    