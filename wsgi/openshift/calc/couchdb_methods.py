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

def get_calcData(onlyActive=False):
    chat= get_Doc("calc","utils/list_active")
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
    calc= SERVER['calc']
    if id in calc: #zakladam ze id == username, co ma sens skoro to unikalne wpisy
        user = calc[id]
        user['active'] = True
    else:
        calc[id] = {'active': True, 'host': HOST_NAME, 'operator':chr('+'), 'calculation':"calc/get_data/"} #Trzeba bedzie na OS sprawdzic jak sie rejestruje
    return
