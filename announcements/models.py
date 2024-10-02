from django.core.exceptions import ValidationError
from django.db import models
from users.models import User
from django.utils import timezone
import phonenumbers
from phonenumbers import NumberParseException
from rest_framework import serializers
from .storages import CustomFileSystemStorage

custom_storage = CustomFileSystemStorage()

# Create your models here.

class Announcement(models.Model):
    class Meta:
        ordering = ['-id']
    project_name = models.CharField(max_length=100)
    deadline = models.DateField()
    cost = models.IntegerField()
    tashkilot_nomi = models.CharField(max_length=50) #
    description = models.CharField(max_length=700)#
    phone = models.CharField(max_length=15, help_text='+998 bilan kiriting!!!')#
    name_of_employer = models.CharField(max_length=30)#
    assigned_to = models.ForeignKey(User, on_delete=models.SET_NULL, limit_choices_to={'deleted_at': None}, null=True, blank=True, related_name='assignments')
    file1 = models.FileField(upload_to='documents', storage=custom_storage, null=True)
    file2 = models.FileField(upload_to='documents', storage=custom_storage, null=True)
    file3 = models.FileField(upload_to='documents', storage=custom_storage, null=True)
    remove_file1 = models.BooleanField(default=False)
    remove_file2 = models.BooleanField(default=False)
    remove_file3 = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(null=True, blank=True, default=None)

    def __str__(self):
        return self.project_name


    # def delete(self, *args, **kwargs):
    #     self.deleted_at = timezone.now()
    #     self.save()


    def clean(self):
        try:
            parsed_number = phonenumbers.parse(self.phone, None)
            if not phonenumbers.is_valid_number(parsed_number):
                raise serializers.ValidationError({'error_massage' : "Invalid phone number"})
        except NumberParseException:
            raise serializers.ValidationError({'error_massage' : "Invalid phone number format"})


    def save(self, *args, **kwargs):
        if self.pk:
            existing_instance = Announcement.objects.get(pk=self.pk)

            # Handle file1
            if not self.file1 and not self.remove_file1:
                self.file1 = existing_instance.file1
            elif self.remove_file1:
                self.file1 = None
                self.remove_file1 = False  # Reset the flag

            # Handle file2
            if not self.file2 and not self.remove_file2:
                self.file2 = existing_instance.file2
            elif self.remove_file2:
                self.file2 = None
                self.remove_file2 = False  # Reset the flag

            # Handle file3
            if not self.file3 and not self.remove_file3:
                self.file3 = existing_instance.file3
            elif self.remove_file3:
                self.file3 = None
                self.remove_file3 = False  # Reset the flag

        self.clean()  # Call the clean method to perform any model validation
        super().save(*args, **kwargs)





    # def update(self, *args, **kwargs):
    #     self.updated_at = datetime.now().strftime('%d-%m-%Y %H:%M')
    #     self.save()

    # def delete(self, *args, **kwargs):
    #     self.deleted_at = datetime.now().strftime('%d-%m-%Y %H:%M')
    #     self.save()


class WorkRequest(models.Model):
    class Meta:
        ordering = ['-id']
    announcement = models.ForeignKey(Announcement, on_delete=models.CASCADE, limit_choices_to={'assigned_to' : None, 'deleted_at': None}, related_name='requests')
    requester = models.ForeignKey(User, on_delete=models.CASCADE, related_name='work_requests')
    status = models.CharField(max_length=50, choices=[('refused', 'Rad Etilgan'), ('pending', 'Kutilyapti'), ('accepted', 'Qabul qilingan')], default='pending')
    deadline = models.DateField()
    cost = models.IntegerField()
    description = models.CharField(max_length=700)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(null=True, blank=True, default=None)
    # class Meta:
    #     unique_together = ('announcement', 'requester')


    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.status == 'accepted':
            announcement = self.announcement
            announcement.assigned_to = self.requester
            announcement.save()
            WorkRequest.objects.filter(announcement=self.announcement).exclude(id=self.id).update(status='refused')

    def __str__(self):
        return f'Request by {self.requester.username} for {self.announcement.project_name}'

    
    # def delete(self, *args, **kwargs):
    #     self.deleted_at = timezone.now()
    #     self.save()
