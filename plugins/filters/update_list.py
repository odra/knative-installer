import json

from ansible.module_utils._text import to_bytes, to_text

try:
  from __main__ import display
except ImportError:
  from ansible.utils.display import Display
  display = Display()


def update_list(a, *args, **kw):
  data = {k:kw[k] for k in kw.keys() if k != 'index'}
  for k in data:
    a[kw['index']][k] = data[k]
  return a


class FilterModule(object):
  def filters(self):
    return {
      'update_list': update_list
    }
