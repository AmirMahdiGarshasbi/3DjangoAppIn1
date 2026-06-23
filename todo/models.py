from django.db import models


# Create your models here.
class Todo(models.Model):
    class Meta:
        verbose_name = 'کار'
        verbose_name_plural = 'کار'

    title = models.CharField('عنوان', max_length=200)
    context = models.TextField('متن')
    created_at = models.DateTimeField(auto_now_add=True)
    OPEN = 1
    DONE = 2
    status_choices = (
        (OPEN, 'انجام نشده'),
        (DONE, 'انجام شد'),
    )
    status = models.IntegerField('وضعیت', choices=status_choices, default = 1)

    def __str__(self):
        new_title = self.title[:30]
        return new_title
    
    def get_status(self):
        if self.status == 1:
            return " | " + "هنوز انجام ندادی😗"
        elif self.status == 2:
            return " | " + "انجام شد😁"