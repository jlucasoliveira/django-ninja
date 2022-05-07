from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from datetime import datetime, timedelta


class Question(models.Model):
    question_text: str = models.CharField(verbose_name=_("question text"), max_length=200)
    pub_date: datetime = models.DateTimeField(verbose_name=_("date published"))

    class Meta:
        verbose_name = _("question")

    def __str__(self) -> str:
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - timedelta(days=1)


class Choice(models.Model):
    question: Question = models.ForeignKey(
        to="polls.Question",
        on_delete=models.deletion.CASCADE,
        verbose_name=_("question"),
    )
    choice_text: str = models.CharField(verbose_name=_("choice text"), max_length=200)
    votes: int = models.IntegerField(verbose_name=_("votes"), default=0)

    class Meta:
        verbose_name = _("choice")

    def __str__(self) -> str:
        return self.choice_text
