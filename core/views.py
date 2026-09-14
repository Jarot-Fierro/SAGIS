from core.standard.views import StandardListView
from users.models import User


# Create your views here.
class DashboardView(StandardListView):
    template_name = 'core/dashboard.html'
    model = User
    title = 'Dashboard'
    update_url_name = None
    delete_url_name = None
    module_name = 'dashboard'
    module_color = 'dashboard'

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return self.model.objects.filter(username=self.request.user.username)
        else:
            return None
