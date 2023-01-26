from django.urls import path

from measure.views import MeasurementView

urlpatterns = [
    path('', MeasurementView.as_view(), name="measurements_list")
]