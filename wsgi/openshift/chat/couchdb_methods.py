from couchdb import Server
from settings import COUCHDB_HOST, HOST_NAME

#wydajna iteracja, na viewsach - warunek, musi byc view w couchdb juz dodany
def get_Doc(docname, view='_all_docs'):
    #https://www.openshift.com/forums/openshift/permission-denied-on-port-8081
    #SERVER = Server('http://194.29.175.241:5984/')
    SERVER = Server(COUCHDB_HOST)
    if docname in SERVER:
        doc= SERVER[docname].view(view)
        return doc
    return None

def get_chatData(onlyActive=False):
    chat= get_Doc("chat1","utils/list_active")
    docs=[]
    if onlyActive:
        for key in chat:
            if 'value' in key:
                docs.append(key['value'])
    else:
        for key in chat:
            if 'value' in key:
                    if key['value']['active']:
                        docs.append(key['value'])
    return docs

def register_to_couchdb():
    id = HOST_NAME
    SERVER = Server(COUCHDB_HOST)
    chat= SERVER['chat1']
    if id in chat: #zakladam ze id == username, co ma sens skoro to unikalne wpisy
        user = chat[id]
        user['active'] = True
    else:
        chat[id] = {'active': True, 'host': HOST_NAME, 'delivery':"chat/get_message/"} #Trzeba bedzie na OS sprawdzic jak sie rejestruje
    return
