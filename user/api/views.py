from user.models import tips
from . serialisers import TipSerializer
from rest_framework.generics import  (
    UpdateAPIView,
    CreateAPIView,
    DestroyAPIView,
    RetrieveAPIView,
    ListAPIView
    )

class TipsListView(ListAPIView):
    queryset = tips.objects.all()
    serializer_class = TipSerializer  

class TipsDetailView(RetrieveAPIView):
    queryset = tips.objects.all()
    serializer_class = TipSerializer

class TipsCreateView(CreateAPIView):
    queryset = tips.objects.all()
    serializer_class = TipSerializer

class TipsDeleteView(DestroyAPIView):
    queryset = tips.objects.all()
    serializer_class = TipSerializer

class TipsUpdateView(UpdateAPIView):
    queryset = tips.objects.all()
    serializer_class = TipSerializer

    

