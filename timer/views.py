from django.shortcuts import render
from django.http import JsonResponse
from .models import Pomodoro
from django.utils import timezone

def index(request):
    # 取得或建立今天的紀錄
    record, created = Pomodoro.objects.get_or_create(
        user_id='GuestUser', 
        date=timezone.now().date()
    )
    return render(request, 'index.html', {'count': record.count})

def update_count(request):
    if request.method == "POST":
        record, created = Pomodoro.objects.get_or_create(
            user_id='GuestUser', 
            date=timezone.now().date()
        )
        record.count += 1
        record.save()
        return JsonResponse({'status': 'success', 'new_count': record.count})