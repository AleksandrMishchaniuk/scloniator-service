#!/usr/bin/env python3
# coding: utf-8

import sys
import codecs
import pymorphy2
import json
import cgi
import html

print("Content-type: text/html; charset=UTF-8")
print()

sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

form = cgi.FieldStorage()
text = form.getfirst("word")
words_arr = json.loads(text)
words = []
morph = pymorphy2.MorphAnalyzer()

for word in words_arr:
  parse = morph.parse(word)[0]
  parses = parse.lexeme

  for item in parses:
    words.append(item.word)


words_res = json.dumps(words, False, False)

print(words_res)
