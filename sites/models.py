from django.db import models

# Create your models here.


def site_name_str(instance, filename):
    return 'media/sites/{0}/{1}'.format(instance.site_name, filename)


class Site(models.Model):
    site_name = models.CharField(max_length=255)
    file1 = models.FileField(upload_to=site_name_str, blank=True, null=True)
    file2 = models.FileField(upload_to=site_name_str, blank=True, null=True)
    file3 = models.FileField(upload_to=site_name_str, blank=True, null=True)
    file4 = models.FileField(upload_to=site_name_str, blank=True, null=True)
    file5 = models.FileField(upload_to=site_name_str, blank=True, null=True)
    file6 = models.FileField(upload_to=site_name_str, blank=True, null=True)
    file7 = models.FileField(upload_to=site_name_str, blank=True, null=True)

    state = models.BooleanField(default=True, editable=False)
    sub_state = models.BooleanField(default=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('created_at',)
        verbose_name = 'site'
        verbose_name_plural = 'sites'

    def __str__(self):
        return self.site_name
