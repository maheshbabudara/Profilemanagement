from rest_framework import generics
from rest_framework.response import Response
from .models import *
from .serializers import *

class Vendor_Creation(generics.ListCreateAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

class Vendor_Modification(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

class Purchase_Order_Creation(generics.ListCreateAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer

class Purchase_Order_Modification(generics.RetrieveUpdateDestroyAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer

class Vendor_Performance_Metrices(generics.RetrieveAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        data = {
            'on_time_delivery_rate': instance.on_time_delivery_rate,
            'quality_rating_avg': instance.quality_rating_avg,
            'average_response_time': instance.average_response_time,
            'fulfillment_rate': instance.fulfillment_rate
        }
        return Response(data)
        # queryset = HistoricalPerformance.objects.all()
        # serializer_class = Performance
