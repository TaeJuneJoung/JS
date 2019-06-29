from django.shortcuts import render
from .models import Love
from django.http import JsonResponse
# Create your views here.
def likes(request):
    Love.objects.get_or_create(pk=1)
    return render(request, 'apps/clickDBevent.html')

def like_click(request):
    islike = Love.objects.get_or_create(pk=1)
    if islike[0].like:#like cancle
        like_value = islike[0].like = 0
        islike[0].save()
        return JsonResponse({'like_value':like_value})
    else:#like
        like_value = islike[0].like = 1
        islike[0].save()
        return JsonResponse({'like_value':like_value})