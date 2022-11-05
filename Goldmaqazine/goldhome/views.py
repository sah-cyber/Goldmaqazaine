
from django.shortcuts import render, redirect
from .models import Gold,Category,Carusel,Tag
from  django.core.paginator import Paginator
from .forms import ContactForm
from django.shortcuts import get_object_or_404







def index(requests):
    tag = Tag.objects.all()
    carusel = Carusel.objects.all()
    cats = Category.objects.all()
    context = {
        'cats':cats,
        'carusel': carusel,
        'tag':tag,
    }
    return render(requests, template_name='gold/index.html', context=context)



def jewellery(requests):

    gold = Gold.objects.all()
    paginator = Paginator(gold,6)
    page_number = requests.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'gold': page_obj,
        'page_obj': page_obj,
    }
    return render(requests, 'gold/jewellery.html', context=context)



def partjeweler(requests, get_id):

    golden = Gold.objects.all()
    #gold = Gold.objects.get(pk=get_id)
    gold = get_object_or_404(Gold, pk=get_id)
    context = {
       'golden': golden,
       'gold':  gold,
    }
    return render(requests, 'gold/partjeweler.html',context=context)



def category(requests, category_id):

    category = Gold.objects.all().filter(category_id=category_id)
    eror = get_object_or_404(Gold,pk=category_id)

    context = {
        'category': category,
        'eror':eror

    }
    return render(requests, 'gold/category.html', context=context)



def contact(requests):

    if requests.method == 'POST':
        form = ContactForm(requests.POST)
        if form.is_valid():
            form.save()
            return redirect('contact_email')
    else:
        form = ContactForm()
    context = {
        'form':form,
    }
    return render(requests, 'gold/contact.html',context)



def contact_email(requests):
    form = ContactForm()
    context = {
        'form': form,
    }
    return render(requests, 'gold/contact2.html', context)



def tag (requests):
    tag = Tag.objects.all()
    context = {
        'tag': tag,

    }
    return render(requests,'gold/tag.html', context=context)



def tag_detail(requests, tag_slug):

    gold = Gold.objects.all().filter(tags__slug=tag_slug)
    category = Category.objects.all()
    context = {
        'gold':gold,
        'category':category,
        'eror': get_object_or_404(Tag,slug=tag_slug)
        }
    return render(requests,'gold/tag_detail.html',context=context)



def eror_404(requests,expension):
    return render(requests, 'gold/404.html')