from rest_framework.views import APIView
from customer.models import Customer   
from .serializers import CustomerSerializer ,CartSerializer
from rest_framework.response import Response
from rest_framework import status
from cart.models import Cart
from inventory.models import Product
# Create your views here.
class CustomerListView(APIView):
    def get(self,request):
        customers = Customer.objects.all()
        serializer = CustomerSerializer(customers, many = True) 
        # data of all customers but in json format
        return Response(serializer.data) 
    # Return is in json format

    def post(self,request):
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class CustomerDetailView(APIView):
    def get(self,request,id,format = None):
        customer = Customer.objects.get(id=id)
        serializer = CustomerSerializer(customer)
        return Response(serializer.data)
    def put(self,request,id,format = None):
        customer = Customer.objects.get(id=id)
        serializer = CustomerSerializer(customer,request.data)   
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,id,format = None):
        customer = Customer.objects.get(id = id)
        customer.delete()
        return Response("customer deleted",status=status.HTTP_204_NO_CONTENT) 
    
class AddToCartView(APIView):
        def post(self,request,format=None):
            cart_id = request.data["cart_id"]
            product_id = request.data["product_id"]
            cart = Cart.objects.get(id=cart_id)
            product = Product.objects.get(id=product_id)
            updated_cart = cart.add_product(product)
            serializer = CartSerializer(updated_cart)
            return Response(serializer.data)