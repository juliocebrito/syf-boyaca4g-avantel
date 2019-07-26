from django.db import models
from django.core.exceptions import ValidationError
from django.urls import reverse
from . import choices
from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver


class HardwareCategory(models.Model):
    name = models.CharField(max_length=255, unique=True)
    state = models.BooleanField(default=True, editable=False)
    sub_state = models.BooleanField(default=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('created_at',)
        verbose_name = 'hardware category'
        verbose_name_plural = 'hardware categories'

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse('hardware:hardware_category_detail', kwargs={'pk': self.pk})


class Hardware(models.Model):
    hardware_category = models.ForeignKey(HardwareCategory, on_delete=models.CASCADE)
    cs_code = models.CharField(max_length=255, unique=True)
    supervendor_code = models.CharField(max_length=255)
    material_description = models.CharField(max_length=255, blank=True, null=True)
    unity = models.CharField(max_length=255,  choices=choices.UNITY_CHOICES, blank=True, null=True)
    total_quantity = models.PositiveIntegerField(default=0, editable=False)
    state = models.BooleanField(default=True, editable=False)
    sub_state = models.BooleanField(default=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('created_at',)
        verbose_name = 'hardware'
        verbose_name_plural = 'hardware'

    def __str__(self):
        return self.cs_code

    # def get_absolute_url(self):
    #     return reverse('hardware:hardware_detail', kwargs={'pk': self.pk})


class HardwareControl(models.Model):
    hardware = models.ForeignKey(Hardware, on_delete=models.CASCADE)
    serial = models.CharField(max_length=255, unique=True)
    site = models.CharField(max_length=255, blank=True, null=True)
    quantity = models.PositiveIntegerField(default=1, editable=False)
    hardware_state = models.CharField(max_length=255, choices=choices.HARDWARE_STATE_CHOICES, default=choices.HARDWARE_STATE_CHOICES[0][0])
    state = models.BooleanField(default=True, editable=False)
    sub_state = models.BooleanField(default=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('created_at',)
        verbose_name = 'hardware control'
        verbose_name_plural = 'hardware controls'

    def __str__(self):
        return self.serial

    # def get_absolute_url(self):
    #     return reverse('hardware:hardware_detail', kwargs={'pk': self.pk})

    def clean(self, *args, **kwargs):
        if self.hardware_state == choices.HARDWARE_STATE_CHOICES[1][1]:
            try:
                hardware_control_log = self.hardwarecontrollog
            except HardwareControlLog.DoesNotExist:
                raise ValidationError('Serial {0} not inventoried'.format(self.serial))
            if self.hardware.total_quantity == 0:
                raise ValidationError('Hardware {0} quantity is 0'.format(self.hardware))
            if self.hardware.total_quantity < self.quantity:
                raise ValidationError('Hardware {0} quantity is not enough'.format(self.hardware))
        if self.hardware_state == choices.HARDWARE_STATE_CHOICES[2][1]:
            try:
                hardware_control_log = self.hardwarecontrollog
            except HardwareControlLog.DoesNotExist:
                raise ValidationError('Serial {0} not inventoried'.format(self.serial))
            if self.hardware.total_quantity == 0:
                raise ValidationError('Hardware {0} quantity is 0'.format(self.hardware))
            if self.hardware.total_quantity < self.quantity:
                raise ValidationError('Hardware {0} quantity is not enough'.format(self.hardware))
        if self.site and self.hardware_state != choices.HARDWARE_STATE_CHOICES[1][1]:
            raise ValidationError('Hardware state must be {0}'.format(choices.HARDWARE_STATE_CHOICES[1][1]))
        if not self.site and self.hardware_state == choices.HARDWARE_STATE_CHOICES[1][1]:
            raise ValidationError('Hardware {0} has not Site assigned'.format(self.hardware))


class HardwareControlLog(models.Model):
    hardware_control = models.OneToOneField(HardwareControl, on_delete=models.CASCADE)
    hardware = models.ForeignKey(Hardware, on_delete=models.CASCADE)
    serial = models.CharField(max_length=255, unique=True)
    site = models.CharField(max_length=255, blank=True, null=True)
    quantity = models.PositiveIntegerField(default=1, editable=False)
    hardware_state = models.CharField(max_length=255, choices=choices.HARDWARE_STATE_CHOICES, default=choices.HARDWARE_STATE_CHOICES[0][0])
    state = models.BooleanField(default=True, editable=False)
    sub_state = models.BooleanField(default=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('created_at',)
        verbose_name = 'hardware control log'
        verbose_name_plural = 'hardware control log'

    def __str__(self):
        return self.serial

    @receiver(post_save, sender=HardwareControl)
    def create_hardware_control_log(sender, instance, created, **kwargs):
        if created:
            hardware_control_log, new = HardwareControlLog.objects.get_or_create(hardware_control=instance,
                                                                                 hardware=instance.hardware,
                                                                                 serial=instance.serial,
                                                                                 site=instance.site,
                                                                                 quantity=instance.quantity,
                                                                                 hardware_state=instance.hardware_state,
                                                                                 )
            if instance.hardware_state == choices.HARDWARE_STATE_CHOICES[0][1]:
                instance.hardware.total_quantity = instance.hardware.total_quantity + instance.quantity
                instance.hardware.save()

    @receiver(post_save, sender=HardwareControl)
    def save_hardware_control_log(sender, instance, **kwargs):

        if instance.hardware_state != instance.hardwarecontrollog.hardware_state:

            if instance.hardware_state == choices.HARDWARE_STATE_CHOICES[0][1]:
                instance.hardware.total_quantity = instance.hardware.total_quantity + instance.quantity
                instance.hardware.save()

            if instance.hardware_state == choices.HARDWARE_STATE_CHOICES[1][1] and instance.hardwarecontrollog.hardware_state != choices.HARDWARE_STATE_CHOICES[2][1]:
                instance.hardware.total_quantity = instance.hardware.total_quantity - instance.quantity
                instance.hardware.save()

            if instance.hardware_state == choices.HARDWARE_STATE_CHOICES[2][1] and instance.hardwarecontrollog.hardware_state != choices.HARDWARE_STATE_CHOICES[1][1]:
                instance.hardware.total_quantity = instance.hardware.total_quantity - instance.quantity
                instance.hardware.save()

        instance.hardwarecontrollog.hardware_control = instance
        instance.hardwarecontrollog.hardware = instance.hardware
        instance.hardwarecontrollog.serial = instance.serial
        instance.hardwarecontrollog.site = instance.site
        instance.hardwarecontrollog.quantity = instance.quantity
        instance.hardwarecontrollog.hardware_state = instance.hardware_state
        instance.hardwarecontrollog.save()

    @receiver(post_delete, sender=HardwareControl)
    def discount_total_quantity(sender, instance, *args, **kwargs):
        if instance.hardware_state == choices.HARDWARE_STATE_CHOICES[0][1]:
            instance.hardware.total_quantity = instance.hardware.total_quantity - instance.quantity
            instance.hardware.save()
        if instance.hardware_state == choices.HARDWARE_STATE_CHOICES[1][1]:
            instance.hardware.total_quantity = instance.hardware.total_quantity + instance.quantity
            instance.hardware.save()
        if instance.hardware_state == choices.HARDWARE_STATE_CHOICES[2][1]:
            instance.hardware.total_quantity = instance.hardware.total_quantity + instance.quantity
            instance.hardware.save()
