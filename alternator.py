import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))

CONTENT_SEPARATOR_TOKEN = 'BEGIN'

def clean_newlines(text):
  return '\n'.join(filter(len, text.split('\n')))

def text_to_metadata(text):
  """
  title: Shop
  url: http://shop.wheelflip.com
  """
  metadata = {}

  if not text:
    return metadata

  for line in clean_newlines(text).split('\n'):
    key, value = line.split(':', 1)
    metadata[key.strip()] = value.strip()

  return metadata

class Page(object):
  def __init__(self, slug, path):
    self.slug = slug
    self.extension = path.split('.')[~0]
    self.metadata = None
    self.content = None

    with open(path, 'r') as f:
      self.raw_content = ''.join(f.readlines())

    self.parse_contents()

  def parse_contents(self):
    if CONTENT_SEPARATOR_TOKEN in self.raw_content:
      metadata, content = self.raw_content.split(CONTENT_SEPARATOR_TOKEN)
      self.metadata = text_to_metadata(metadata)
      self.content = content.strip()

    else:
      self.metadata = text_to_metadata(self.raw_content)

def print_tree():
  pages_path = os.path.join(HERE, 'content', 'pages')

  pages = [ Page(p, os.path.join(pages_path, p)) for p in os.listdir(pages_path)]

  for p in pages:
    print p.slug
    print p.content
    print

if __name__ == '__main__':
  print_tree()
