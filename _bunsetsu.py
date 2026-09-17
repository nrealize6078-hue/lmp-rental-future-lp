# -*- coding: utf-8 -*-
"""日本語を文節っぽい単位に切る（形態素解析なし・切らない側に倒す）"""
import re

KANJI = r'一-鿿々'
KATA  = r'ァ-ヶー'
# 助詞の直前に来てよい文字。ひらがなが続く途中では切らない（「ひとつ」の「と」対策）
PREV  = rf'[{KANJI}{KATA}0-9A-Za-z）」』】]'
JOSHI = r'(?:からは|までは|には|へは|とは|では|から|まで|より|など|ほど|だけ|こそ|しか|[がをにへとはもでやかの])'
# 助詞の直後がこれらで始まるときは動詞・補助用言が続くとみなして切らない
NOCUT = ('される','されて','され','した','して','しま','する','すれ','しれ',
         'なる','なっ','なり','なろ','ない','なく','いう','いく','いる','いた',
         'おり','おい','よる','より','あり','ある','きる','つい','対し','関し','向け','言',
         'す','し','せ','そう','き','く','け')  # 「大丈夫で|すか？」のような助動詞の切断を防ぐ
CLOSERS = '」』）】"\''
PUNCT = '、。！？'

def split_bunsetsu(text):
    # 1) 句読点の後で切る（続く閉じ括弧は前に含める）
    parts, buf, i = [], '', 0
    while i < len(text):
        ch = text[i]; buf += ch; i += 1
        if ch in PUNCT:
            while i < len(text) and text[i] in CLOSERS:
                buf += text[i]; i += 1
            parts.append(buf); buf = ''
    if buf:
        parts.append(buf)
    # 2) 助詞の後で切る
    out = []
    for p in parts:
        segs, last = [], 0
        for m in re.finditer(rf'(?<={PREV}){JOSHI}', p):
            end = m.end()
            if end >= len(p) or p[end] in PUNCT or p[end] in CLOSERS:
                continue
            if p[end:].startswith(NOCUT):
                continue
            segs.append(p[last:end]); last = end
        segs.append(p[last:])
        out += [s for s in segs if s]
    # 3) 1文字の断片は前にくっつける
    merged = []
    for s in out:
        if merged and len(s.strip()) <= 1:
            merged[-1] += s
        else:
            merged.append(s)
    return merged
