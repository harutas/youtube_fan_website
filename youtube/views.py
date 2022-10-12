import random
from django.shortcuts import render, get_object_or_404, get_list_or_404

# Create your views here.
from django.views.generic import TemplateView

from .models import Youtube, Notable, Link

# home
class IndexView(TemplateView):

    template_name = 'index.html'

    def get(self, request):
        youtubes = Youtube.objects.all()
        random_pk = random.randint(1, len(youtubes))
        youtube = Youtube.objects.get(pk=random_pk)
        context = {
        "youtube": youtube
        }
        return render(request, "index.html", context)

index = IndexView.as_view()

# genre
class GenreView(TemplateView):
    
    template_name = 'genre.html'
    
    def get(self, request, pk):
        youtube = get_object_or_404(Youtube, pk=pk)
        context = {
        "youtube": youtube
        }
        return render(request, "genre.html", context)
    
genre = GenreView.as_view()

# notables
class NotablesView(TemplateView):
    
    template_name = 'notables.html'
    
    def get(self, request, pk):
        youtube = get_object_or_404(Youtube, pk=pk)
        notables = get_list_or_404(Notable, youtube=youtube)
        context = {
            "youtube": youtube,
            "notables" : notables
        }
        return render(request, "notables.html", context)

notables = NotablesView.as_view()
    
# notables detail
class NotablesDetailView(TemplateView):
    
    template_name = 'detail.html'
    
    def get(self, request, pk, notableIndex):
        youtube = get_object_or_404(Youtube, pk=pk)
        notables = get_list_or_404(Notable, youtube=youtube)
        notable = notables[notableIndex]
        context = {
            "youtube": youtube,
            "notable" : notable
        }
        return render(request, "detail.html", context)
    
    
notablesDetail = NotablesDetailView.as_view()

# link
class LinkView(TemplateView):
    
    template_name = 'link.html'
    
    def get(self, request, pk):
        youtube = get_object_or_404(Youtube, pk=pk)
        links = get_list_or_404(Link, youtube=youtube)
        context = {
            "youtube": youtube,
            "links" : links
        }
        return render(request, "link.html", context)

link = LinkView.as_view()

