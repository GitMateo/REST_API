from django.shortcuts import render, redirect
from .models import ShoppingItem
from .forms import ShoppingItemForm

def shopping_list(request):
    items = ShoppingItem.objects.all()
    return render(request, 'shopping/shopping_list.html', {'items': items})

def add_item(request):
    if request.method == 'POST':
        form = ShoppingItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('shopping_list')
    else:
        form = ShoppingItemForm()
    return render(request, 'shopping/add_item.html', {'form': form})

def edit_item(request, item_id):
    item = ShoppingItem.objects.get(id=item_id)
    if request.method == 'POST':
        form = ShoppingItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('shopping_list')
    else:
        form = ShoppingItemForm(instance=item)
    return render(request, 'shopping/edit_item.html', {'form': form, 'item': item})

def delete_item(request, item_id):
    item = ShoppingItem.objects.get(id=item_id)
    item.delete()
    return redirect('shopping_list')

def toggle_bought(request, item_id):
    if request.method == 'POST':
        item = get_object_or_404(ShoppingItem, pk=item_id)
        item.bought = not item.bought
        item.save()
        return JsonResponse({'success': True})
    return JsonResponse({'success': False})