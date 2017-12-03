#!/usr/bin/python
import  re
import  sublime
import  sublime_plugin
from . import DygCmt
from . import ideComm
from . import baseLib
class fmtInputHelper():
      def __init__(self, edit, view, time, user):
        self.file_name = ""
        self.edit = edit
        self.view = view
        self.time = time
        self.user = user
        
      def gethfile(self, file):
          fileHead = DygCmt.getFileHead(self.user, self.time, "", file)
          cHead = DygCmt.getCHeaderTemp(file)
          comment = fileHead + cHead
          nView = self.view.window().new_file()
          sublime.set_clipboard(comment)
          nView.run_command('paste')

      def getcfile(self, file):
          fileHead = DygCmt.getFileHead(self.user, self.time, "", file)
          comment = fileHead
          nView = self.view.window().new_file()
          sublime.set_clipboard(comment)
          nView.run_command('paste')

class formatCollections():
      def block(cmd, edit, view,  time, user):
        help_str = {"dd":"delete", "ad":"add", "md":"modify"}
        flag = 1 
        titleStr = "%s %s by %s"%(time, help_str[cmd._key_str], user._name)

        formatStr = "/* %s  Begin*/\n#if %d \n\n#endif\n/* %s  End*/\n"
        if cmd._key_str == "dd":
          flag   = 0 
        return formatStr%(titleStr, flag, titleStr);

      def fileHead(cmd, edit, view,  time, user):
        return DygCmt.getFileHead(user, time, "", baseLib.getFileNameFromPath(view.file_name()))

      def history(cmd, edit, view,  time, user):
        formatStr = "%s %s description: "
        return formatStr%(time, user._name)

      def headFile(cmd, edit, view,  time, user):
            inputHelper = fmtInputHelper(edit, view, time, user)
          #TODO: use sublimetext api to create a input pannel and get ther input
            view.window().show_input_panel("please input head file name", "", inputHelper.gethfile, None, None)
            return ""

      def sourceFile(cmd, edit, view, time, user):                
            inputHelper = fmtInputHelper(edit, view, time, user)
          #TODO: use sublimetext api to create a input pannel and get ther input
            view.window().show_input_panel("please input source file name", "", inputHelper.getcfile, None, None)
            return ""


      def func(cmd, edit, view, time, user):
        commHead = DygCmt.getBlockCmtCxt(user, time, "")
        returnStr = ""
        textCont = ""
        blockCmtReg = r'\/\*.*?\*\/'
        funcReg = "((?:static|inline|extern)?\s*?(?:const)?\s*(?:unsigned|struct)?\s*?\w+\s*?\*{0,2})\s*([-_\w]+)\s*['(']([^'(']*)[')']\s*\{"
        #2017-02-07, yuch, modify the regx to support void parament
        paramReg = "\s*((?:const)?\s*(?:unsigned|struct)?\s*[-|_|\w]+\s*\*{0,2})\s*([-|_|\w]*)\s*,?"
        paramReg2 = "\s*([-|_\w]+\s*\*{0,2}\s*([-|])"
        resArray = []
        paramStr = ""
        result = []
  
        #get 16 non-empty lines
        textCont = ideComm.getMoreLinesFromDoc(view, 16)
   

        textCont = textCont.replace(blockCmtReg, "")


        #get func implementation string
        result = re.search(funcReg, textCont,  re.M|re.I|re.U)

        if result is None:
          return


        returnStr = DygCmt.getReturn(result.group(1))
        #print(returnStr)
        commHead = DygCmt.getBlockCmtCxt(user, time, result.group(2))
        #print(commHead)
        #print(result.group(3))
        pSearchStr = result.group(3)
        while True:
          resArray=re.search(paramReg, pSearchStr, re.M|re.I|re.U)
        #if cnt > 10:
        #  return ""
        #++cnt
          if resArray is None:
            break 
          #print(resArray.group(1))
          #print(resArray.group(2))         
          paramStr += DygCmt.getOneParam(resArray.group(1), resArray.group(2))
          pSearchStr = pSearchStr[resArray.end():]
        #return ""
        
        return DygCmt.getBlockCmt(commHead + paramStr + returnStr)
