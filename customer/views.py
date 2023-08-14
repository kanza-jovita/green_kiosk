from django.shortcuts import render,redirect

# Create your views here.
from .forms import CustomeruploadForm
from customer.models import Customer

def upload_customer(request):                      
    if request.method == 'POST':
        uploaded_customer = request.FILES["image"]
        form = CustomeruploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = CustomeruploadForm()
        
    return render(request, "inventory/customer_upload.html", {"form": form})
  
  
def customer_list(request):
    customers = Customer.objects.all()
    return render (request, "customer/customer_list.html", {"customers": customers})
  
  
def  customer_detail(request,id):
  customer = Customer.objects.get(id =id)
  return render(request,"customer/customer_detail.html",{"customer":customer})


def customer_edit(request, id):
    customer = Customer.objects.get(id=id)

    if request.method == "POST":
        form = CustomeruploadForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect("customer_detail_view", id=id)
    else:
        form = CustomeruploadForm(instance=customer)

    return render(request, "customer/edit_customer.html", {"form": form})

