import os,requests,sys

def get_file(url):
    try:
        r = requests.get(url=url) 
        if (r.status_code == 200):
            return r.content
        else:
            raise Exception('Get json file failed for status code :'+ str(r.status_code))
    except Exception as e:
        raise Exception(e)


def save(destination,text):
    try:
        path = os.path.dirname(destination)
        if not os.path.exists(path):
            os.makedirs(path)

        with open(destination,'wb') as f:
            f.write(text)
    except Exception as e:
        print('save error: '+ e)


if __name__=='__main__':
    print(len(sys.argv))
    source = sys.argv[1]
    destination = sys.argv[2]
 
    print('download file from: '+source)
    content = get_file(source)

    print('save file to: ' + os.path.abspath(destination))
    save(destination, content)
