from .models import *
def user_context(request):
    user = None
    if request.user.is_authenticated:
        try:
            user = Tarqatuvchi.objects.get(username=request.user.username)
        except Tarqatuvchi.DoesNotExist:
            pass
    context = {
        'user': user,
    }
    return context
