import csv
import asyncio


async def waiter():
    await asyncio.sleep(3)


info_from_csv = {}

with open('binlist-data.csv', encoding='utf-8') as f:
    reader = csv.reader(f, delimiter=',', quotechar='"')
    for row in reader:
        info_from_csv[row[0]] = [row[1], row[2], row[3], row[4],
                                 row[5], row[6], row[7], row[8],
                                 row[9], row[10], row[11]]


def get_data_from_csv(data):
    try:
        return True, {'results': info_from_csv[data], 'bin': data}
    except KeyError:
        return False, {'results': None}
