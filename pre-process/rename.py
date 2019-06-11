import os
import shutil
dirname = os.path.dirname
def main():
  
  for fname in os.listdir("./snake"):
    src = os.path.join("./snake", fname, "Annotation")
    for lname in os.listdir(src):
      lpath = os.path.join(src, lname)
      for xname in os.listdir(lpath):
        xpath = os.path.join(lpath, xname)
        dst = os.path.join("./annotation", "_".join([fname, xname.split("_")[1]]))
        shutil.copy(xpath, dst)


if __name__ == "__main__":
    main()