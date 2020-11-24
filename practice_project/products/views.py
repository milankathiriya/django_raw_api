from .forms import ProductForm
from .models import Product
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render


def index(request):
    """
    List of all products
    """
    qs = Product.objects.all()
    products = []
    for i in qs:
        products.append({'id': i.id, 'name': i.name,
                         'price': i.price, 'created_at': i.created_at})
    return JsonResponse(data={'data': products}, safe=False)


def addProduct(request):
    """
    Add a new product
    """
    if request.method == 'POST':
        form = ProductForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            return redirect(index)
    else:
        form = ProductForm()
    return render(request, 'add_product.html', {'form': form})


def fetchProduct(request, id):
    """
    Fetch a single product
    """
    qs = get_object_or_404(Product, pk=id)
    product = {'id': qs.id, 'name': qs.name,
               'price': qs.price, 'created_at': qs.created_at}
    return JsonResponse(data={'data': product}, safe=False)
