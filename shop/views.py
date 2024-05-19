from django.shortcuts import render
from django.views import View
from .models import Product, Category,Brands,Color,ClothingType
from django.db.models import Q


# Create your views here.
class ShopView(View):
    def get(self, request):
        products = Product.objects.all()
        search = request.GET.get("search") or ''
        price = request.GET.get("price") or ''
        color = request.GET.get("color") or ''
        typ = request.GET.get("typ") or ''
        brand = request.GET.get("brand") or ''

        products = products.filter(name__icontains = search)

        if price!="":
            if price == "20":
                products = products.filter(Q(price__gte=0) & Q(price__lte=20))
            elif price == "50":
                products = products.filter(Q(price__gte=20) & Q(price__lte=50))
            elif price == "100":
                products = products.filter(Q(price__gte=50) & Q(price__lte=100))
            elif price == "150":
                products = products.filter(Q(price__gte=100) & Q(price__lte=150))
            elif price == "300":
                products = products.filter(Q(price__gte=150) & Q(price__lte=300))
        if color:
            products = products.filter(color__icontains=color)
        if typ:
            products = products.filter(types__icontains=typ)
        if brand:
            products = products.filter(brand__name__icontains=brand)

        categories = Category.objects.all()
        brands = Brands.objects.all()

        context = {
            "products": products,
            "categories": categories,
            "brands": brands,
            "colors": Color.choices,
            "types": ClothingType.choices,
        }
        return render(request, "shop/shop.html",context)


class ShopDetailView(View):
    def get(self,request,id):
        pass


