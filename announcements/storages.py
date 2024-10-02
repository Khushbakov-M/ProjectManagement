import os
import uuid
from django.core.files.storage import FileSystemStorage
from django.utils.deconstruct import deconstructible

@deconstructible
class CustomFileSystemStorage(FileSystemStorage):
    def get_available_name(self, name, max_length=None):
        base, extension = os.path.splitext(name)
        while self.exists(name):
            name = f"{base}*{uuid.uuid4().hex}{extension}"
        return name[:max_length] if max_length else name
