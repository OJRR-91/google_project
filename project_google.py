# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 14:58:28 2020

@author: oscarjex
"""
class Event():
    def __init__(self,event_date,event_type,machine_name,user):
        self.date=event_date
        self.type=event_type
        self.machine=machine_name
        self.user=user

def get_event_date(event):
    return event.date
def current_users(events):
    events.sort(key=get_event_date)
    machines={}
    for i in events:
        if i.machine not in machines:
            machines[i.machine]=set()
        if i.type=="login":
            machines[i.machine].add(i.user)
        elif i.type=="logon":
            machines[i.machine].remove(i.user)
    return machines
def generate_report(machines):
    for machine,user in machines.items():
        if len(user)>0:
            user_list=", ".join(user)
            print("{} :{}".format(machine,user_list))
            