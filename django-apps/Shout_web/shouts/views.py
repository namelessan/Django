from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from django.utils import timezone
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView, ListView
from django.urls import reverse_lazy

from .models import Shout
from .forms import AddShout

# Create your views here.
# def index(request):
#     form = AddShout()
#     contents = {
#         "form": form
#     }
#     return render(request, 'shouts/index.html', contents)
class IndexView(CreateView):
    form_class = AddShout
    success_url = reverse_lazy('shouts:detail')
    template_name = 'shouts/index.html'


class DetailView(ListView):
    model = Shout
    template_name = 'shouts/detail.html'
    context_object_name = 'shout_list'

    def get_queryset(self):
        return Shout.objects.order_by('-shout_time')[:10]

# def detail(request):
#     if request.method == 'POST':
#         shout_text = request.POST['shout_text']
#         shout_time = timezone.datetime.now()
#         Shout.objects.create(shout_text=shout_text, shout_time=shout_time)
#     latest_shout_list = Shout.objects.order_by('-shout_time')[:10]
#     context = { 'latest_shout_list': latest_shout_list}
#     """Return the last ten published question."""
#     return render(request, 'shouts/detail.html', context)
