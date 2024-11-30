from django import forms
from . import models

class ProductForm(forms.ModelForm):

  class Meta:
    model = models.Product
    fields = ['title', 'category', 'brand', 'description', 'serie_number', 'cost_price', 'selling_price']
    widgets = {
      'title': forms.TextInput({'class': 'form-control'}),
      'category': forms.Select({'class': 'form-control'}),
      'brand': forms.Select({'class': 'form-control'}),
      'description': forms.Textarea({'class': 'form-control'}),
      'serie_number': forms.TextInput({'class': 'form-control'}),
      'cost_price': forms.NumberInput({'class': 'form-control'}),
      'selling_price': forms.NumberInput({'class': 'form-control'}),
    }
    labels = { 
      'title': 'Título',
      'category': 'Categoria',
      'brand': 'Marca',
      'description': 'Descrição',
      'serie_number':'Número de série',
      'cost_price': 'Preço de custo',
      'selling_price': 'Preço de venda',
    }