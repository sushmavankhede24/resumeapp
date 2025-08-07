from django.db import models


# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    email = models.EmailField()
    profile_pic = models.ImageField(upload_to="profile_pics/", blank=True, null=True)

    def __str__(self):
        return self.name


class Skill(models.Model):
    profile = models.ForeignKey(Profile, related_name="skills", on_delete=models.CASCADE)
    skill_name = models.CharField(max_length=50)
    proficiency = models.IntegerField(default=0)  # 0-100 scale

    def __str__(self):
        return f"{self.skill_name} ({self.proficiency}%)"


class Project(models.Model):
    profile = models.ForeignKey(Profile, related_name="projects", on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to="project_images/", blank=True, null=True)
    url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title
