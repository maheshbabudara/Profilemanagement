from django.db import models
from django.core.validators import MinValueValidator

class Vendor(models.Model):
    name = models.CharField(max_length=100)
    contact_details = models.TextField()
    address = models.TextField()
    vendor_code = models.CharField(max_length=20, unique=True)
    on_time_delivery_rate = models.FloatField(default=0,validators=[MinValueValidator(0.0)])
    quality_rating_avg = models.FloatField(default=0,validators=[MinValueValidator(0.0)])
    average_response_time = models.FloatField(default=0,validators=[MinValueValidator(0.0)])
    fulfillment_rate = models.FloatField(default=0,validators=[MinValueValidator(0.0)])

    def __str__(self):
        return self.name

class PurchaseOrder(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    po_number = models.CharField(max_length=50, unique=True)
    order_date = models.DateTimeField()
    delivery_date = models.DateTimeField()
    items = models.JSONField()
    quantity = models.IntegerField(validators=[MinValueValidator(0)])
    status_values={"Inprogress":"Inprogress","completed":"completed","pending":"pending","cancelled":"cancelled"}
    status = models.CharField(max_length=20, choices=status_values)
    quality_rating = models.FloatField(blank=True, null=True, validators=[MinValueValidator(0.0)])
    issue_date = models.DateTimeField()
    acknowledgment_date = models.DateTimeField(blank=True, null=True)

class HistoricalPerformance(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    date = models.DateTimeField()
    on_time_delivery_rate = models.FloatField(validators=[MinValueValidator(0.0)])
    quality_rating_avg = models.FloatField(validators=[MinValueValidator(0.0)])
    average_response_time = models.FloatField(validators=[MinValueValidator(0.0)])
    fulfillment_rate = models.FloatField(validators=[MinValueValidator(0.0)])
