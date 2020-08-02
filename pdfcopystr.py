#! /usr/bin/env python
# coding=utf-8

from nltk.tokenize.punkt import PunktSentenceTokenizer, PunktParameters

oldstr = '''Design pattern detection (DPD) is an active field of research, useful
to support software maintenance and reverse engineering. In particular, it gives useful hints to understand some design decisions, which
are helpful for the comprehension of the system and the following
reengineering steps. Moreover, design pattern detection (DPD) helps
also during the redocumentation phase of a system.
The detection techniques used in the literature span many areas,
like graph theory, constraints satisfaction, fuzzy sets, machine learning and computation of similarity measures, but an optimal solution
has not been found yet. Many causes concur to this situation, e.g., design pattern definitions, programming languages. The definitions of
design patterns, e.g., the ones reported in Gamma et al. (1995), often
focus on the pattern’s intent, and less on its implementation, which is
instead relevant from the reverse engineering point of view, because
it is the input of the detection task. The different possible implementations of a design pattern are known as variants (Niere et al., 2002).
Variants are mainly due to two factors: first, a single abstract solution
can have different implementations, having exactly the same structure and behavior; second, as the definition of the pattern is informal,
two different developers may have slightly different interpretations
of the pattern definition, and they can produce different variants, having a different structure and, in theory, the same external behavior.'''

# 删除换行符
fullstr = oldstr.replace('\n', ' ')
print(fullstr)

# 使用NLTK工具切分句子
punkt_param = PunktParameters()
# 为避免句子在‘i.e.’后面被切分，使用nltk.tokenize.punkt并且自定义缩写词表。
# 可以添加多个缩写词，注意添加的缩写词应该没有最后的“.”，比如i.e.写成i.e，比如al.写成al
abbreviation = ['i.e', 'al']
punkt_param.abbrev_types = set(abbreviation)
tokenizer = PunktSentenceTokenizer(punkt_param)
newstr = tokenizer.tokenize(fullstr)
for temp in newstr:
    print(temp)

print(type(newstr))
