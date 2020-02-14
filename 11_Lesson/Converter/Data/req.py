def get_data_from_uri(resp):

    """
    Method for obtaining data on exchange rates from the NBRB website
    """

    currents = resp.json()
    result = []
    for key in currents:
        result.append({'Abbreviation': key['Cur_Abbreviation'], 'Name': key['Cur_Name'],
                       'How many units': key['Cur_Scale'], 'BYN': key['Cur_OfficialRate']})
    return result
