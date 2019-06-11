import os

dirname = os.path.dirname

par_dir_path = dirname(dirname(os.path.abspath(__file__ )))
print(par_dir_path)
data_path = os.path.join(par_dir_path, "Data")

class LoadImage(object):
  def __init__(self, dirname):
    super(LoadImage, self).__init__()
    self.dirname = dirname

  def __iter__(self):
    for dname in sorted(os.listdir(self.dirname)):
      for fname in sorted(os.listdir(os.path.join(self.dirname, dname))):
        yield os.path.join(self.dirname, dname, fname)

test = LoadImage(data_path)
for item in test:
  print(item)