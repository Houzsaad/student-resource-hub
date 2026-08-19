from django.db import models
from django.utils.text import slugify


class Faculty(models.Model):
    name = models.CharField(max_length=150, unique=True)
    slug = models.SlugField(max_length=160, unique=True, blank=True)

    class Meta:
        ordering = ["name"]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Department(models.Model):
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE, related_name="departments")
    name = models.CharField(max_length=150)
    slug = models.SlugField(max_length=160, blank=True)

    class Meta:
        ordering = ["name"]
        unique_together = ("faculty", "name")

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} ({self.faculty.name})"


class Course(models.Model):
    SEMESTER_CHOICES = [("first", "First"), ("second", "Second")]

    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name="courses")
    code = models.CharField(max_length=20)          # e.g. "CIT 201"
    title = models.CharField(max_length=200)
    level = models.PositiveSmallIntegerField()        # e.g. 100, 200, 300
    semester = models.CharField(max_length=10, choices=SEMESTER_CHOICES)

    class Meta:
        ordering = ["level", "code"]
        unique_together = ("department", "code")

    def __str__(self):
        return f"{self.code} — {self.title}"

# Create your models here.
