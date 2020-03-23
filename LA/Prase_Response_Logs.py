import re, os, json, bs4, traceback
from bs4 import BeautifulSoup


# get all files for the given folder, including the files in subfolders
def get_all_files(path):
    parents = os.listdir(path)
    for parent in parents:
        child = os.path.join(path, parent)
        if os.path.isdir(child):
            get_all_files(child)
        if os.path.isfile(child):
            file_list.append(child)

    return file_list


# read content of the log file
def read_file(path):
    with open(path, 'rt', encoding='utf-8') as f:
        return f.read()


# save result_dict to file
def save_result(result_dict):
    with open(result_file, 'wt', encoding='utf-8') as f:
        for key in result_dict.keys():
            f.write(result_dict[key] + '\t' + key + '\n')


def parse_api_logs_to_retrieve_all_endpoints(content):
    try:
        # Get request method
        start = content.index('Request method:')
        end = content.index('Request URI')
        log_method = content[start + 16:end].replace('\n', '')

        # Get URI
        start = end
        end = content.index('Proxy:')
        log_uri = content[start + 13:end].replace('\n', '')

        results = log_method + '\t' + log_uri
    except:
        results = 'None' + '\t' + 'None'


# parse jcite keywords log, return id, citation, response value and response code
def parse_jcite_keywords_log(content):
    # get request
    pattern = re.compile(r'<Citation[\s\S]*?</Citation>')
    request = pattern.findall(content)[0]
    soup = BeautifulSoup(request, 'xml')

    id = soup.Citation["id"]
    citation = soup.Citation.string

    response_value = '\t\t'

    start = content.index('HTTP/1.1')
    end = content.index('Content-', start)
    response_code = content[start:end]

    # get response
    if 'HTTP/1.1 200 OK' in content:
        pattern = re.compile(
            r'<JCiteKeywordsOutput[\s\S]*?</JCiteKeywordsOutput>')
        response = pattern.findall(content)[0]
        soup = BeautifulSoup(response, 'xml')

        keyword = soup.Keyword
        normalized = soup.Normalized

        if isinstance(keyword, bs4.Tag) and isinstance(normalized, bs4.Tag):
            b = soup.Keyword.string
            c = soup.Normalized.string
            response_value = b + '\t' + c + '\t'

        result = id + '\t' + citation + '\t' + response_value + response_code
    else:
        result = id + '\t' + citation + '\t' + response_value + response_code

    return result


# parse jcite keywords log, return id, citation, response value and response code
def parse_jcite_keywords_with_pinpoint_log(content):
    # get request
    pattern = re.compile(r'<Citation[\s\S]*?</Citation>')
    request = pattern.findall(content)[0]
    soup = BeautifulSoup(request, 'xml')

    id = soup.Citation["id"]
    citation = soup.Citation.string

    response_value = '||'
    # get response
    # get response code

    start = content.index('HTTP/1.1')
    end = content.index('Content-Type:')
    response_code = content[start:end]

    if 'HTTP/1.1 200 OK' in content:
        pattern = re.compile(
            r'<JCiteKeywordsOutput[\s\S]*?</JCiteKeywordsOutput>')
        response = pattern.findall(content)[0]
        soup = BeautifulSoup(response, 'xml')

        keyword = soup.Keyword
        normalized = soup.Normalized
        pinpoint = soup.Pinpoint

        if isinstance(keyword, bs4.Tag) and isinstance(
                normalized, bs4.Tag) and isinstance(pinpoint, bs4.Tag):
            b = soup.Keyword.string
            c = soup.Normalized.string
            d = soup.Pinpoint.string
            response_value = b + '|' + c + '|' + d + '|'

    result = '|' + id + '|' + citation + '|' + response_value + '|' + response_code
    return result


