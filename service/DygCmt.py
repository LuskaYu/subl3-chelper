#!/usr/bin/python
from . import baseLib

def  getBlockCmt(comment):
        blockStart = '''/**\n'''
        blockEnd = '''*/\n'''
        return blockStart + comment + blockEnd

    

def getBlockCmtCxt(user, time, brief):
        blockComCmt = '''
* @brief  %s\n*\n*\n*\n
* @author %s\n\
* @email  %s\n\
* @date   %s\n\
''';
        return blockComCmt%(brief, user._name, user._email, time)
    


def getCopyRights(user, other):
        return "* CopyRights(C) %s %s \n*%s\n"%(user._company, user._copyrights, other)



def getFileHead(user, time, brief, file):
        crs = getCopyRights(user, brief)
        comTxt = getBlockCmtCxt(user, time , file)
        comment = getBlockCmt(crs + comTxt)   

        return comment  
    
def getCHeaderTemp(file):

        hDefine =  baseLib.getFileNamePart(file).upper();
        cHeaderFormat = '''#ifndef __%s_H__\n\
#define __%s_H__\n\
#ifdef __cplusplus\n\
extern \"C\" {\n\
#endif\n\
/*----------------------------------------------*\n\
* file including instruction                   *\n\
*----------------------------------------------*/\n\n\n\
/*----------------------------------------------*\n\
* declare extern variaries                     *\n\
*----------------------------------------------*/\n\n\n\
/*----------------------------------------------*\n\
* declare extern functions                     *\n\
*----------------------------------------------*/\n\n\n\
/*----------------------------------------------*\n\
*declare inner functions                             *\n\
*----------------------------------------------*/\n\n\n\
/*----------------------------------------------*\n\
* global variaries                              *\n\
*----------------------------------------------*/\n\n\n\
/*----------------------------------------------*\n\
* module variaries                              *\n\
*----------------------------------------------*/\n\n\n\
/*----------------------------------------------*\n\
* constants                                      *\n\
*----------------------------------------------*/\n\n\n\n\
/*----------------------------------------------*\n\
* marcro                                       *\n\
*----------------------------------------------*/\n\n\n\
#ifdef __cplusplus\n\
}\n\
#endif\n\
#endif /* __%s_H__ */\n''';           
        return cHeaderFormat%(hDefine, hDefine, hDefine)
 
def getOneParam(ptype, pname):
        funcParamFmt = "* @param  %s %s\n"
        return funcParamFmt%(baseLib.alignStr2Width(ptype, 16, " "), baseLib.alignStr2Width(pname, 16, " "))


def getReturn(preturn):
        returnFmt = "* @return %s \n"
        return returnFmt%(preturn)
