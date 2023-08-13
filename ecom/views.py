from django.shortcuts import get_object_or_404, render
from django.views import generic
from django.core.paginator import Paginator
from .models import ProductListing,buyproduct

from .forms import CommentForm

"""class List(generic.ListView):
    queryset = InstitutesListing.objects.filter(status=1).order_by("-created_on")
   
    template_name = "main/institutelisting.html"
    paginate_by = 10"""

def list_View(request):
    """
    """
    list = ProductListing.objects.filter(status=1,).order_by('-created_on')
    paginator = Paginator(list, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {

        'page_obj': page_obj,

    }
    return render(request, 'main/productlisting.html', context)




"""def product_detail(request, slug):
    template_name = "main/productdetail.html"
    page = get_object_or_404(ProductListing, slug=slug)
        
    return render(
        request,
        template_name,
        {
            "page": page,
        }
                )"""



def product_detail(request, slug):
    template_name = "main/productdetail.html"
    post = get_object_or_404(ProductListing, slug=slug)
    productbuyer = post.productbuyer.filter(active=True).order_by("-created_on")
    new_comment = None
    # Comment posted
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():

            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(
        request,
        template_name,
        {
            "post": post,
            "productbuyer": productbuyer,
            "new_comment": new_comment,
            "comment_form": comment_form,
        },
    )




