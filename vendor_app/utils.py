from django.db.models import Avg, Count
from django.utils import timezone
from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete
from .models import Vendor, PurchaseOrder
from django.db.models import F

from .models import PurchaseOrder

def update_vendor_metrics(vendor):
    completed_pos = PurchaseOrder.objects.filter(vendor=vendor, status='completed')

    vendor.on_time_delivery_rate = calculate_on_time_delivery_rate(completed_pos)
    vendor.quality_rating_avg = calculate_quality_rating_avg(completed_pos)
    vendor.average_response_time = calculate_average_response_time(completed_pos)
    vendor.fulfillment_rate = calculate_fulfillment_rate(completed_pos)

    vendor.save()

def calculate_on_time_delivery_rate(completed_pos):
    on_time_deliveries = completed_pos.filter(delivery_date__lte=timezone.now())
    return (on_time_deliveries.count() / completed_pos.count()) * 100 if completed_pos.count() > 0 else 0

def calculate_quality_rating_avg(completed_pos):
    return completed_pos.filter(quality_rating__isnull=False).aggregate(Avg('quality_rating'))['quality_rating__avg'] or 0.0

def calculate_average_response_time(completed_pos):
    response_times = completed_pos.filter(acknowledgment_date__isnull=False).annotate(
        response_time=F('acknowledgment_date') - F('issue_date')
    ).aggregate(Avg('response_time'))['response_time__avg']
    return response_times.total_seconds() / 60 if response_times else 0.0

def calculate_fulfillment_rate(completed_pos):
    fulfilled_pos = completed_pos.filter(status='completed', quality_rating__isnull=True)
    return (fulfilled_pos.count() / completed_pos.count()) * 100 if completed_pos.count() > 0 else 0


# Signal to update vendor metrics after each PurchaseOrder save or delete
@receiver(post_save, sender=PurchaseOrder)
@receiver(post_delete, sender=PurchaseOrder)
def update_vendor_metrics_on_po_change(sender, instance, **kwargs):
    update_vendor_metrics(instance.vendor)