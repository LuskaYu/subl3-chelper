#!/usr/bin/python
import  sys
import  sublime
import  sublime_plugin
import  time
from .service import CmdHandler


class ChelperCommand(sublime_plugin.TextCommand):
	def run(self, edit):

          #get selection descritor 
          chelper =  CmdHandler.mainProcess()
          #view.insert(edit, 0, "hello")
          return chelper.run(edit, self.view)


