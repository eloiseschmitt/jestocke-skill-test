from django.contrib import admin

from api.date_range_list_filter import EndDateRangeListFilter, StartDateRangeListFilter
from booking.models import Booking


@admin.register(Booking)
@admin.display(ordering="-created_on")
class BookingAdmin(admin.ModelAdmin):
    list_display = ('tenant', 'start_date', 'end_date', 'storage_box')
    list_filter = ['storage_box', StartDateRangeListFilter, EndDateRangeListFilter]
