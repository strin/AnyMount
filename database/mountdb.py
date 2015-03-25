# mount relationship database.
import json
import shelve

class Mount:
  def __init__(self, path, names, links, selected = False):
    "create a mount relationship object"
    self.path = path
    self.names = names
    self.links = links
    self.selected = selected

  def __str__(self):
    res = ['path:', str(self.path), \
           'names:', str(self.names), \
           'links:', str(self.links), \
           'selected:', str(self.selected)]
    return '\n'.join(res)

class ShelveDB:
  "simple implementation of mount relational database"
  def __init__(self, path):
    self.mounts = []
    self.path = path

  def mount(self, mount_obj):
    self.mounts += [mount_obj]

  def unmount(self, id):
    self.mounts.remove(self.mounts[id])

  def load(self):
    database = shelve.open(self.path)
    if not database.has_key('mounts'):
      self.mounts = []
      return 
    self.mounts = database['mounts']
    database.close()

  def save(self):
    database = shelve.open(self.path)
    database['mounts'] = self.mounts
    database.close()

  def __str__(self):
    res = [str(mount) for mount in self.mounts]
    return '\n\n'.join(res)

if __name__ == "__main__":
  # db = ShelveDB('database.db')
  # db.mount(Mount("/model", ["abc", "cba"], ["http://a/", "http://b/"], selected=True))
  # db.mount(Mount("/data", ["ofu", "ufo"], ["http://q/", "http://p/"], selected=True))
  # db.save()
  db2 = ShelveDB('database.db')
  db2.load()
  print db2