# parse casebase retrieve paragraph detail log, return LNI, Response Code, and total paragraph
def parse_casebase_retrieve_paragraph_detail_log(content):
    start = content.index('casebase')
    lni = content[start + 9:start + 37]

    start = content.index('HTTP/1.1')
    end = content.index('Date')
    code = content[start:end].strip()

    if ('200' in code):
        #find json response string
        start = content.find('{')
        json_str = content[start:]
        json_obj = json.loads(json_str)
        total_paragraph = json_obj['total_paragraph']
        judge_info_count = len(json_obj['judge_info'])

        if (judge_info_count == 1):
            judge_name1 = json_obj['judge_info'][0]['judge_name']
            start_para1 = json_obj['judge_info'][0]['start_para']
            end_para1 = json_obj['judge_info'][0]['end_para']

            judge_name2, start_para2, end_para2, judge_name3, start_para3, end_para3 = ' ', ' ', ' ', ' ', ' ', ' '
        elif (judge_info_count == 2):
            judge_name1 = json_obj['judge_info'][0]['judge_name']
            start_para1 = json_obj['judge_info'][0]['start_para']
            end_para1 = json_obj['judge_info'][0]['end_para']

            judge_name2 = json_obj['judge_info'][1]['judge_name']
            start_para2 = json_obj['judge_info'][1]['start_para']
            end_para2 = json_obj['judge_info'][1]['end_para']

            judge_name3, start_para3, end_para3 = ' ', ' ', ' '
        elif (judge_info_count == 3):
            judge_name1 = json_obj['judge_info'][0]['judge_name']
            start_para1 = json_obj['judge_info'][0]['start_para']
            end_para1 = json_obj['judge_info'][0]['end_para']

            judge_name2 = json_obj['judge_info'][1]['judge_name']
            start_para2 = json_obj['judge_info'][1]['start_para']
            end_para2 = json_obj['judge_info'][1]['end_para']

            judge_name3 = json_obj['judge_info'][2]['judge_name']
            start_para3 = json_obj['judge_info'][2]['start_para']
            end_para3 = json_obj['judge_info'][2]['end_para']
        else:
            judge_name1, start_para1, end_para1, judge_name2, start_para2, end_para2, judge_name3, start_para3, end_para3 = ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '
    else:
        total_paragraph, judge_info_count, judge_name1, start_para1, end_para1, judge_name2, start_para2, end_para2, judge_name3, start_para3, end_para3 = ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '

    result = lni + '\t' + code + '\t' + total_paragraph + '\t' + str(
        judge_info_count
    ) + '\t' + judge_name1 + '\t' + start_para1 + '\t' + end_para1 + '\t' + judge_name2 + '\t' + start_para2 + '\t' + end_para2 + '\t' + judge_name3 + '\t' + start_para3 + '\t' + end_para3
    return result


# parse casebase retrieve referenced paragraph log, return LNI and Response Code
def parse_casebase_retrieve_referenced_paragraph_log(content):
    start = content.index('casebase')
    lni = content[start + 9:start + 37]

    start = content.index('HTTP/1.1')
    end = content.index('Date')
    code = content[start:end].strip()

    if ('200' in code):
        # find json response string
        start = content.find('{')
        json_str = content[start:]
        json_obj = json.loads(json_str)
        reference_count = len(json_obj['referenced_paragraph_count'])
    else:
        reference_count = ' '

    result = lni + '\t' + code + '\t' + str(reference_count)
    return result


# parse document retrieve json name, json description and div count with paywall
def parse_document_paywall(content):
    start = content.index('HTTP/1.1')
    end = content.index('Content-', start)
    response_code = content[start:end]

    # print("response code:"+response_code)

    if '200' in response_code:
        # get doc lni
        start = content.index('Content-Location')
        end = content.index('Content-Type', start)
        doc_lni = content[start:end].strip()[-28:]
        print('LNI: ' + doc_lni)

        # get response body html
        start = content.index('<html')
        response_body = content[start:]
        soup = BeautifulSoup(response_body, 'xml')

        # get tag : script
        original_script = soup.script.string

        left_count = original_script.count('{')
        right_count = original_script.count('}')

        script = original_script.replace('\n',
                                         '').replace('\t',
                                                     '').replace('},', '')

        try:
            json_obj = json.loads(script)
            name = json_obj['name']
            description = json_obj['description']
        except Exception as e:
            name = 'None'
            description = 'None'

        print('name: ' + name)
        print('description: ' + description)

        # get tag: div with class paywall
        tags = soup.find_all('div', class_='paywall')
        print('div count: ' + str(len(tags)))

        result = doc_lni + '\t' + name + '\t' + description + '\t' + str(
            len(tags)) + '\t' + str(left_count) + '\t' + str(right_count)
        return result


if __name__ == '__main__':
    file_list = []
    result_dict = {}

    # path = r'C:\TFS\infra-shared-services-tests\target\rest-logs\tails'
    # result_file = r'C:\TFS\infra-shared-services-tests\target\rest-logs\detail.txt'

    path = r'C:\Work\SCRUM\86756 -CaseBase Paragraph Citation\cert2\12-6-results\webservice-apac-webservices-retrieve-paragraph-detail'
    result_file = r'C:\Work\SCRUM\86756 -CaseBase Paragraph Citation\cert2\12-6-results\para.txt'

    file_list = get_all_files(path)
    print(file_list)
    for f in file_list:
        fname = f[f.rfind('\\') + 1:]
        content = read_file(f)
        # result_dict[fname] = parse_jcite_keywords_log(content)

        result_dict[fname] = parse_casebase_retrieve_paragraph_detail_log(
            content)
        # result_dict[fname] = parse_casebase_retrieve_referenced_paragraph_log(content)
        # result_dict[fname] = parse_document_paywall(content)

    # print(result_dict)
    save_result(result_dict)
