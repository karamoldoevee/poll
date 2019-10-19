from django.db import models


class Poll(models.Model):
    question = models.TextField(max_length=50, blank=False, null=False, verbose_name='Вопрос')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')

    def __str__(self):
        return self.question

class Choice(models.Model):
    choice_text = models.TextField(max_length=50, blank=False, null=False, verbose_name='Вариант ответа')
    poll = models.ForeignKey('webapp.Poll', related_name='choices', null=False, on_delete=models.CASCADE, verbose_name='Опрос')

    def __str__(self):
        return self.choice_text

class Answer(models.Model):
    poll = models.ForeignKey('webapp.Poll', related_name='answers', on_delete=models.PROTECT, null=False, verbose_name='Вопрос')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    choice_text = models.ForeignKey('webapp.Choice', related_name='answers', on_delete=models.PROTECT, null=False, verbose_name='Вариант Ответа')


