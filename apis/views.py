from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import SearchKeyForm, WhatsappForm
import requests
from blog.models import Post
from django.http import HttpResponseRedirect


class SearchKeyView(TemplateView):
  
  template_name = 'apis/search_key.html'
  
  def get(self, request):
    post = Post.objects.get(pk=4)
    form = SearchKeyForm()
    return render(request, self.template_name, {'form':form, 'post':post})

  def post(self, request):
    post = Post.objects.get(pk=4)
    form = SearchKeyForm(request.POST)
    if form.is_valid():
      search_key = form.cleaned_data['search_key']

      url = "https://keywords4.p.rapidapi.com/google-topLevel-10-keywords"
      headers = {
      'content-type': "application/json",
      'x-rapidapi-host': "keywords4.p.rapidapi.com",
      'x-rapidapi-key': "C4e4A0veUwpEi3lQDOLNgWYX59sUBN86"     }

      querystring = {"search":search_key,"country":"br"}
      try:
        response = requests.request("GET", url, headers=headers, params=querystring)
        response = response.json()['googleGuggestedKeywords']
        return render(request, self.template_name, {'form':form, 'response':response,'post':post  })

      except Exception:
        return HttpResponseRedirect(self.request.path_info)
    
class WhatsappView(TemplateView):
   
  template_name = 'apis/whatsapp.html'
  
  def get(self, request):
     post = Post.objects.get(pk=2)
     form = WhatsappForm()
     return render(request, self.template_name, {'form':form,'post':post})
     

  def post(self, request):
    post = Post.objects.get(pk=2)
    form = WhatsappForm(request.POST)
    if form.is_valid():
     whatsapp = form.cleaned_data['cell']
     whatsapp = whatsapp.replace('(','').replace('-','').replace(')','')
     whatsapp = whatsapp.replace(" ","")
     whats_url = f'https://api.whatsapp.com/send?phone=+55{whatsapp}'
     whats_link = f'<i class="bx bxl-whatsapp bx-lg" style= "color:#25D366;"</i> https://api.whatsapp.com/send?phone=+55{whatsapp} <script src="https://unpkg.com/boxicons@2.1.1/dist/boxicons.js"></script>'
     return render(request, self.template_name, {'whats_link':whats_link, 'whats_url':whats_url, 'post':post})
  
