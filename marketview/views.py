from django.shortcuts import render
from pymongo import MongoClient
from bson.json_util import dumps
from django.http import HttpResponse

def takeFirst(elem):
    return elem[0]

def takeDate(elem):
    return elem['date']

def takeY(elem):
    return elem['y']

# Create your views here.
def getDailyData(request, InsCode):
    db = MongoClient()
    bourse = db.bourse
    symbols = bourse.symbols
    symbol = symbols.find_one({"InsCode": InsCode})
    ddata = symbol['DailyData']
    volume_real = []
    volume_legal = []
    count_real = []
    count_legal = []
    for day in ddata:
        daydata = []
        daydata.append(1000* (day['date'].timestamp()))
        daydata.append(day['vol_buy_real'] + day['vol_sell_real'])
        volume_real.append(daydata)
        daydata = []
        daydata.append(1000* (day['date'].timestamp()))
        daydata.append(day['vol_buy_legal'] + day['vol_sell_legal'])
        volume_legal.append(daydata)
        daydata = []
        daydata.append(1000* (day['date'].timestamp()))
        daydata.append(day['count_buy_real'] + day['count_sell_real'])
        count_real.append(daydata)
        daydata = []
        daydata.append(1000* (day['date'].timestamp()))
        daydata.append(day['count_buy_legal'] + day['count_sell_legal'])
        count_legal.append(daydata)
        
    volume_real.sort(key=takeFirst)
    volume_legal.sort(key=takeFirst)
    count_real.sort(key=takeFirst)
    count_legal.sort(key=takeFirst)
    data = {'real': {'volume': volume_real, 'count': count_real}, 'legal': {'volume': volume_legal, 'count': count_legal}}
    json = dumps(data)
    return HttpResponse(json, content_type='application/json')

def getShareHolders(request, InsCode):
    db = MongoClient()
    bourse = db.bourse
    symbols = bourse.symbols
    symbol = symbols.find_one({"InsCode": InsCode})
    shareholders = symbol['Shareholders']
    data = []
    if len(shareholders) > 10:
        support_data = []
        for shareholder in shareholders:
            entry = {}
            entry['name'] = shareholder['Name']
            shares = shareholder['Shares']
            shares.sort(key=takeDate, reverse=True)
            today = shares[0]
            entry['y'] = today['stock']
            support_data.append(entry)
        support_data.sort(key=takeY, reverse=True)
        for supdata in support_data:
            if len(data) < 9:
                data.append(supdata)
            else:
                if len(data) == 10:
                    data[9]['y'] += supdata['y']
                else:
                    entry = {}
                    entry['name'] = u'بقیه'
                    entry['y'] = supdata['y']
                    data.append(entry)
    else:
        for shareholder in shareholders:
            entry = {}
            entry['name'] = shareholder['Name']
            shares = shareholder['Shares']
            shares.sort(key=takeDate, reverse=True)
            today = shares[0]
            entry['y'] = today['stock']
            data.append(entry)
    data.sort(key=takeY, reverse=True)
    data[0]['sliced'] = True
    data[0]['selected'] = True
    json = dumps(data)
    return HttpResponse(json, content_type='application/json')

def getOHLC(request, InsCode):
    db = MongoClient()
    bourse = db.bourse
    symbols = bourse.symbols
    symbol = symbols.find_one({"InsCode": InsCode})
    ddata = symbol['OHLC']
    ohlc = []
    for day in ddata:
        daydata = []
        daydata.append(1000* (day['date'].timestamp()))
        daydata.append(day['o'])
        daydata.append(day['h'])
        daydata.append(day['l'])
        daydata.append(day['c'])
        ohlc.append(daydata)
        
    ohlc.sort(key=takeFirst)
    json = dumps(ohlc)
    return HttpResponse(json, content_type='application/json')

def getSearchSymbols(request):
    db = MongoClient()
    bourse = db.bourse
    symbols = bourse.symbols
    results = symbols.find({'$or':[{'LVal18AFC': {'$regex': request.GET.get('s','')}},{'Title': {'$regex': request.GET.get('s','')}}]})
    searchdata = []
    for result in results:
        data = {}
        data['Name'] = result['LVal18AFC']
        data['Title'] = result['Title']
        data['ID'] = result['InsCode']
        searchdata.append(data)
    json = dumps(searchdata)
    return HttpResponse(json, content_type='application/json')

def getLastAnalysis(request, Count):
    db = MongoClient()
    bourse = db.bourse
    analysis = bourse.analysis
    count = Count if Count <= 4 and Count > 0 else 4
    results = analysis.find().sort([('_id', 1)]).limit(count)
    lastones = []
    for result in results:
        data = {}
        data['ID_Symbol'] = result['ID_Symbol']
        data['Title'] = result['Title']
        data['Thumbnail'] = result['Thumbnail']
        data['Summery'] = result['Summery']
        lastones.append(data)
    json = dumps(lastones)
    return HttpResponse(json, content_type='application/json')

def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def panel(request):
    return render(request, 'test.html')
