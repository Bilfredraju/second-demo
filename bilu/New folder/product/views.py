from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
from django.template import loader
from .models import data

# Create your views here.

def homepage(req):
    page=loader.get_template('homepage.html')
    data={'cat':'Applainces',
          'pro':[
              {'id':'001',
               'item':'Washing Machine',
               'brand':'LG',
               'spec':['Front Load','6.5 Kg','Silver']
               },
               {'id':'002',
               'item':'Refrigerator',
               'brand':'Samsung',
               'spec':['Double Door','300 L','White']
               } ,  
               {'id':'003',
               'item':'Microwave Oven', 
               'brand':'Whirlpool',
               'spec':['20 L','Convection','Black']
               },
               {
                'id':'004', 
                'item':'Air Conditioner',
                'brand':'Daikin',
                'spec':['1.5 Ton','Inverter','White']
               }
            ]
        }
    response=page.render(data,req)
    return HttpResponse(response)

def dbitems(req):
    page=loader.get_template('dbitems.html')
    db = data.objects.all()
    data1 = {'db': db}
    response=page.render(data1,req)
    return HttpResponse(response)

def productdetail(req,id):
    page = loader.get_template('ProductDetails.html')
    db = data.objects.filter(id=id)
    data2 = {'db': db}
    response=page.render(data2,req)
    return HttpResponse(response)


def view(request):
    page = loader.get_template('Cart.html')
    if request.session.__contains__('cartdata'):
        for key in request.session.keys():
            if key == 'cartdata':
               items = list(request.session[key].items())
               itemdb = []
               for i in items:
                   proid = i[0]
                   quantity = i[1]
                   db = data.objects.get(id=proid)
                   itemdb.append({
                       'id' : proid,
                       'name' : db.name,
                       'quantity' : quantity,
                       'price' : db.price,
                       'description' : db.desc,
                       'feature' : db.fea,
                       'pro_t': int (db.price) * int (quantity)
                   })
            grand_total = 0
            for item in itemdb:
                grand_total += item['pro_t']
            response = page.render({'pros': itemdb, 'grand_total': grand_total}, request)
        return HttpResponse(response)
    else:
        return HttpResponse("No items in cart")

def addcart(request):
    pro_id = request.GET['proid']
    quantity = request.GET['quantity']
    response = HttpResponse("Item Added to Cart")
    cartitems = {}
    if request.session.__contains__('cartdata'):
        cartitems = request.session['cartdata']
    cartitems[pro_id] = quantity
    request.session['cartdata'] = cartitems
    print(cartitems)
    print(request.session.get('cartdata'))
    return response

def clearcart(request):
    if request.session.__contains__('cartdata'):
        del request.session['cartdata']
        return redirect('/product/view/')
    else:
        return HttpResponse("No items in cart to clear")


def search(req):
    page = loader.get_template('search.html')
    datas = {}
    response = page.render(datas,req)
    return HttpResponse(response)
    
def getalldata(req):
    ls = []
    for i in data.objects.all():
        ls.append({
            'id': i.id,
            'name': i.name,
            'price': i.price,
            'fea': i.fea,
            'desc': i.desc
        })
    alldata = {'new':ls}    
    return JsonResponse(alldata)

def getproduct(req,keyw):
    ls = []
    for i in data.objects.filter(name__icontains = keyw):
        ls.append({
            'id': i.id,
            'name': i.name,
            'price': i.price,
            'fea': i.fea,
            'desc': i.desc
        })
    alldata = {'produ':ls}    
    return JsonResponse(alldata)

# def searchitem(request):
#     page = loader.get_template('search.html')
#     query = request.GET.get('q','')
#     results = []
#     if query:
#         results = data.objects.filter(name__icontains=query)
#     response = page.render({'results': results, 'query': query}, request)
#     return HttpResponse(response)

