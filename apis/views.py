from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import SearchKeyForm, WhatsappForm, SeoForm
import requests
from blog.models import Post
from django.http import HttpResponseRedirect
import os 
from googleapiclient.discovery import build

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

class SeoView(TemplateView):
  
  template_name = 'apis/seocheckup.html'
  
  def get(self, request):
    post = Post.objects.get(pk=61)
    form = SeoForm()
    return render(request, self.template_name, {'form':form, 'post':post})

  def post(self, request):
    post = Post.objects.get(pk=61)
    form = SeoForm(request.POST)
    if form.is_valid():
      seo_url = form.cleaned_data['seo_url']
      seo_url = f"https://{seo_url}"
      ##em dev, tirar #
      #os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r"C:\Users\rafae\instabot\digitimes-1643719520339-4d1f6d8086d1.json"
      os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/home/fmrafael/projeto10/keys.json"
      service = build('pagespeedonline', 'v5')
      
      category=['ACCESSIBILITY', 'BEST_PRACTICES', 'PERFORMANCE', 'PWA', 'SEO']
      
      try:
        collection = service.pagespeedapi()
        response = collection.runpagespeed(url=seo_url, category=category).execute()
        data = response["lighthouseResult"]["categories"]
        datax = {}
        scores_desc=['Performance', 'Acessibilidade', 'Melhores práticas', 'SEO', 'PWA']
        for key,value in  data.items():
          datax1 = {key:round(value["score"]*100)}
          datax.update(datax1)
        
        
        return render(request, self.template_name, { 'form':form,'datax':datax,'post':post, 'scores_desc':scores_desc  })
        

      except Exception:
        return HttpResponseRedirect(self.request.path_info)
  
class TrendzzzView(TemplateView):
  template_name = 'apis/trendzzz.html'
  def get(self, request):
    post = Post.objects.get(pk=61)
    return render(request, self.template_name, {'post':post})

  