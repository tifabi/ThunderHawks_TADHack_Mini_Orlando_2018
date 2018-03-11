def sendInvite(toNum, callNum, disTopic):
    import requests
    import json

    url = "https://sms.telnyx.com/messages"
    data = {}
    data['to'] = toNum
    data['from'] = '+14077511702'
    data['body'] = 'Hello from Thunderhawk! Call {0} to begin your discussion on {1}'.format(callNum, disTopic)
    payload = json.dumps(data)

    headers = {
        'x-profile-secret': "SECRET",
        'Content-Type': "application/json"
        }

    response = requests.request("POST", url, data=payload, headers=headers)

    return(response.text)


attendees = ['+18328408244','+18326274321','+18324278481','+18327140658']
for i in attendees:
    print sendInvite(i,'+19892560976','Super Smash')
