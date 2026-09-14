from organization.models import Establishment


def establishment_processor(request):
    if request.user.is_authenticated:
        return {
            'global_establishment': Establishment.objects.filter(is_active=True).order_by('name')
        }
    return {}

def establishment_theme(request):
    establishment = None
    if request.user.is_authenticated:
        establishment = request.user.establishment
    return {
        'establishment': establishment,
    }