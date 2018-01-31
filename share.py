import BaseHTTPServer
from SimpleHTTPServer import SimpleHTTPRequestHandler
import os
import Tkinter
import tkFileDialog
import shutil











srchtml = os.getcwd()+'/share.html'
print("Select file to send!")
# Tkinter.Tk().withdraw() # Close the root window
# file_path = tkFileDialog.askopenfilename()

file_path='/home/revanth/Desktop/index.html'


dir_path=os.path.dirname(file_path)

dsthtml=dir_path+'/index.html'

shutil.copy(srchtml, dsthtml)



os.chdir(dir_path)
addr = ("0.0.0.0", 8000)
serv = BaseHTTPServer.HTTPServer(addr, SimpleHTTPRequestHandler)
print("Sharing the folder!")
print("open 192.168.31.238:8000")
print("press Ctrl+c to stop")
serv.serve_forever()



 














# import os
# import shutil

# srcfile = 'a/long/long/path/to/file.py'
# dstroot = '/home/myhome/new_folder'


# assert not os.path.isabs(srcfile)
# dstdir =  os.path.join(dstroot, os.path.dirname(srcfile))

# os.makedirs(dstdir) # create all directories, raise an error if it already exists
# shutil.copy(srcfile, dstdir)




# path = "/home"

# # Check current working directory.
# retval = os.getcwd()
# print "Current working directory %s" % retval

# # Now change the directory
# os.chdir( path )

# # Check current working directory.
# retval = os.getcwd()

# print "Directory changed successfully %s" % retval