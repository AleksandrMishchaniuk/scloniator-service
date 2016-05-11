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
text = html.escape(text)

morph = pymorphy2.MorphAnalyzer()
parse = morph.parse(text)[0]
parses = parse.lexeme

words = []

for item in parses:
	words.append(item.word)

words = json.dumps(words, False, False)

print(words)
