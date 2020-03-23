import requests

class TestV2eAPI(object):
    domain = 'https://www.v2ex.com/'

    def test_node(self):
        path = 'api/nodes/show.json?name=python'
        url = self.domain + path

        jsonRes = requests.get(url).json()   #将返回的json字符串转换成python 字典
        assert jsonRes['id'] ==90
        assert jsonRes['name'] == 'python'
        print(jsonRes)
        print(type(jsonRes))

        textRes = requests.get(url).text
        print(textRes)
        print(type(textRes))