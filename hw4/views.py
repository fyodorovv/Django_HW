from django.shortcuts import render
from .forms import EditProductForm, AddImageProduct
from django.core.files.storage import FileSystemStorage


def edit_product_view(request):
    if request.method == 'POST':
        form = EditProductForm(request.POST)
        message = 'Ошибка в данных'
        if form.is_valid():
            product = form.cleaned_data['product']
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            price = form.cleaned_data['price']
            count = form.cleaned_data['count']

            product.title = title
            product.description = description
            product.price = price
            product.count = count
            product.save()

            message = 'Товар изменен'
    else:
        form = EditProductForm()
        message = 'Заполните форму'
    return render(request, 'edit_product.html', {'form': form, 'message': message})


def add_image_view(request):
    if request.method == 'POST':
        form = AddImageProduct(request.POST, request.FILES)
        message = 'Ошибка в данных'
        if form.is_valid():
            product = form.cleaned_data['product']
            image = form.cleaned_data['image']
            fs = FileSystemStorage()
            image.name = f"{product.title}_{image.name}"
            fs.save(image.name, image)
            product.image_scr = image.name
            product.save()
            message = 'Изображение к товару добавлено'
    else:
        form = AddImageProduct()
        message = 'Заполните форму'
    return render(request, 'add_image.html', {'form': form, 'message': message})
