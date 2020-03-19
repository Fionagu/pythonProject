#! python

import re
import httplib
import os
from urlparse import urlparse
from HTMLParser import HTMLParser


class MyTMLParser(HTMLParser):
    def handle_data(self, data):
        self.links.append(data)


def get_report_response(report_url):
    o = urlparse(report_url)
    netloc = o.netloc
    path = o.path

    conn = httplib.HTTPSConnection(netloc)
    conn.request('GET', path)
    response = conn.getresponse()
    return response.read()


def parse_test_count(response):
    passCount, totalCount, failCount, passRate = '/','/','/','/'
    try:
        pattern = re.compile(r'<table id="tablesorter"[\s\S]*?</table>')
        content = pattern.findall(response)
        if len(content) > 0:
            content = content[0]
            pattern = re.compile(r'<tfoot [\s\S]*?</tfoot>')
            footer = pattern.findall(content)[0]
            print("\nContent to extract count is: \n" + footer)

            parser = MyTMLParser()
            parser.links = []
            parser.feed(footer)

            passCount = parser.links[15]
            failCount = parser.links[17]
            totalCount = parser.links[19]
            passRate = parser.links[39]
    except:
        pass

    print("\nCount extracted is:")
    print("Total:"+ totalCount)
    print("Pass:"+ passCount)
    print("Fail:"+ failCount)
    print("Rate:"+ passRate)

    return totalCount, passCount, failCount, passRate


def parse_test_count_parallel(response):
    passCount, totalCount, failCount, passRate = '/', '/', '/', '/'
    try:
        pattern = re.compile(r'<li class="list-group-item" data-cluecumber-item="scenario-summary">[\s\S]*?</li>')
        content = pattern.findall(response)
        if len(content) > 0:
            content = content[0]
            print('\nContent to extract count is :\n'+content)

            parser = MyTMLParser()
            parser.links = []
            parser.feed(content)

            totalCount = parser.links[0]
            passCount = parser.links[1]
            failCount = parser.links[3]

            totalCount = totalCount[:totalCount.index('Scenario')].strip(' ').replace(',', '')
            passCount = passCount.strip(' ').replace(',', '')
            failCount = failCount.strip(' ').replace(',', '')
            passRate = '{0:.2f}%'.format(float(passCount) / float(totalCount)*100)
    except:
        pass

    print("\nCount extracted is:")
    print("Total:" + totalCount)
    print("Pass:" + passCount)
    print("Fail:" + failCount)
    print("Rate:" + passRate)

    return totalCount, passCount, failCount, passRate


def write_to_file():
    file_name = 'report.txt'
    try:
        with open(file_name, 'wt') as f:
            for t in text_to_file:
                f.writelines(t+'\n')
    except Exception as e:
        print("Error when write into file:", e)


if __name__ == '__main__':
    smoke_build = os.getenv('smoke_build')
    regression_build = os.getenv('regression_build')

    # smoke_build = 'https://opsdev-app-jenkins.route53.lexis.com/job/Dev/job/LA-App_APAC/job/LA-APAC-Infra-Cert2-Smoke/250/cucumber-html-reports/overview-features.html'
    # regression_build ='https://opsdev-app-jenkins.route53.lexis.com/job/Dev/job/LA-App_APAC/job/LA-APAC-Infra-Cert2-Reg/250/cucumber-html-reports/overview-features.html'

    smoke_content=get_report_response(smoke_build)
    smoke_totalCount, smoke_passCount, smoke_failCount, smoke_passRate =parse_test_count_parallel(smoke_content)

    reg_content=get_report_response(regression_build)
    reg_totalCount, reg_passCount, reg_failCount, reg_passRate = parse_test_count_parallel(reg_content)

    text_to_file= []
    text_to_file.append('smoke_pass = '+str(smoke_passCount))
    text_to_file.append('smoke_fail = ' + str(smoke_failCount))
    text_to_file.append('smoke_total = ' + str(smoke_totalCount))
    text_to_file.append('smoke_pass_rate = ' + str(smoke_passRate))
    text_to_file.append('smoke_build_url = ' + smoke_build[:smoke_build.find('artifact') if smoke_build.find("artifact") > smoke_build.find("cucumber-html-reports") else smoke_build.find('cucumber-html-reports')])

    text_to_file.append('regression_pass = ' + str(reg_passCount))
    text_to_file.append('regression_fail = ' + str(reg_failCount))
    text_to_file.append('regression_total = ' + str(reg_totalCount))
    text_to_file.append('regression_pass_rate = ' + str(reg_passRate))
    text_to_file.append('regression_build_url = ' + regression_build[:regression_build.find('artifact') if regression_build.find("artifact") > regression_build.find("cucumber-html-reports") else regression_build.find('cucumber-html-reports')])

    print('\n\nParameters write to file is\n')
    for t in text_to_file:
        print(t)

    write_to_file()