from django.shortcuts import render,redirect

# Create your views here.
from .forms import CustomeruploadForm
from inventory.models import Customer

def upload_customer(request):                      
    if request.method == 'POST':
        uploaded_product = request.FILES["image"]
        form = CustomeruploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = CustomeruploadForm()
        
    return render(request, "inventory/customer_upload.html", {"form": form})
  
  
def customers_list(request):
    customers = Customer.objects.all()
    return render (request, "inventory/customers_list.html", {"products": customers})
  
  
def  customer_detail(request,id):
  customer = Customer.objects.get(id =id)
  return render(request,"customer/customers_detail.html",{"product":customer})


def edit_customer(request, id):
    customer = Customer.objects.get(id=id)

    if request.method == "POST":
        form = CustomeruploadForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect("product_detail", id=id)
    else:
        form = CustomeruploadForm(instance=customer)

    return render(request, "customer/edit_customer.html", {"form": form})

