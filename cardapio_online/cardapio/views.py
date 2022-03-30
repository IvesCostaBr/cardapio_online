from django.shortcuts import render
from django.views.generic import TemplateView




class IndexView(TemplateView):
    template_name = 'cardapio/index.html'
    
    # def get(self, request):
    #     return 

class PetiscosView(TemplateView):
    template_name = 'cardapio/petiscos.html'