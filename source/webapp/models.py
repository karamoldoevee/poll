from django.db import models

class Poll(models.Model):
    question = models.TextField(max_length=50, blank=False, null=False, verbose_name='Вопрос')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')

    def __str__(self):
        return self.question

class Choice(models.Model):
    choice_text = models.TextField(max_length=50, blank=False, null=False, verbose_name='Вариант ответа')
    poll = models.ForeignKey('webapp.Poll', related_name='choices', on_delete=models.CASCADE, verbose_name='Опрос')
