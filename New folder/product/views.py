from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.template import loader
from .models import data


# Create your views here.

def homepage(req):
    page=loader.get_template('homepage.html')
    data={'cat':'Applainces',
          'pro':[
              {'id':'001',
              'item':'washing machine',
              'brand':'LG',
              'spec':['5l','front load','light weight']
              },
              {
                'id':'002',
                'item':'TV',
                'brand':'samsung',
                'spec':['44 inch','double door','tight']
               },
                {
                  'id':'003',
                  'item':'refrigenarator',
                  'brand':'sony',
                  'spec':['5 star','200l'] 
                }
              
                ]}
          

    response=page.render(data,req)
    return HttpResponse(response)

def dbitemdisp(req):
    page=loader.get_template('dbitemdisp.html')
    db=data.objects.all()
    datas={'prods':db}
    response=page.render(datas,req)
    return HttpResponse(response)

def prod(req,key):
    page=loader.get_template('productdetails.html')
    db=data.objects.get(id=key)
    datas={'pro':db}
    response=page.render(datas,req)
    return HttpResponse(response)

# def viewcart(req):
#     page = loader.get_template('shopping.html')
#     datas = req.COOKIES.get('pid')
#     if datas != None:
#       items = datas.split(',')
#       values = {}
#       for i in items:
#           proid,qty = i.split(':')
#           values[proid] = qty
#       response = page.render({'mycart':values},req)
#     else:
#         response = page.render({},req)
#     return HttpResponse(response)

# def addtocart(req):
#     proid = req.GET['proid']
#     qty = req.GET['qty']
#     response = HttpResponse("Item added to cart!")
#     data = req.COOKIES.get('pid')
#     if data !=None:
#         data = data + ',' + proid + ':' + qty
#     else:
#         data = proid+':'+qty
#     response.set_cookie('pid',data)
#     return response




def addtocart(req):
    proid=req.GET['proid']
    qty=req.GET['qty']
    response=HttpResponse("item added to cart")
    cartitems={}
    if req.session.__contains__('cartdata'):
        cartitems=req.session['cartdata']
    cartitems[proid]=qty  
    req.session['cartdata']=cartitems
    print(cartitems)
    return response

def viewcart(req):
    page=loader.get_template('shopping.html')
    if req.session.__contains__('cartdata'):
        for key in req.session.keys():
            if key=='cartdata':
                item=list(req.session[key].items())
                itemdb=[]
                for i in item:
                    proid =i[0]
                    qty=i[1]
                    db=data.objects.get(id=proid)
                    itemdb.append({
                        'id':proid,
                        'Name':db.name,
                        'qty':qty,
                        'Price':db.price,
                        'Fea':db.fea,
                        'Des':db.desc,
                        'pro_t':int(qty)*db.price


                    })
                    cart_sum = sum([i['pro_t']for i in itemdb])
                    # cart_sum=0
                    # for i in itemdb:
                    #     for k,v in i.items():
                    #         if key=='pro_t':
                    #             cart_sum+=values
        response=page.render({'pros':itemdb,'cart_sum':cart_sum},req)                        
                
        return HttpResponse(response)
    else:
        return HttpResponse("no items were added to cart")  

from django.shortcuts import redirect


def clearcart(req):
    if 'cartdata' in req.session:
        del req.session['cartdata']
        return redirect('/product/dbitem/')
    #return HttpResponse("cart cleared")
    else:
        return HttpResponse('no data')

def getalldata(req):
    datas = []
    for i in data.objects.all():
        datas.append({
            'id':i.id,
            'Name':i.name,
            'Price':i.price,
            'Fea':i.fea,
            'Des':i.desc,
        })
    alldata = {'new':datas}
    return JsonResponse(alldata)

def Search(req):
    page=loader.get_template('Search.html')
    datas={}
    response=page.render(datas,req)
    return HttpResponse(response)

def getproduct(req,keyw):
    ls=[]
    for i in data.objects.filter(name__contains=keyw):
        ls.append(
            {
                "id":i.id,
                'name':i.name,
                'price':i.price,
                'fea':i.fea,
                "desc":i.desc
            })
    alldata={'produ':ls}    
    return JsonResponse(alldata)
           