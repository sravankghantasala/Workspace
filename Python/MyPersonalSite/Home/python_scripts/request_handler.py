from json import dumps,loads


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
    if req.get('transaction').lower() == 'topic':
        return dumps({'data': req.get('topic') + ' topic'})
    elif req.get('transaction').lower() == 'submitpost':
#         TODO: Have to add the data to sql database.
        return dumps({'data': 'got the data .. will process!'})
        