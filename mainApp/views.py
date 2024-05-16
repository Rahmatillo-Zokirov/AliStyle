from django.shortcuts import render, get_object_or_404
from .models import *
from django.views import View

class HomeView(View):
    def get(self, request):
        bolimlar = Bolim.objects.all()[:7]
        context = {
            'bolimlar': bolimlar

            }
        return render(request, 'page-index.html', context)

class BolimlarView(View):
    pass


class BolimView(View):
    def get(self, request, pk):
        bolim = get_object_or_404(Bolim, id=pk)
        ichki_bolimlar = IchkiBolim.objects.filter(bolim=bolim)
        context = {
            'bolim': bolim,
            'ichki_bolimlar': ichki_bolimlar
        }
        return render(request, 'page-category.html', context)


# class IchkiBolimMahsulotlarView(View):
#     def get(self, request, pk):
#         ichki_bolim = get_object_or_404(IchkiBolim, id=pk)
#         mashsulotlar = Mahsulot.objects.filter(ichki_bolim=ichki_bolim)
#         context = {
#             'mashsulotlar': mashsulotlar,
#             'ichki_bolim': ichki_bolim
#         }
#         return render(request, 'page-listing-grid.html', context)

