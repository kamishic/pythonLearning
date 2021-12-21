import os

for currentDir,childDirs,fileNames in os.walk('./data'):
  print("currentDir",currentDir)
  print("childDirs",childDirs)
  print("fileNames:",fileNames)
  for fileName in fileNames:
    print("os.path.join:",os.path.join('a','b',fileName))
