import json 
import requests


BASE_URL = "http://127.0.0.1:8000/"

END_POINT = "api/updates/"

def get_list():
    r = requests.get(BASE_URL + END_POINT)
    data = r.json()
    return data 

print(get_list())

def create_update():
    new_data = {
        "user": 1,
        "content": "new more more cool content"
    }
    r = requests.post(BASE_URL + END_POINT, data=json.dumps(new_data))
    if r.status_code == requests.codes.ok:
        return r.json()
    return r.text

def do_obj_update():
    new_data = {
        "content": "id 5 content"
    }
    r = requests.put(BASE_URL + END_POINT + "5/", data=json.dumps(new_data))
    print(r.status_code)
    if r.status_code == requests.codes.ok:
        return r.json()
    return r.text

def do_obj_delete():
    r = requests.delete(BASE_URL + END_POINT + "4/")
    print(r.status_code)
    if r.status_code == requests.codes.ok:
        return r.json()
    return r.text

#print(get_list())
print(do_obj_update())

