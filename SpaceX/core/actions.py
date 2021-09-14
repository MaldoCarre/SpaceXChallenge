from json import decoder
import random
import re
from SpaceX.settings import (
    TRELLO_API_TECLA,
    TRELLO_API_TOCKEN,
    todo_list_id,
    spacex_action_id,
    bug_list_id,
    board_id
    )
import requests

def get_members():
    url = f"https://api.trello.com/1/boards/{board_id}/members"
    querystring = {"key": TRELLO_API_TECLA, "token": TRELLO_API_TOCKEN}
    response=requests.request("GET", url, params=querystring)
    members = response.json()
    return members


def create_card(name, list_id, desc):
    url = f"https://api.trello.com/1/cards"
    querystring = {
        "name": name, 
        "idList": list_id, 
        "desc":desc, 
        "key": TRELLO_API_TECLA, 
        "token": TRELLO_API_TOCKEN
        }
    response = requests.request("POST", url, params=querystring)
    card_id = response.json()["id"]

def card_to_do(data:dict)->dict:
    name = data['title']
    desc = data['description']
    create_card(name, todo_list_id, desc)
    resp = {
        'type':data['type'],
        'desc':desc,
        'title':name,
    }
    return resp

def card_bug(data:dict)->dict:
    name = data['title']
    desc = data['description']
    members_list = []
    members=get_members()
    for m in members:
        members_list.append(m['id'])
    random_meber = random.choice(members_list)
    url = f"https://api.trello.com/1/cards"
    querystring = {
        "name": name, 
        "idList": bug_list_id, 
        "desc":desc, 
        "idMembers":random_meber, 
        "key": TRELLO_API_TECLA, 
        "token": TRELLO_API_TOCKEN
        }
    response = requests.request("POST", url, params=querystring)
    resp = {
        'type':data['type'],
        'desc':desc,
        'title':name,
    }
    return resp

def task_card (data:dict)->dict:
    name=data['title']
    desc=data['category']
    url = f"https://api.trello.com/1/cards"
    querystring = {
        "name": name, 
        "idList": spacex_action_id, 
        "desc":desc, 
        "key": TRELLO_API_TECLA, 
        "token": TRELLO_API_TOCKEN
        } 
    response = requests.request("POST", url, params=querystring)
    resp = {
        'type':data['type'],
        'category':desc,
        'title':name,
    }
    return resp

def checktasck(data:dict):
    if data['type'] == 'issue':
        return card_to_do(data)
    elif data['type'] == 'bug':
        return card_bug(data)
    elif data['type'] == 'task':
        return task_card(data)
    else:
        resp = {
            'type':'Error',
            'title':'Invalid element',
            'description':'You are trying to add a invalid element. Just bug, issue and task are able.'
        }
        return resp

