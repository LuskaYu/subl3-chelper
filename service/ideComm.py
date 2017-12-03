#!/usr/bin/python

import  sublime
import  sublime_plugin


def openNewDocAndFill(context):
	pass

def getLineText(view):
	regionStr = ""
	sels = view.sel()
	for a in sels:
		line = view.line(a)
		regionStr += view.substr(line) 
	return regionStr

def getLineRegion(view):
	sels = view.sel()
	for a in sels:
		line = view.line(a)
	return line

def getMoreLinesFromDoc(view, line_cnt):
	sels = view.sel()
	tmpLine = sublime.Region(0,0)
	for a in sels:
		line = view.line(a)	
	
	tmpLine.a = line.a
	tmpLine.b = line.b
	#print("old:%u %u\n"%(line.a, line.b))
	for i in range(line_cnt):
		tmpLine.b = tmpLine.b + 1
		tmpLine = view.line(tmpLine)
		if line.b == tmpLine.b:
			break
		line.a = tmpLine.a
		line.b = tmpLine.b
	#print("new:%u %u\n"%(line.a, line.b))
	#print("%s"%(view.substr(line)))
	return view.substr(line)