from django.db import models
from accounts.models import survote_user


class Voter(models.Model):
    user = models.OneToOneField(survote_user, on_delete=models.CASCADE, null=True, blank=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
    voted = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username


class Position(models.Model):
    name = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    @property
    def get_candidate(self):
        return self.candidate_set.all()

    @property
    def get_polls(self):
        return self.candidate.polls_set.all()

    def __str__(self):
        return self.name 


class Candidate(models.Model):
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    fullname = models.CharField(max_length=150, blank=True, null=True)
    photo = models.ImageField(upload_to='candidate_imgs')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    polls = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.fullname

    @property
    def imageURL(self):
        try:
            url = self.photo.url 
        except:
            url = ''
        return url 


class Vote(models.Model):
    position = models.ForeignKey(Position, on_delete=models.CASCADE, null=True, blank=True)
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE, null=True, blank=True)
    voter = models.ForeignKey(Voter, on_delete=models.CASCADE, null=True, blank=True)