import os
##import sys
import fileinput
import re
##import subprocess
##src="C:\\Users\\uib25191\\Downloads\\david-marcu-114194-unsplash.jpg"
##dst="D:\\photo"
##cmd='copy "%s" "%s"' % (src, dst)
##subprocess.call(cmd, shell=True)

##import os
##import shutil
###import datetime
##
###now = str(datetime.datetime.now())[:19]
###now = now.replace(":","_")
##
##src_dir="C:\\Users\\uib25191\\Downloads\\david-marcu-114194-unsplash.jpg"
##dst_dir="D:\\photo\\"+"1.jpg"
##shutil.copy(src_dir,dst_dir)

textToSearch = 'Cats'  

textToReplace = 'cats'

fileToSearch  =os.path.realpath(os.getcwd() + "./change.txt")
#os.rename("asdf.cmm","as_df.cmm")
tempFile = open( fileToSearch, 'r+' )

for line in fileinput.input( fileToSearch ):
    matchObj = re.search( r'dogs', line, re.M|re.I)
    if matchObj:
      print ("match --> matchObj.group() : ", matchObj.group())
    else:
      print ("No match!!")
##    if textToSearch in line :
##        print('Match Found')
##    else:
##        print('Match Not Found!!')
##    tempFile.write( line.replace( textToSearch, textToReplace ) )
tempFile.close()
##
##
##input( '\n\n Press Enter to exit...' )


