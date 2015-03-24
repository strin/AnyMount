# dropbox api wrapper.
# use shares

def make_raw_link(link):
  "convert a dropbox file link to a raw link (downloadable)"
  return link+u'&raw=1'

def make_raw_links(links):
  assert(isinstance(links, list))
  return [make_raw_link(link) for link in links]