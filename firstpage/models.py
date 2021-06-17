from django.db import models

from django.db import models
from django.forms import ModelForm
from django.forms.models import model_to_dict


class table(models.Model):
    Account_length=models.IntegerField()
    Area_code=models.IntegerField()
    Number_vmail_messages=models.IntegerField()
    Total_day_minutes=models.IntegerField()
    Total_day_calls=models.IntegerField()
    Total_day_charge=models.IntegerField()
    Total_eve_minutes=models.IntegerField()
    Total_eve_calls=models.IntegerField()
    Total_eve_charge=models.IntegerField()
    Total_night_minutes=models.IntegerField()
    Total_night_calls=models.IntegerField()
    Total_night_charge=models.IntegerField()
    Customer_service_calls=models.IntegerField()
    Voice_mail_plan=models.IntegerField()
    International_plan=models.IntegerField()
    international_voice_call_usage=models.IntegerField()

    def __int__(self):
        return self.Account_length;
    
    def natural_key(self):
        print("natural keys--office")
        return model_to_dict(self)


class TableForm(ModelForm):
    class Meta:
        model = table
        fields = "__all__"

