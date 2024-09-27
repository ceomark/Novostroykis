from django.views.generic import ListView
from .models import Property

class PropertyListView(ListView):
    model = Property
    template_name = 'properties/property_list.html'
