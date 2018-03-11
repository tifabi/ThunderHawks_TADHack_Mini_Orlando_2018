def connectConf(toNum):
    from zang import ZangException, Configuration, ConnectorFactory
    from zang.domain.enums.http_method import HttpMethod
    sid ='ACf674eb3243bc6af758c7413085619724'
    authToken ='64c45edae0144a46ad419ad94820295b'
    url ='http://api.zang.io/v2'

    configuration = Configuration(sid, authToken, url=url)
    callsConnector = ConnectorFactory(configuration).callsConnector

    try:
        call = callsConnector.makeCall(
            to=toNum,
            from_='19892560976',
            url='http://cloud.zang.io/data/inboundxml/a191249bb4c4928c95c96d73ae3fa0172cce62de',
            method=HttpMethod.GET,
            sipAuthUsername='ACf674eb3204fd5668655b4b5ca30868fb',
            sipAuthPassword='72d75225757b45778c1cc7693ed9540c')
        print(call.sid)
    except ZangException as ze:
        print(ze)

attendees = ['+18328408244','+18326274321','+18324278481','+18327140658']
for i in attendees:
    connectConf(i)
