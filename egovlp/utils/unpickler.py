'''

People build ML code assuming only one model. So they 
give their model some top-level package name like "model".

But what if two people do that??? You're gonna have a mess of 
import conflicts.

So I put everything under a python module with the name of the model e.g. egovlp.
But then when you unpickle the checkpoint, you're going to get 
import errors because it tries to "import model". This lets you
rename those modules.

'''
import sys
from contextlib import contextmanager

@contextmanager
def rename_modules(**modules):
    old_modules = {k: sys.modules.get(k) for k in modules}
    try:
        for k, m in modules.items():
            sys.modules[k] = m
        yield
    finally:
        for k, m in old_modules.items():
            if m is not None:
                sys.modules[k] = m
            else:
                del sys.modules[k]


@contextmanager
def rename():
    from egovlp import model, base, parse_config
    with rename_modules(model=model, base=base, parse_config=parse_config):
        yield