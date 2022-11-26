from django.forms import model_to_dict
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Product


# Create your views here.
@api_view(['GET'])
def api_view(request):
    query = Product.objects.all().order_by("?").first()
    data = {}
    if query:
        data = model_to_dict(query)

    return Response(data)