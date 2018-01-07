from flask import Flask
from flask import request
from flask import send_from_directory
from flask import send_file
from Network import CorpusGraph
from Network import TextGraph
from ResultReference import JiebaChecker, ThulacChecker
import os
import json

# 从json文件建立语料库图模型
cg = CorpusGraph()
cg.load_from_json()

# 分词结果校对
jieba_checker = JiebaChecker()
thulac_checker = ThulacChecker()


app = Flask(__name__, template_folder='./presentation', static_folder='./presentation')


@app.route('/')
def hello_world():
    return send_file('./presentation/WordLink.html')


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'presentation'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')


# 加载引用文件（js css 等）
@app.route('/<loadfile>', methods=['POST', 'GET'])
def load_ref(loadfile):
    print(loadfile)
    return send_from_directory(os.path.join(app.root_path, 'presentation'), loadfile)


# 分词的api，web接口只对单句分词（目前）
@app.route('/tokenize-result', methods=['GET', 'POST'])
def tokenize():
    if request.method == 'GET':
        tg = TextGraph()
        sentence = "没有输入"

        # 从参数获取待分词句子
        if request.args.get('sentence', '') != "":
            sentence = request.args.get('sentence', '')
        tg.build([sentence])
        tg.fill_edge(cg)

        # 暂时只对单句分词
        result = tg.cut()[0]
        check_jieba = jieba_checker.check(sentence, result)
        check_thulac = thulac_checker.check(sentence, result);


        # jieba的分词结果
        jieba_result = check_jieba["jieba_result"]
        jieba_overlap = check_jieba["overlap"]

        thulac_result = check_thulac["thulac_result"]
        thulac_overlap = check_thulac["overlap"]
        res = json.dumps(
            {"graph": tg.make_json(cg, path=None), "result": result,
             "jieba": jieba_result, "jieba_overlap": jieba_overlap,
             "thulac": thulac_result, "thulac_overlap": thulac_overlap},
            ensure_ascii=False)
        return res


if __name__ == '__main__':
    app.run(host="localhost", port=8000)
