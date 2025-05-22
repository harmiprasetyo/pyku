from tastypie.resources import ModelResource
from tastypie.constants import ALL
from .models import Dashboard


class DashboardResource(ModelResource):

    class Meta:
        model = "Dashboard"

        queryset = Dashboard.objects.all()

        resource_name = 'dashboard'

        filtering = {'username': ALL}
