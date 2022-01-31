from django import forms

class SearchKeyForm(forms.Form):
  search_key = forms.CharField(label = 'Insira uma palavra ou frase', max_length = 200, required=False )


class WhatsappForm(forms.Form):
  cell = forms.CharField(label = 'NÚMERO DO CELULAR', max_length = 18, required = True, strip = True, widget=forms.TextInput(attrs={'placeholder': '(00) 000000-0000'}))

