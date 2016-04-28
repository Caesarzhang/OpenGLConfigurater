#coding=utf-8
import os
import glob

def copySingleFile(src,dst,mode=''):
    with open(src,'r'+mode) as fsrc:
        with open(dst,'w'+mode) as fdst:
            print(dst+' is done.')
            fdst.write(fsrc.read())

def copyFiles(src,dst):
    os.makedirs(dst)
    os.chdir(src)
    hFile=glob.glob('*.h')
    for h in hFile:
        copySingleFile(src+'\\'+h,dst+'\\'+h)
    libFile=glob.glob('*.lib')
    for lib in libFile:
        copySingleFile(src+'\\'+lib,dst+'\\'+lib,'b')
    dllFile=glob.glob('*.dll')
    for dll in dllFile:
        copySingleFile(src+'\\'+dll,dst+'\\'+dll,'b')

def fileEditor(dst,filters):
    content=''
    filters=b'''<ItemGroup>\r\n    <ClInclude Include="Dependencies\\freeglut\\freeglut.h">\r\n      <Filter>\xe5\xa4\xb4\xe6\x96\x87\xe4\xbb\xb6</Filter>\r\n    </ClInclude>\r\n    <ClInclude Include="Dependencies\\freeglut\\freeglut_ext.h">\r\n      <Filter>\xe5\xa4\xb4\xe6\x96\x87\xe4\xbb\xb6</Filter>\r\n    </ClInclude>\r\n    <ClInclude Include="Dependencies\\freeglut\\freeglut_std.h">\r\n      <Filter>\xe5\xa4\xb4\xe6\x96\x87\xe4\xbb\xb6</Filter>\r\n    </ClInclude>\r\n    <ClInclude Include="Dependencies\\freeglut\\glut.h">\r\n      <Filter>\xe5\xa4\xb4\xe6\x96\x87\xe4\xbb\xb6</Filter>\r\n    </ClInclude>\r\n    <ClInclude Include="Dependencies\\glew\\glew.h">\r\n      <Filter>\xe5\xa4\xb4\xe6\x96\x87\xe4\xbb\xb6</Filter>\r\n    </ClInclude>\r\n    <ClInclude Include="Dependencies\\glew\\glxew.h">\r\n      <Filter>\xe5\xa4\xb4\xe6\x96\x87\xe4\xbb\xb6</Filter>\r\n    </ClInclude>\r\n    <ClInclude Include="Dependencies\\glew\\wglew.h">\r\n      <Filter>\xe5\xa4\xb4\xe6\x96\x87\xe4\xbb\xb6</Filter>\r\n    </ClInclude>\r\n  </ItemGroup>\r\n  <ItemGroup>\r\n    <Library Include="Dependencies\\freeglut\\freeglut.lib" />\r\n    <Library Include="Dependencies\\glew\\glew32.lib" />\r\n  </ItemGroup>\r\n</Project>'''
    with open(dst,'rb') as f:
        content=f.read()
        content=content.replace(b'</Project>',filters)
        print(content)
    with open(dst,'wb') as f:
        f.write(content)

src=r"C:\%USERPROFILE%\Coding2016\Dependencies"
dst=input('input the project path')
projectName=dst.split('\\')[-1]

copyFiles(src,dst+'\\'+'\\x64\\Debug')

dst=dst+'\\'+projectName+'\\'

copyFiles(src+'\\freeglut',dst+'Dependencies\\freeglut')
copyFiles(src+'\\glew',dst+'Dependencies\\glew')



filters=b'''<ItemGroup>\r\n    <ClInclude Include="Dependencies\\freeglut\\freeglut.h">\r\n      <Filter>\xe5\xa4\xb4\xe6\x96\x87\xe4\xbb\xb6</Filter>\r\n    </ClInclude>\r\n    <ClInclude Include="Dependencies\\freeglut\\freeglut_ext.h">\r\n      <Filter>\xe5\xa4\xb4\xe6\x96\x87\xe4\xbb\xb6</Filter>\r\n    </ClInclude>\r\n    <ClInclude Include="Dependencies\\freeglut\\freeglut_std.h">\r\n      <Filter>\xe5\xa4\xb4\xe6\x96\x87\xe4\xbb\xb6</Filter>\r\n    </ClInclude>\r\n    <ClInclude Include="Dependencies\\freeglut\\glut.h">\r\n      <Filter>\xe5\xa4\xb4\xe6\x96\x87\xe4\xbb\xb6</Filter>\r\n    </ClInclude>\r\n    <ClInclude Include="Dependencies\\glew\\glew.h">\r\n      <Filter>\xe5\xa4\xb4\xe6\x96\x87\xe4\xbb\xb6</Filter>\r\n    </ClInclude>\r\n    <ClInclude Include="Dependencies\\glew\\glxew.h">\r\n      <Filter>\xe5\xa4\xb4\xe6\x96\x87\xe4\xbb\xb6</Filter>\r\n    </ClInclude>\r\n    <ClInclude Include="Dependencies\\glew\\wglew.h">\r\n      <Filter>\xe5\xa4\xb4\xe6\x96\x87\xe4\xbb\xb6</Filter>\r\n    </ClInclude>\r\n  </ItemGroup>\r\n  <ItemGroup>\r\n    <Library Include="Dependencies\\freeglut\\freeglut.lib" />\r\n    <Library Include="Dependencies\\glew\\glew32.lib" />\r\n  </ItemGroup>\r\n</Project>'''
fileEditor(dst+'\\'+projectName+r'.vcxproj.filters',filters)

filters=b'''<ItemGroup>\r\n    <ClInclude Include="Dependencies\\freeglut\\freeglut.h" />\r\n    <ClInclude Include="Dependencies\\freeglut\\freeglut_ext.h" />\r\n    <ClInclude Include="Dependencies\\freeglut\\freeglut_std.h" />\r\n    <ClInclude Include="Dependencies\\freeglut\\glut.h" />\r\n\r\n  </ItemGroup>\r\n  <ItemGroup>\r\n    <Library Include="Dependencies\\freeglut\\freeglut.lib" />\r\n    <Library Include="Dependencies\\glew\\glew32.lib" />\r\n  </ItemGroup>\r\n</Project>'''
fileEditor(dst+projectName+r'.vcxproj',filters)
