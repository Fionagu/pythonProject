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


def parse_test_count_load(response):
    passCount, totalCount, failCount, passRate = '/', '/', '/', '/'
    try:
        pattern = re.compile(r'<div class="summaryGroup">[\s\S]*?</table>')
        content = pattern.findall(response)
        if len(content) > 0:
            content = content[0]
            print('\nContent to extract count is :\n' + content)

            parser = MyTMLParser()
            parser.links = []
            parser.feed(content)

            i = 0
            print(parser.links)
            for t in parser.links:
                print(str(i)+':'+t)
                i=i+1


            totalCount = parser.links[5]
            failCount = parser.links[13]
            passCount = int(totalCount) - int(failCount)

            passRate = '{0:.2f}%'.format(float(passCount) / float(totalCount) * 100)
    except:
        pass

    print("\nCount extracted is:")
    print("Total:" + str(totalCount))
    print("Pass:" + str(passCount))
    print("Fail:" + str(failCount))
    print("Rate:" + str(passRate))

    return totalCount, passCount, failCount, passRate


def calc_summary():
    aggregate_total = sum(int(i) for i in [smoke_totalCount, reg_totalCount, load_totalCount] if i != '/')
    aggregate_pass = sum(int(i) for i in [smoke_passCount, reg_passCount, load_passCount] if i != '/')
    aggregate_fail = sum(int(i) for i in [smoke_failCount, reg_failCount, load_failCount] if i != '/')

    if aggregate_total == 0:
        aggregate_pass_rate, aggregate_total, aggregate_pass, aggregate_fail = '/'

    try:
        aggregate_pass_rate = '{:.2f}%'.format(100 * float(aggregate_pass) / aggregate_total)
    except:
        aggregate_pass_rate = '/'

    return aggregate_pass_rate, aggregate_total, aggregate_pass, aggregate_fail


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
    loadspec_build = os.getenv('loadspec_build')
    #
    # smoke_build = 'https://opsdev-app-jenkins.route53.lexis.com/job/Dev/job/LA-App_APAC/job/Cert2-Smoke/1/artifact/target/test-report/index.html'
    # regression_build ='https://opsdev-app-jenkins.route53.lexis.com/job/Dev/job/LA-App_APAC/job/Cert2-Reg/1/artifact/target/test-report/index.html'
    # loadspec_build = 'https://opsdev-app-jenkins.route53.lexis.com/job/Dev/job/LA-App_APAC/view/Infra/job/APAC_Loadspec/152/artifact/Loader/build/reports/tests/test/index.html'

    smoke_content=get_report_response(smoke_build)
    smoke_totalCount, smoke_passCount, smoke_failCount, smoke_passRate =parse_test_count(smoke_content)

    reg_content=get_report_response(regression_build)
    reg_totalCount, reg_passCount, reg_failCount, reg_passRate = parse_test_count(reg_content)

    load_content = get_report_response(loadspec_build)
    load_totalCount, load_passCount, load_failCount, load_passRate = parse_test_count_load(load_content)

    aggregate_pass_rate, aggregate_total, aggregate_pass, aggregate_fail = calc_summary()

    text_to_file= []
    text_to_file.append('smoke_pass = '+str(smoke_passCount))
    text_to_file.append('smoke_fail = ' + str(smoke_failCount))
    text_to_file.append('smoke_total = ' + str(smoke_totalCount))
    text_to_file.append('smoke_pass_rate = ' + str(smoke_passRate))
    text_to_file.append('smoke_build_url = ' + smoke_build[:smoke_build.find("cucumber-html-reports")])

    text_to_file.append('regression_pass = ' + str(reg_passCount))
    text_to_file.append('regression_fail = ' + str(reg_failCount))
    text_to_file.append('regression_total = ' + str(reg_totalCount))
    text_to_file.append('regression_pass_rate = ' + str(reg_passRate))
    text_to_file.append('regression_build_url = ' + regression_build[:regression_build.find("cucumber-html-reports")])

    text_to_file.append('loadspec_pass = ' + str(load_passCount))
    text_to_file.append('loadspec_fail = ' + str(load_failCount))
    text_to_file.append('loadspec_total = ' + str(load_totalCount))
    text_to_file.append('loadspec_pass_rate = ' + str(load_passRate))
    text_to_file.append('loadspec_build_url = ' + loadspec_build[:loadspec_build.find('artifact')])

    text_to_file.append('aggregate_pass = ' + str(aggregate_pass))
    text_to_file.append('aggregate_fail = ' + str(aggregate_fail))
    text_to_file.append('aggregate_total = ' + str(aggregate_total))
    text_to_file.append('aggregate_pass_rate = ' + str(aggregate_pass_rate))

    print('\n\nParameters write to file is\n')
    for t in text_to_file:
        print(t)

    write_to_file()