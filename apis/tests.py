from django.test import TestCase
from django.contrib.auth import get_user_model
from blog.models import Post
from .forms import SearchKeyForm, WhatsappForm, SeoForm



class SeoCheckup(TestCase):
    
    def test_googleapi_url(self):
        post = Post()
        data = {"seo_url": "www.ecocircuito.com.br", "post":post}

        response = self.client.post('/apis/seocheckup', data=data, follow = True)
        status_code = response.status_code
        redirect_path = response.request.get('/apis/seocheckup/')
        self.assertEqual(status_code, 200)
        self.assertEqual(redirect_path, '/apis/seocheckup/')



class UserTest(TestCase):

    def setUp(self):
        user_a = User(name='fmrafael', email= 'fmrafael@gmail.com')
        user_a.is_staff = True
        user_a.is_superuser = True
        user_a.set_password('123')
        user_a.save()
        print(user_a.id)

    def test_user_exists(self):
        user_count = User.objects.all().count()
        self.assertEqual(user_count, 1)
        print(user_count)

        

