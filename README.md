# lastminuter-python-api

## Installation

```bash
git clone git@github.com:PythonicNinja/lastminuter-python-api.git
cd lastminuter-python-api
pip install -e .
```

## Usage

```python
| => lastminuter --help
usage: lastminuter [-h] [--select-period SELECT_PERIOD] [--exclude-country EXCLUDE_COUNTRY] [--months MONTHS] [--board BOARD] [--stars STARS] [--duration DURATION]
                   [--source-city SOURCE_CITY] [--max-price MAX_PRICE] [--pages PAGES]

Crawl offers for given conditions

optional arguments:
  -h, --help            show this help message and exit
  --select-period SELECT_PERIOD
                        prompt with X last periods to select, default: 6
  --exclude-country EXCLUDE_COUNTRY
                        exclude specific countries like: Bułgaria,Turcja
  --months MONTHS       which months to select like: 2023-05,2023-06,2023-07
  --board BOARD         what type of accommodation types to crawl: All Inclusive,Trzy posiłki,Dwa posiłki,Śniadania,Własne
  --stars STARS         what type of stars to crawl: 5,4,3,2,1
  --duration DURATION   how many days to crawl: 1-8
  --source-city SOURCE_CITY
                        from which city to crawl: Gdańsk,Warszawa,Kraków,
  --max-price MAX_PRICE
                        max price to crawl, default: 3000
  --pages PAGES         how many pages to crawl, default: 1
```

