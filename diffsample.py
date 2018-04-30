import difflib
import csvreader
import webbrowser
from pprint import pprint
from distutils import sys
from difflib import context_diff

#sfp='C:\\Users\\nori\\Documents\\program\\vs2015\\PythonApplication7\\dat\\sample1.csv'
#dfp='C:\\Users\\nori\\Documents\\program\\vs2015\\PythonApplication7\\dat\\sample2.csv'

sfp="C:\\Users\\nori\\Documents\\program\\vs2015\\PythonApplication7\\dat\\sampleData\\999\\901\\9999013\\-\\ADT-00\\9999013_-_ADT-00_999999999999999_20111220224447339_-_1"
dfp="C:\\Users\\nori\\Documents\\program\\vs2015\\PythonApplication7\\dat\sampleData\\999\\901\\9999013\\-\\ADT-00\\9999013_-_ADT-00_999999999999999_20111220224447339_-_0"


source=csvreader.openCsv(sfp)
dest=csvreader.openCsv(dfp)

##�����̎擾
#d=difflib.Differ()
#diff=d.compare(source.splitlines(),dest.splitlines())
#pprint(list(diff))

#dd=difflib.HtmlDiff()
#print(dd.make_table(source.splitlines(),dest.splitlines()))



#HTML---------------------------
dd=difflib.HtmlDiff()
diffResult=dd.make_file(source.splitlines(),dest.splitlines(),"aaa","bbb",context=False,charset='iso-2022-jp')

diffResultFilepath='C:\\Users\\nori\\Documents\\program\\vs2015\\diffResult.html'

f=open(diffResultFilepath,'w')
f.write(diffResult)
f.close()

browser=webbrowser.get('"C:\\Program Files\\internet explorer\\iexplore.exe" %s')
browser.open(diffResultFilepath)


#sys.stdout.writelines(context_diff(source,dest))