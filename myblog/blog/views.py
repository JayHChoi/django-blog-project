from django.shortcuts import render
from django.views import generic
# Create your views here.


class AboutView(generic.TemplateView):
    template_name = "blog/about.html"


class ContactView(generic.TemplateView):
    template_name = "blog/contact.html"


class PortfolioView(generic.TemplateView):
    template_name = "blog/portfolio.html"
