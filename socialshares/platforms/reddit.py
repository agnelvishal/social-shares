def fetch(session, url):
    return session.get('https://www.reddit.com/api/info.json',
        params={'url': url})

def parse(response):
    if response.status_code != 200:
        raise IOError()

    data = response.json()
    ups = 0
    downs = 0
    for child in data['data']['children']:
        ups = ups + child['data']['ups']
        downs = downs + child['data']['downs']
        
    return {
        'ups': ups, 
        'downs': downs, 
        }