```bash
| => lastminuter --months 2023-05  --exclude Bułgaria --max-price 3000 --pages 2 --stars 5,4,3 --source-city Gdańsk

--------------------
 2023-05-01 - 2023-05-31
--------------------

1408 | Turcja     |  Riwiera Turecka  | 17.05 (Wed) - 24.05 (Wed) | 7 | All Inclusive | 4   | https://lastminuter.pl/wycieczka/turcja,riwiera-turecka,gdansk,all-inclusive,1560626424/
1409 | Turcja     |  Riwiera Turecka  | 17.05 (Wed) - 24.05 (Wed) | 7 | All Inclusive | 4   | https://lastminuter.pl/wycieczka/turcja,riwiera-turecka,gdansk,all-inclusive,1560626426/
1432 | Turcja     |  Riwiera Turecka  | 17.05 (Wed) - 24.05 (Wed) | 7 | All Inclusive | 3   | https://lastminuter.pl/wycieczka/turcja,riwiera-turecka,gdansk,all-inclusive,1560626438/
1460 | Turcja     |  Riwiera Turecka  | 17.05 (Wed) - 24.05 (Wed) | 7 | All Inclusive | 5   | https://lastminuter.pl/wycieczka/turcja,riwiera-turecka,gdansk,all-inclusive,1560626443/
1548 | Turcja     | Wybrzeże Egejskie | 18.05 (Thu) - 26.05 (Fri) | 8 | All Inclusive | 3   | https://lastminuter.pl/wycieczka/turcja,wybrzeze-egejskie,gdansk,all-inclusive,1558748955/
1549 | Turcja     |      Bodrum       | 18.05 (Thu) - 25.05 (Thu) | 7 | All Inclusive | 3   | https://lastminuter.pl/wycieczka/turcja,bodrum,gdansk,all-inclusive,1560191317/
1557 | Turcja     |  Riwiera Turecka  | 17.05 (Wed) - 24.05 (Wed) | 7 | All Inclusive | 4   | https://lastminuter.pl/wycieczka/turcja,riwiera-turecka,gdansk,all-inclusive,1560626431/
1575 | Turcja     |  Riwiera Turecka  | 17.05 (Wed) - 24.05 (Wed) | 7 | All Inclusive | 5   | https://lastminuter.pl/wycieczka/turcja,riwiera-turecka,gdansk,all-inclusive,1560626445/
1605 | Turcja     |      Alanya       | 16.05 (Tue) - 23.05 (Tue) | 7 | All Inclusive | 4   | https://lastminuter.pl/wycieczka/turcja,alanya,gdansk,all-inclusive,1560566918/
1610 | Cypr       |     Ayia Napa     | 22.05 (Mon) - 29.05 (Mon) | 7 |               | 3   | https://lastminuter.pl/wycieczka/cypr,ayia-napa,gdansk,wlasne,1560633404/
1613 | Turcja     |  Riwiera Turecka  | 17.05 (Wed) - 24.05 (Wed) | 7 | All Inclusive | 5   | https://lastminuter.pl/wycieczka/turcja,riwiera-turecka,gdansk,all-inclusive,1560626406/
1636 | Turcja     |      Alanya       | 16.05 (Tue) - 23.05 (Tue) | 7 | All Inclusive | 4   | https://lastminuter.pl/wycieczka/turcja,alanya,gdansk,all-inclusive,1560483251/
1636 | Turcja     |      Alanya       | 16.05 (Tue) - 23.05 (Tue) | 7 | All Inclusive | 4   | https://lastminuter.pl/wycieczka/turcja,alanya,gdansk,all-inclusive,1560291952/
1655 | Turcja     |  Riwiera Turecka  | 24.05 (Wed) - 31.05 (Wed) | 7 | Dwa posiłki   | 3   | https://lastminuter.pl/wycieczka/turcja,riwiera-turecka,gdansk,dwa-posilki,1560611632/
1661 | Cypr       |     Ayia Napa     | 22.05 (Mon) - 29.05 (Mon) | 7 |               | 3   | https://lastminuter.pl/wycieczka/cypr,ayia-napa,gdansk,wlasne,1560632599/
1666 | Turcja     |  Riwiera Turecka  | 17.05 (Wed) - 24.05 (Wed) | 7 | All Inclusive | 4   | https://lastminuter.pl/wycieczka/turcja,riwiera-turecka,gdansk,all-inclusive,1560626321/
1669 | Turcja     |  Riwiera Turecka  | 17.05 (Wed) - 24.05 (Wed) | 7 | Śniadania     | 4   | https://lastminuter.pl/wycieczka/turcja,riwiera-turecka,gdansk,sniadania,1560626420/
1679 | Cypr       |   Cypr Północny   | 22.05 (Mon) - 29.05 (Mon) | 7 | Śniadania     | 3   | https://lastminuter.pl/wycieczka/cypr,cypr-polnocny,gdansk,sniadania,1560551842/
1713 | Turcja     |  Riwiera Turecka  | 17.05 (Wed) - 24.05 (Wed) | 7 | Dwa posiłki   | 3   | https://lastminuter.pl/wycieczka/turcja,riwiera-turecka,gdansk,dwa-posilki,1560626429/
1714 | Turcja     |      Alanya       | 16.05 (Tue) - 23.05 (Tue) | 7 | All Inclusive | 5   | https://lastminuter.pl/wycieczka/turcja,alanya,gdansk,all-inclusive,1560610183/
1718 | Turcja     |       Kemer       | 16.05 (Tue) - 23.05 (Tue) | 7 | All Inclusive | 3   | https://lastminuter.pl/wycieczka/turcja,kemer,gdansk,all-inclusive,1560632278/
1730 | Turcja     |       Kemer       | 16.05 (Tue) - 23.05 (Tue) | 7 | All Inclusive | 5   | https://lastminuter.pl/wycieczka/turcja,kemer,gdansk,all-inclusive,1560567001/
1746 | Turcja     |       Kemer       | 16.05 (Tue) - 23.05 (Tue) | 7 | All Inclusive | 4   | https://lastminuter.pl/wycieczka/turcja,kemer,gdansk,all-inclusive,1560632405/
1758 | Turcja     |  Riwiera Turecka  | 17.05 (Wed) - 24.05 (Wed) | 7 | All Inclusive | 3   | https://lastminuter.pl/wycieczka/turcja,riwiera-turecka,gdansk,all-inclusive,1560626361/
1768 | Turcja     |      Alanya       | 16.05 (Tue) - 23.05 (Tue) | 7 | All Inclusive | 4   | https://lastminuter.pl/wycieczka/turcja,alanya,gdansk,all-inclusive,1560567683/
1773 | Turcja     |      Alanya       | 16.05 (Tue) - 23.05 (Tue) | 7 | All Inclusive | 4   | https://lastminuter.pl/wycieczka/turcja,alanya,gdansk,all-inclusive,1560566860/
1778 | Turcja     |  Riwiera Turecka  | 17.05 (Wed) - 24.05 (Wed) | 7 | All Inclusive | 3   | https://lastminuter.pl/wycieczka/turcja,riwiera-turecka,gdansk,all-inclusive,1560626354/
1781 | Turcja     | Wybrzeże Egejskie | 18.05 (Thu) - 26.05 (Fri) | 8 | All Inclusive | 3   | https://lastminuter.pl/wycieczka/turcja,wybrzeze-egejskie,gdansk,all-inclusive,1556878294/
1782 | Turcja     |      Bodrum       | 18.05 (Thu) - 25.05 (Thu) | 7 | All Inclusive | 3   | https://lastminuter.pl/wycieczka/turcja,bodrum,gdansk,all-inclusive,1560214958/
1785 | Turcja     |       Kemer       | 16.05 (Tue) - 23.05 (Tue) | 7 | All Inclusive | 4   | https://lastminuter.pl/wycieczka/turcja,kemer,gdansk,all-inclusive,1560633008/

```

## TODO

- add tests
- add badges
