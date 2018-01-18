import requests

def get(url):
    return requests.get(url)

def post(url):
    return requests.post(url)


def url_test(url):
    get_response = get(url)
    post_response = post(url)
    if get_response.status_code == 200 and post_response.status_code == 200:
        return True
    else:
        return False
