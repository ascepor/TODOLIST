import datetime
from django.db import models
from django.forms import ValidationError

#Choices for status option
SHOW_STATUS = [
        ('open','OPEN'),
        ('working','WORKING'),
        ('done','DONE'),
        ('overdue','OVERDUE')
    ]
# Date Validation for Due date it cannot be prior to the created date
def validate_date(date):
    if date < datetime.datetime.now().date():
        raise ValidationError("Date cannot be in the past")

# Create your models here.
class ToDo(models.Model):
    Title = models.CharField(max_length=100, blank=False) #Mandatory
    Description = models.TextField(max_length=1000, blank=False)#Mandatory
    created = models.DateTimeField(auto_now_add=True, editable=False)  #Timestamp uneditable
    Due_Date = models.DateField(null=True, blank=True, default=None, validators=[validate_date]) #Validate
    Tag = models.CharField(max_length=50, blank=False, unique=True) # one tag only able to use only once
    Status = models.CharField(max_length=7, choices=SHOW_STATUS, default='OPEN')
    DisplayFields = ['id', 'Title', 'Description', 'created', 'Due_Date', 'Tag', 'Status']#Filter For display
    FilterFields = ['id', 'created', 'Due_Date', 'Status'] #Filter for models


    def __str__(self):
        return self.Title