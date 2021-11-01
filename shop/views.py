from django.shortcuts import render
from django.template import loader
from shop.models import Krasofkalar,Category
from shop.forms import CreateKrasofkaForm
from django.views.generic.edit import CreateView
# Create your views here.
def get_product(request):
    categories = Category.objects.all()
    products = Krasofkalar.objects.all()
    products_by_categories = {}
    for c in categories:
        lst = []
        for p in products:
            if c == p.category:
                lst.append(p)
        if len(lst) != 0:
            products_by_categories[c.name] = lst

    context = {
        "categories": categories, 
        "products_by_categories": products_by_categories}
    return render(request, 'brend/index.html', context)

def get_by_category_id(request, category_id):
    categories = Category.objects.all()
    products = Krasofkalar.objects.filter(category=category_id)
    products_by_categories = {}
    for c in categories:
        lst = []
        for p in products:
            if c == p.category:
                lst.append(p)
        if len(lst) != 0:
            products_by_categories[c.name] = lst

    context = {
        "categories": categories, 
        "products_by_categories": products_by_categories}
    return render(request, 'brend/index.html', context)

def import_data(request):
    import csv         
    import os

    settings_dir = os.path.dirname(__file__)
    # print(settings_dir)
    # path = settings_dir + "\maxway.csv"
    info = ''
    categories = {}
    with open(settings_dir + "\maxway_category.csv") as f:
            reader = csv.reader(f)                        
            for row in reader:                
                categories[row[0]]=Category.objects.create(
                    pk = int(row[0]),
                    name = row[1]
                    )
                info = f"{info}\n{row[0]}. {row[1]}"

    info = info + "\n\n\n"
    with open(settings_dir + "\info.csv") as f:
            reader = csv.reader(f)                        
            for row in reader:
                price = int(row[2].replace(" ", ""))
                old_price = int(row[3].replace(" ", ""))
                Krasofkalar.objects.create(
                    name=row[1],
                    old_price=old_price,
                    price=price,
                    image = row[0],
                    category = categories[row[4]]
                    )
                info = f"{info}\n {row[1]}\n"
    return HttpResponse("Success")


class CreateKrasofkaView(CreateView):
    template_name = 'brend/create.html'
    form_class = CreateKrasofkaForm
    success_url = '/'

    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)
        context['category'] = Category.objects.all()
        return context