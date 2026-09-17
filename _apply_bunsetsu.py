# -*- coding: utf-8 -*-
"""見出し・本文のテキストを文節spanで包む（再実行しても二重にならない）"""
import re, sys
from bs4 import BeautifulSoup, NavigableString
sys.path.insert(0, '.')
from _bunsetsu import split_bunsetsu

TARGET = 'h1,h2,h3,p,summary,.step,.word,.lc-h,.tag,.row span,.row strong,.end-line'
SKIP_PARENT = {'a', 'script', 'style', 'button', 'title'}
SKIP_CLASS = {'eyebrow', 'pb', 'bar-long', 'bar-short'}
JA = re.compile(r'[぀-ヿ一-鿿]')

def has_skip_ancestor(node):
    for par in node.parents:
        if par.name in SKIP_PARENT:
            return True
        cls = set(par.get('class') or [])
        if cls & SKIP_CLASS:
            return True
    return False

def main():
    html = open('index.html', encoding='utf-8').read()
    if 'class="pb"' in html:
        print('すでに適用済み'); return
    soup = BeautifulSoup(html, 'html.parser')
    wrapped = 0
    for el in soup.select(TARGET):
        for node in list(el.find_all(string=True)):
            text = str(node)
            if not JA.search(text) or not text.strip():
                continue
            if has_skip_ancestor(node):
                continue
            segs = split_bunsetsu(text.strip())
            if len(segs) <= 1:
                continue
            lead = text[:len(text) - len(text.lstrip())]
            tail = text[len(text.rstrip()):]
            frag = lead + ''.join(f'<span class="pb">{s}</span>' for s in segs) + tail
            node.replace_with(BeautifulSoup(frag, 'html.parser'))
            wrapped += 1
    open('index.html', 'w', encoding='utf-8', newline='\n').write(str(soup))
    print(f'{wrapped}箇所を文節に分割しました')

main()
