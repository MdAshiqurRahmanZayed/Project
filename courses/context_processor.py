from .models import Category

def menu_links(request):
     links = Category.objects.all()
     return dict(links=links) 

def categories(request):
     categories = Category.objects.all()
     return dict(categories=categories) 