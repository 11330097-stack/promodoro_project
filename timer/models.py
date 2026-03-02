from django.db import models

class Pomodoro(models.Model):
    user_id = models.CharField(max_length=50)   # 使用者 ID
    count = models.IntegerField(default=0)      # 完成次數
    date = models.DateField(auto_now_add=True)  # 自動紀錄當天日期

    def __str__(self):
        return f"{self.user_id} - {self.date}"