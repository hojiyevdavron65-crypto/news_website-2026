from django.shortcuts import render,redirect,get_object_or_404
from .models import Article,Category,Tag,Subscribe
from interactions.models import Comment
from django.contrib import messages
from django.db.models import Q
from django.core.paginator import Paginator



# Create your views here.
def home_page(request):
    latest_new=Article.published.all()[0]
    latest_new_4=Article.published.all()[1:5]
    sport=Article.published.filter(category__name="Sport")[0:4]
    techno=Article.published.filter(category__name="Texnologiya")[0:4]
    iqtisod=Article.published.filter(category__name="Iqtisodiyot")[0:4]
    edu=Article.published.filter(category__name="Ta'lim")[0:4]
    news=Article.published.all()[1:6]
    tag=Tag.objects.all()
    query=request.GET.get('q','')

    if query:
        articles=Article.published.filter(
            Q(title__icontains=query)|Q(body__icontains=query)
        )
        return render(request,"search.html",context={"articles":articles})


    if request.method=="POST":
        email=request.POST.get("email")
        Subscribe.objects.create(
        email=email
        )
        messages.success(request,"Sizning arizangiz muvaffaqiyatli jo'natildi!")
        return redirect('home')

    context={
        "latest_new":latest_new,
        "latest_new_4":latest_new_4,
        "sport":sport,
        "techno":techno,
        "iqtisod":iqtisod,
        "edu":edu,
        "news":news,
        "tag":tag

    }
    return render(request,"index.html",context)

def single_page_view(request,slug):
    article=get_object_or_404(Article.published,slug=slug)
    category=Category.objects.all()
    tag=Tag.objects.all()
    back_url=request.META.get("HTTP_REFERER")
    comments=Comment.objects.filter(article=article,parent__isnull=True)

    # ko'rilgan yangilillar ro'yxatda sessiondan olamiz

    viewed=request.session.get("viewed_articles",[])
    if article.id not in viewed:
        article.views_count+=1
        article.save()
        viewed.append(article.id)
        request.session['viewed_articles']=viewed


    if request.method=="POST":
        if not request.user.is_authenticated:
            messages.warning(request,"Izoh qoldirish uchun avval ro'yxatdan o'ting yoki tizimga kiring!")
            return redirect("signup")

        body=request.POST.get("body")
        parent_id=request.POST.get('parent_id')
        if body:
            Comment.objects.create(
                article=article,
                body=body,
                author=request.user,
                parent_id=parent_id
            )
            return redirect('single',slug=article.slug)


    context={
        "article":article,
        "category":category,
        "tag":tag,
        "back_url":back_url,
        "comments":comments
    }

    return render(request,"single-page.html",context)




def sport_view(request):
    sport = Article.published.filter(category__name="Sport")[0::]
    paginator=Paginator(sport,5)
    page_number=request.GET.get("page")
    page_obj=paginator.get_page(page_number)

    context={
        "page_obj":page_obj
    }

    return render(request,"sport.html",context)

def local_view(request):
    local= Article.published.filter(category__name="Mahalliy")[0::]
    paginator=Paginator(local,5)
    page_number=request.GET.get("page")
    page_obj=paginator.get_page(page_number)

    context={
        "page_obj":page_obj
    }

    return render(request,"local.html",context)

def global_view(request):
    globals= Article.published.filter(category__name="Xorijiy")[0::]
    paginator=Paginator(globals,5)
    page_number=request.GET.get("page")
    page_obj=paginator.get_page(page_number)

    context={
        "page_obj":page_obj
    }

    return render(request,"global.html",context)

def techno_view(request):
    techno= Article.published.filter(category__name="Texnologiya")[0::]
    paginator=Paginator(techno,5)
    page_number=request.GET.get("page")
    page_obj=paginator.get_page(page_number)

    context={
        "page_obj":page_obj
    }

    return render(request,"techno.html",context)

def finance_view(request):
    finance= Article.published.filter(category__name="Iqtisodiyot")[0::]
    paginator=Paginator(finance,5)
    page_number=request.GET.get("page")
    page_obj=paginator.get_page(page_number)

    context={
        "page_obj":page_obj
    }

    return render(request,"finance.html",context)

def society_view(request):
    society= Article.published.filter(category__name="Jamiyat")[0::]
    paginator=Paginator(society,5)
    page_number=request.GET.get("page")
    page_obj=paginator.get_page(page_number)

    context={
        "page_obj":page_obj
    }

    return render(request,"society.html",context)

def edu_view(request):
    edu= Article.published.filter(category__name="Ta'lim")[0::]
    paginator=Paginator(edu,5)
    page_number=request.GET.get("page")
    page_obj=paginator.get_page(page_number)

    context={
        "page_obj":page_obj
    }

    return render(request,"edu.html",context)


