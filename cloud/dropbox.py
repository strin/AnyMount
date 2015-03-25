# dropbox api wrapper.
# use shares
import sys, os
import urllib

def strip_path(path):
  while path[0] == '/' or path[0] == '\\':
    path = path[1:]
  while path[-1] == '/' or path[-1] == '\\':
    path = path[:-1]
  return path

def make_raw_link(link):
  "convert a dropbox file link to a raw link (downloadable)"
  return link+u'&raw=1'

def make_raw_links(links):
  assert(isinstance(links, list))
  return [make_raw_link(link) for link in links]

def download(names, links, path):
  os.system('mkdir -p %s' % path)
  for (name, link) in zip(names, links):
    print 'downloading', name, '->', link
    urllib.urlretrieve(link, path + '/' + name)
