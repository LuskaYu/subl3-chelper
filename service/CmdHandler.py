#!/usr/bin/python

import  sublime
import  sublime_plugin
from . import  CommentFormat
from . import ideComm
from . import baseLib
from . import UserInfo

def commHandle(entry, edit, view,  time, user):
    fillStr = entry._format(entry, edit, view, time, user);  
    line = ideComm.getLineRegion(view)
    view.run_command('cut')
    view.insert(edit, line.a, fillStr)
    sublime.set_clipboard('')
    return
    



class baseCmd():
    def __init__(self, key_str, des, handle, fmt_model):
        self._key_str = key_str
        self._cmd_des = des
        self._handle = handle
        self._format = fmt_model     
  

class mainProcess():
    def __init__(self):
        global CMH
        self._cmdHash = {};
        self._cmdHash["hfile"] =  baseCmd("hfile", "add a new head file", commHandle, CommentFormat.formatCollections.headFile)
        self._cmdHash["cfile"] =  baseCmd("cfile", "add a new c file", commHandle, CommentFormat.formatCollections.sourceFile)
        self._cmdHash["hi"] =  baseCmd("hi", "modify list ", commHandle, CommentFormat.formatCollections.history)
        self._cmdHash["ad"] =  baseCmd("ad", "the comment for adding", commHandle, CommentFormat.formatCollections.block)
        self._cmdHash["md"] =  baseCmd("md", "the comment for modifing", commHandle, CommentFormat.formatCollections.block)          
        self._cmdHash["dd"] =  baseCmd("dd", "the comment for deleting", commHandle, CommentFormat.formatCollections.block)
        self._cmdHash["func"] =  baseCmd("func", "add a new function or function comment", commHandle, CommentFormat.formatCollections.func)
        self._cmdHash["head"] =  baseCmd("head", "add a new file head", commHandle, CommentFormat.formatCollections.fileHead)


    def run(self, edit, view):
       # print("file name %s"%(view.file_name()))

        regionStr = ideComm.getLineText(view)  
        time = baseLib.getStdTimeStr()
        user =  UserInfo.user()
        key = regionStr.strip()
        
        if len(key) == 0:
            return

        if key not in self._cmdHash.keys():
            return

        entry = self._cmdHash[key]
        entry._handle(entry, edit,  view,  time, user)
