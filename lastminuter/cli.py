import asyncio
import argparse
from typing import List

import arrow
import httpx
from simple_term_menu import TerminalMenu

base_url = "https://lastminuter.pl"


async def get_trips(
    session: httpx.AsyncClient,
    source_city="Gdańsk",
    destination_country="Grecja,Hiszpania",
    start="2023-08-01",
    till="2023-08-31",
    stars="5",
    duration="6-8",
    pages=3,
    exclude_destination_country=None,
    board=None,
    **kwargs,
) -> List[dict]:
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
    if board:
        filters_str += f"7:{board}|"

    filters_not_str = ""
    if exclude_destination_country:
        filters_not_str += f"3:{exclude_destination_country}|"

    trips = []
    for page in range(pages):
        filter = {
            'filters_not': filters_not_str,
            'filters_and': filters_str,
            'sorting': 'price',
            'page': page,
            'filters_ext': 0,
            'context': {},
        }
        req = await session.post(
            url=f"{base_url}/offers/",
            headers=headers,
            json=filter,
        )
        data = req.json()['trips']
        trips.extend(data)
    return trips


async def display_trips_table(period: dict):
    line = '\n'
    spacer = line + '-' * 20 + line
    print(f"{spacer} {period['start']} - {period['till']} {spacer}")

    async def run():
        async with httpx.AsyncClient() as client:
            trips = await get_trips(client, **period)
            for trip in trips:
                trip_date = arrow.get(trip['date'].split(' ')[0])
                display_start = trip_date.format('DD.MM (ddd)')
                display_end = trip_date.shift(days=trip['days']).format('DD.MM (ddd)')
                display_date = f"{display_start} - {display_end}"
                display_board = trip['board'] if trip['board'] != 'Własne' else '    '
                if period['max_price'] and trip['pln'] > period['max_price']:
                    break
                row = [
                    trip['pln'],
                    trip['country'],
                    trip['city'],
                    display_date,
                    trip['days'],
                    display_board,
                    trip['stars'],
                    base_url + trip['link'],
                ]
                print('{:>4} | {:<10} | {:^17} | {:<3} | {:<1} | {:<13} | {:<3} | {:<10}'.format(*row))

    await run()


def main():
    parser = argparse.ArgumentParser(
        description="Crawl offers for given conditions"
    )
    parser.add_argument(
        "--select-period",
        default=6,
        type=int,
        help="prompt with X last periods to select, default: 6",
    )
    parser.add_argument(
        "--exclude-country",
        default=None,
        type=str,
        help="exclude specific countries like: Bułgaria,Turcja",
    )
    parser.add_argument(
        "--months",
        default="",
        type=str,
        help="which months to select like: 2023-05,2023-06,2023-07"
    )
    parser.add_argument(
        "--board",
        default=None,
        type=str,
        help="what type of accommodation types to crawl: All Inclusive,Trzy posiłki,Dwa posiłki,Śniadania,Własne"
    )
    parser.add_argument(
        "--stars",
        default="5,4,3,2,1",
        type=str,
        help="what type of stars to crawl: 5,4,3,2,1"
    )
    parser.add_argument(
        "--duration",
        default="-8",
        type=str,
        help="how many days to crawl: 1-8"
    )
    parser.add_argument(
        "--source-city",
        default="Gdańsk",
        type=str,
        help="from which city to crawl: Gdańsk,Warszawa,Kraków,"
    )
    parser.add_argument(
        "--max-price",
        default=None,
        type=int,
        help="max price to crawl, default: 3000",
    )
    parser.add_argument(
        "--pages",
        default=1,
        type=int,
        help="how many pages to crawl, default: 1",
    )
    args = parser.parse_args()

    if args.months:
        selected_periods = [m for m in args.months.split(",") if m]
    else:
        period_options = [
            arrow.now().shift(months=month_shift).format("YYYY-MM")
            for month_shift in range(args.select_period)
        ]
        terminal_menu = TerminalMenu(
            period_options,
            multi_select=True,
            show_multi_select_hint=True,
        )
        selected_indexes = terminal_menu.show()
        selected_periods = [period_options[index] for index in selected_indexes]

    periods = []
    for selected_period in selected_periods:
        start = arrow.get(selected_period).replace(day=1)
        till = start.shift(months=1, days=-1)
        period = dict(
            start=start.format("YYYY-MM-DD"),
            till=till.format("YYYY-MM-DD"),
            destination_country=None,
            duration=args.duration,
            source_city=args.source_city,
            stars=args.stars,
            pages=args.pages,
            max_price=args.max_price,
            board=args.board,
            exclude_destination_country=args.exclude_country,
        )
        periods.append(period)

    async def display_trips():
        for period in periods:
            await display_trips_table(period)

    asyncio.run(display_trips())


if __name__ == '__main__':
    main()
