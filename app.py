# coding=utf-8

from flask import Flask, request, render_template, send_file
import json
import mockData

app = Flask(__name__)


@app.route('/')
def hello_world():
    return jsonDump(mockData.a)


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


def jsonDump(data):
    # t = {}
    # t['data'] = a
    # return json.dumps(t, ensure_ascii=False)
    return json.dumps(data, ensure_ascii=False)


if __name__ == '__main__':
    app.run()
