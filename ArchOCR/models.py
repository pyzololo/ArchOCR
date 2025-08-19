from django.conf import settings
from django.db import models
from django.utils import timezone
import uuid


class ScanPage(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="scans")
    image = models.ImageField(upload_to="scans/%Y/%m/%d/")
    uploaded_at = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ["-uploaded_at"]

    def __str__(self):
        filename = self.image.name.split('/')[-1] if self.image else "—"
        short_id = str(self.id)[:8]
        return f"{short_id}, {self.owner}, {filename}, {self.uploaded_at:%Y-%m-%d %H:%M}"


class Translation(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    page = models.ForeignKey(ScanPage, on_delete=models.CASCADE, related_name="translations")
    model_name = models.CharField(max_length=100)
    text = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        preview = (self.text[:40] + "…") if self.text and len(self.text) > 40 else (self.text or "")
        return f"{self.model_name}, {self.created_at:%Y-%m-%d %H:%M}, {preview}"

