from django.shortcuts import render
from django.views.generic import TemplateView

def home_page_view(request):
    context = {
        "inventory_list": ["Widget 1", "Widget 2", "Widget 3"],
        "greeting": "THAnk you FOR visitING.",
    }
    return render(request, "home.html", context)

class AboutPageView(TemplateView):
    template_name = "about.html"

class ProductsPageView(TemplateView):
    template_name = "products.html"
    extra_context = {
        "products": ["Product 1", "Product 2", "Product 3", "Product 4"],
    }