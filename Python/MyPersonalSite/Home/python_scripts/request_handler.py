import json


def _get():
    '''
        Handler for GET requests.
        Typically, GET request is recieved only once when the site is called for the first time.
    '''
#     Noting to do now
#     TODO: have to throw recent 10 posts.
    pass

def _post(req):
    '''
        Handler for POST requests.
        Except the initial call for the home page, rest every thing needs to go through this.
    '''
    if req.get('topic').lower() in ['python','java','shell','c++','misc']:
        return json.dumps({'data':req.get('topic') + ' topic'})
    