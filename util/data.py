import requests
import functools
import sched, time

s = sched.scheduler(time.time, time.sleep)

data = {
    'buy': {},
    'sale': {}
}


def flat_map(acc, c):
    acc['buy'][c['ccy'].lower()] = c['buy']
    acc['sale'][c['ccy'].lower()] = c['sale']
    return acc


def updateData():
    global data
    print('update start', data)
    res = requests.get("https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5").json()
    data = functools.reduce(flat_map, res, dict({'buy': {}, 'sale': {}}))
    print('update finish', data)
    return data


updateData()
s.enter(15 * 60, 1, updateData)
s.run(blocking=False)
