#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Network import CorpusGraph
from Network import TextGraph
from ResultReference import JiebaChecker
from ResultReference import ThulacChecker
from IO import DisIO

cg = CorpusGraph()
# cg.build_corpus()
#cg.save_as_json('./data/ten.json')
cg.load_from_json('./data/corpus_50k.json')
jieba_checker = JiebaChecker()
thulac_checker = ThulacChecker()

def tokenize(sentence):
    tg = TextGraph()
    tg.build([sentence])
    tg.fill_edge(cg)

    # 暂时只对单句分词
    result = tg.cut()[0]
    jieba_check = jieba_checker.check(sentence, result)
    thulac_check = thulac_checker.check(sentence, result)

    jieba_result = jieba_check["jieba_result"]
    jieba_overlap = jieba_check["overlap"]

    thulac_result = thulac_check["thulac_result"]
    thulac_overlap = thulac_check["overlap"]
    res = {"sentence": sentence, "result": result, "jieba": jieba_result, "jieba_overlap": jieba_overlap,"thulac":thulac_result,"thulac_overlap":thulac_overlap}
    return res

def batching(parag):
    j = 0
    count = 0
    sen_list = []
    para_len = len(parag)
    for i in range(0,para_len):
        if(parag[j] == '。'):
            j += 1
            continue
        if((parag[i] == '。')):
            sen_list.append(tokenize(parag[j:i]))
            count += 1
            j = i + 1
            if count % 10000 == 0:
                print("sen" + str(count))
    if(parag[para_len-1] != '。'):
        sen_list.append(tokenize(parag[j:para_len]))
    print("sen   ok")
    return sen_list

if __name__ == '__main__':
    re = DisIO()
    read_sens = re.sen_from_mongo()
    sen_list = batching(read_sens)
    re.re_to_text(sen_list)