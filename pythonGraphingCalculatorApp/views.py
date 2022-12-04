from django.http import JsonResponse
from django.http import HttpResponse
from rest_framework import generics
from .models import User
from .serializers import UserSerializer
import numpy as np, matplotlib.pyplot as plt

# Create your views here.
class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

def generate_bar_graph(request):
    x = np.arange(2, 30, 2)
    y = x ** 2
    largura = 12
    altura = 5
    plt.figure(figsize=(largura, altura))
    título = '1.2B - Plotagem com Barras'
    tamanho_fonte_título = 16
    plt.title(título, fontsize=tamanho_fonte_título)
    plt.bar(x, y)
    plt.savefig(título + '.png')
    plt.show()

    response = { 'url': 'google.com'}

    return JsonResponse(response)
