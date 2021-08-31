import os

def run(**agrs):
  print "[*] W module dirlister."
  files = os.listdir(".")
  
  return str(files)
