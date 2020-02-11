class ErrorConnect(Exception):
    def __init__(self, text):
        self.text = text


def uri_link(resp):
    currents = resp.json()
    result = []
    for key in currents:
        result.append({'Abbreviation': key['Cur_Abbreviation'], 'Name': key['Cur_Name'],
                       'How many units': key['Cur_Scale'], 'BYN': key['Cur_OfficialRate']})
    return result
