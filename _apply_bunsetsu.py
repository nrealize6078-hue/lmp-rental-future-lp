# -*- coding: utf-8 -*-
"""見出し・本文のテキストを文節タグ <w-b> で包む（再実行すると貼り直す）

span を使うと .pain span / .row span:nth-child(2) のような
既存セレクタに巻き込まれて色やサイズが変わってしまうため、
どのCSSにも一致しない専用のカスタム要素を使う。
"""
import re, sys
from bs4 import BeautifulSoup
sys.path.insert(0, '.')
from _bunsetsu import split_bunsetsu

TAG = 'w-b'
TARGET = ('h1,h2,h3,p,summary,strong,b,em,'
          '.step,.word,.lc-h,.tag,.row span,.end-line')
SKIP_PARENT = {'a', 'script', 'style', 'button', 'title'}
SKIP_CLASS = {'eyebrow', 'bar-long', 'bar-short'}
JA = re.compile(r'[぀-ヿ一-鿿]')

def has_skip_ancestor(node):
    for par in node.parents:
        if par.name in SKIP_PARENT:
            return True
        if set(par.get('class') or []) & SKIP_CLASS:
            return True
    return False

def main():
    soup = BeautifulSoup(open('index.html', encoding='utf-8').read(), 'html.parser')
    # 既存の文節タグを剥がしてから貼り直す（旧 span.pb も対象）
    removed = 0
    for old in soup.find_all(TAG) + soup.select('span.pb'):
        old.unwrap(); removed += 1
    soup.smooth()

    wrapped = 0
    for el in soup.select(TARGET):
        for node in list(el.find_all(string=True)):
            text = str(node)
            if not JA.search(text) or not text.strip() or has_skip_ancestor(node):
                continue
            segs = split_bunsetsu(text.strip())
            if len(segs) <= 1:
                continue
            lead = text[:len(text) - len(text.lstrip())]
            tail = text[len(text.rstrip()):]
            frag = lead + ''.join(f'<{TAG}>{s}</{TAG}>' for s in segs) + tail
            node.replace_with(BeautifulSoup(frag, 'html.parser'))
            wrapped += 1
    open('index.html', 'w', encoding='utf-8', newline='\n').write(str(soup))
    print(f'古いタグ{removed}個を剥がし、{wrapped}箇所を文節に分割しました')

main()
