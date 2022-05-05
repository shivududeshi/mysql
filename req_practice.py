import requests

def req_info():
    # r = requests.post('https://httpbin.org/post', data={'key': 'value'})
    r = requests.get('https://api.github.com/events')
    print(dir(r))
    print('r.apparent_encoding: ',r.apparent_encoding)
    print('r.status_code: ',r.status_code)
    # print('r.content',r.content)
    print('r.cookies: ',r.cookies)
    print('r.elapsed: ',r.elapsed)
    print('r.encoding: ',r.encoding)
    print('r.headers: ',r.headers)
    # print('r.json',r.json())
    print('r.ok: ',r.ok)
    print('r.raise for status: ',r.raise_for_status)
    # print('r.text',r.text)
    print('r.url: ',r.url)

req_info()

def stream_content():
    r = requests.get('https://api.github.com/events', stream=True)

    with open('raw_data', 'wb') as fd:
        i=0
        for chunk in r.iter_content(chunk_size=1000):
            print(f'chunk {i} is {chunk}')
            fd.write(chunk)
            i+=1

# stream_content()

def req_timeout():
    try:
        r=requests.get('https://github.com/', timeout=0.05)
        print(r.status_code)
    except Exception as e:
        print('error is :',e)

# req_timeout()


