from django.shortcuts import redirect, render
from .forms import ProductuploadForm
from inventory.models import Product

def upload_product(request):                      
    if request.method == 'POST':
        uploaded_product = request.FILES["image"]
        form = ProductuploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = ProductuploadForm()
        
    return render(request, "inventory/product_upload.html", {"form": form})
  
  
def products_list(request):
    products = Product.objects.all()
    return render (request, "inventory/products_list.html", {"products": products})
  
  
def  product_detail(request,id):
  product = Product.objects.get(id=id)
  return render(request,"inventory/products_detail.html",{"product":product})


def edit_product(request, id):
    product = Product.objects.get(id=id)

    if request.method == "POST":
        form = ProductuploadForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect("product_detail_view", id=id)
    else:
        form = ProductuploadForm(instance=product)

    return render(request, "inventory/edit_product.html", {"form": form})


def search_results(request):
    query = request.GET.get('q')
    if query:
        results = Product.objects.filter(name__icontains=query)
    else:
        results = []
    return render(request, 'search_results.html', {'results': results, 'query': query})