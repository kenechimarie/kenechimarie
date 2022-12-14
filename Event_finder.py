def Berlin_events():
    user = input('Type a event ')
    list_event = {'Bouldering garten':12059, 'Bouldering klub':10999, 'UX_meet_ups':'factory_gorlitzer', 'party':'Suicide_circus'}
    for k in list_event.items():
        if k in user:
            user = user.replace(k)
    return user
Berlin_events()
