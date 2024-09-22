def load_teencode():
    replace_list = dict()
    with open('vnpreprocess/dictionary/teencode.txt', encoding='utf-8') as f:
        for pair in f.readlines():
            key, value = pair.split('\t')
            replace_list[key] = value.strip()
    return replace_list
teencode_list = load_teencode()

from .utils import *