teencode_list = dict()
with open('vnpreprocess/dictionary/teencode.py', 'r', encoding="UTF-8") as re:
    for line in re:
        src, tgt = line.split('\t')
        teencode_list[src.strip()] = tgt.strip()