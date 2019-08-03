from django.shortcuts import render
from django.http import HttpResponse
from . models import Category,Product
from django.shortcuts import get_object_or_404, render
from django.http import Http404


# def index_view(request):
#     # return HttpResponse("This is index view")
#     return render (request, 'Shop/index.html')

def category(request, category_id):
    return render(request, 'category.html',{})

# def index(request):
#     # return HttpResponse("This in index")
#     return render(request,'category_new.html')
def allProdCat(request, c_slug=None):
    c_page=None
    products=None
    if c_slug!=None:
        c_page=get_object_or_404(Category, slug=c_slug)
        products=Product.objects.filter(category=c_page,available=True)
    else:
        products=Product.objects.all().filter(available=True)
    # cat= Category.objects.get(slug=c_slug)
    # products=Product.objects.filter(category=cat, available=True)
    # return render (request,"category.html",{'category':c_page,'products':products})
    return render (request,"category.html",{'category':c_page,'products':products})

def productsInfo(request,prod_id):

    product = get_object_or_404(Product,pk=prod_id)

    return render(request,"productInfo.html",{'product':product})

def ProdCatDetail(request, c_slug, product_slug):
    try:
        product = Product.objects.get(category__slug=c_slug, slug=product_slug)
    except Exception as e:
        raise e
    return render(request, 'product.html', {'product': product})



