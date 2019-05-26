from django.shortcuts import render
from .models import Love
from django.http import JsonResponse
# Create your views here.
def likes(request):
    Love.objects.get_or_create(pk=1)
    return render(request, 'apps/clickDBevent.html')

def like_click(request):
    islike = Love.objects.get_or_create(pk=1)
    if islike.like:#like cancle
        like_value = islike.like = 0
        islike.save()
        return JsonResponse({'like_value':like_value})
    else:#like
        like_value = islike.like = 1
        islike.save()
        return JsonResponse({'like_value':like_value})