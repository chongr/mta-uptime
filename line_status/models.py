import datetime

from django.db import models
from django.utils.timezone import utc

# Create your models here.

class LineStatus(models.Model):
    line_name = models.CharField(max_length=1, primary_key=True)
    delayed = models.BooleanField(default=False)
    created_at = models.DateTimeField(blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)
    delayed_time = models.IntegerField(default=0)

    def __init__(self, *args, **kwargs):
        super(LineStatus, self).__init__(*args, **kwargs)
        self.orignal_status = self.delayed
        self.orignal_updated_at = self.updated_at

    def to_json(self):
        return {"line_name": self.line_name, "delayed": self.delayed}

    def get_delayed_time(self):
        if self.delayed:
            now = datetime.datetime.utcnow().replace(tzinfo=utc)
            timediff = now - self.updated_at
            additional_delayed_time += timediff.total_seconds()
            return self.delayed_time + additional_delayed_time
        return self.delayed_time

    def save(self, *args, **kwargs):
        now = datetime.datetime.utcnow().replace(tzinfo=utc)
        self.updated_at = now
        # not delayed anymore add to delayed time
        if self.orignal_status != self.delayed and self.delayed == False:
            timediff = now - self.orignal_updated_at
            self.delayed_time += timediff.total_seconds()
        super(LineStatus, self).save(*args, **kwargs)
