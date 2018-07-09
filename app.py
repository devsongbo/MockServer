# coding=utf-8

from flask import Flask, request, render_template, send_file
import json
import mockData

app = Flask(__name__)


@app.route('/')
def hello_world():
    print  dir(Flask)
    return jsonDump(mockData.b)


# @app.route('/hello/')
# @app.route('/hello/<name>')
#
# def hello(name=None):
#         return render_template('hello.html', name=name)


@app.route('/short/conllect/getConllectCount', methods=['POST', 'GET'])
def register():
    print '****************'
    # print request.headers
    # print request.form
    # print request.values
    # print request.json
    print  request.url
    print jsonDump(mockData.circle_banner_list)

    return jsonDump(mockData.circle_banner_list)


@app.route('/showweb.html', methods=['POST', 'GET'])
def showweb():
    return send_file('helloWorld.html')


@app.route('/circle/topic2/comment/getDateComment', methods=['POST', 'GET'])
def jsonData():

    # 可以读取多种文件类型里的数据   用.json 文件的好处，不用每次修改数据后重新运行
    return send_file('data.json')


def jsonDump(data):
    # t = {}
    # t['data'] = a
    # return json.dumps(t, ensure_ascii=False)
    return json.dumps(data, ensure_ascii=False)


if __name__ == '__main__':

    app.run()
