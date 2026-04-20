from djongo import models

class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)
    class Meta:
        db_table = 'teams'
    def __str__(self):
        return self.name

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    team = models.CharField(max_length=100)
    class Meta:
        db_table = 'users'
    def __str__(self):
        return self.name

class Activity(models.Model):
    user = models.CharField(max_length=100)
    activity = models.CharField(max_length=100)
    duration = models.IntegerField()
    class Meta:
        db_table = 'activities'
    def __str__(self):
        return f"{self.user} - {self.activity}"

class Workout(models.Model):
    user = models.CharField(max_length=100)
    workout = models.CharField(max_length=100)
    reps = models.IntegerField()
    class Meta:
        db_table = 'workouts'
    def __str__(self):
        return f"{self.user} - {self.workout}"

class Leaderboard(models.Model):
    user = models.CharField(max_length=100)
    points = models.IntegerField()
    class Meta:
        db_table = 'leaderboard'
    def __str__(self):
        return f"{self.user} - {self.points}"
