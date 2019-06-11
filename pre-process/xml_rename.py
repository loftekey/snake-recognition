import os
import xml.etree.ElementTree as ET

path = "./annotation"
files =  os.listdir(path)
for fname in sorted(files):
  print(fname)
  try:
    tree = ET.parse (os.path.join(path, fname))
    root = tree.getroot()
    folder = root.find("./folder")
    folder.text = "images"
    filename = root.find("./filename")
    filename.text = fname.replace(".xml", ".jpg")
    name = root.find("./object/name")
    name.text = fname.split("_")[0]
    tree.write(os.path.join(path, fname))
  except Exception as e:
    print(e)