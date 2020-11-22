from rest_framework import routers, serializers, viewsets
from user.models import tips  


class TipSerializer(serializers.ModelSerializer):
    class Meta:
        model = tips
        fields = ('Title','Details','UserProfession')

