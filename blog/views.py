from django.views.generic import DetailView, ListView
from django.shortcuts import render
from .models import Post, TableAffiliate


class PostListView(ListView):
  queryset = Post.objects.filter(status=1).order_by('-created')
  model = Post
#  template_name = "blog/post_list.html"

class PostDetailView(DetailView):
  model = Post


def home_view(request, *args, **kwargs):
  return render(request, "home.html",{})
# Create your views here.


def policy_view(request, *args, **kwargs):
  return render(request, "policy.html", {})


def affiliate_view(request, *args, **kwargs):
  get_affiliate = TableAffiliate.objects.all()
  post = Post.objects.get(pk=6)
  return render(request, "blog/affiliate.html", {"get_affiliate": get_affiliate, "post":post,} )