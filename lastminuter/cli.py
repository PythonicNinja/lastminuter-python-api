from typing import List

import requests

base_url = "https://lastminuter.pl"


def get_trips(
        source_city="Gdańsk",
        destination_country="Grecja,Hiszpania",
        start="2023-08-01",
        till="2023-08-31",
        stars="5",
        duration="6-8",
        pages=3,
) -> List[dict]:
    """
    "10:Gdańsk|13:2023-08-01|14:2023-08-31|8:5|6:6-8|3:Grecja,Hiszpania"
    """
    headers = {
        'Content-Type': 'application/json',
    }
    filters_str = ""
    if source_city:
        filters_str += f"10:{source_city}|"
    if start:
        filters_str += f"13:{start}|"
    if till:
        filters_str += f"14:{till}|"
    if stars:
        filters_str += f"8:{stars}|"
    if duration:
        filters_str += f"6:{duration}|"
    if destination_country:
        filters_str += f"3:{destination_country}|"

    trips = []
    for page in range(pages):
        filter = {
            'filters_not': '',
            'filters_and': filters_str,
            'sorting': 'price',
            'page': 0,
            'filters_ext': 0,
            'context': {},
        }
        req = requests.post(
            url=f"{base_url}/offers/",
            headers=headers,
            json=filter,
        )
        data = req.json()['trips']
        trips.extend(data)
    return trips


def main():
    trips = get_trips(
        source_city="Gdańsk",
        destination_country=""
                            "Grecja,"
                            "Egipt,"
                            "Hiszpania,"
                            "Turcja,"
                            "Albania,"
                            "Bułgaria,"
                            "Cypr,"
                            "",
        start="2023-08-01",
        till="2023-08-31",
        stars="5,4,3,2",
        duration="-8",
    )
    for trip in trips:
        print(f"{trip['country']} - {trip['city']} - {trip['pln']} - ({trip['date'].split(' ')[0]} #{trip['days']}days) - {trip['board']} - Hotel {trip['stars']}* - {base_url}{trip['link']}")


if __name__ == '__main__':
    main()
