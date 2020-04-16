from django.db import models
from django.contrib.auth.models import User
from app.other_constants import *


#
#
#
class AccGroups(models.Model):

    user = models.ForeignKey(
        User,
        db_index = True,
        on_delete = models.CASCADE,
    )

    major_head = models.IntegerField(        
        db_index = True,
        null = True,
        blank = True,
    )
    
    group_name = models.CharField(
        max_length = 250,
        blank = True,
        null = True,
    )

    group_info = models.TextField(
        blank = True,
        null = True,
    )

    is_active = models.BooleanField(
        db_index = True,
        default = True,
        choices = user_constants.IS_TRUE,
    )

    def __str__(self):
        return self.group_name

#
#
#
class AccLedger(models.Model):

    user = models.ForeignKey(
        User,
        db_index = True,
        on_delete = models.CASCADE,
    )

    acc_group = models.CharField(
        max_length = 200,
        db_index = True,
        null = True,
        blank = True,
    ) 

    accounts_name = models.CharField(
        max_length = 250,
        blank = True,
        null = True,
    )

    major_heads = models.IntegerField(
        null = True,
        blank = True,
        db_index = True,
        choices = accounts_constant.LEDGER_ACCOUNT_CHOICES,
    )

    info_message = models.TextField(
        null = True,
        blank = True,
    )

    description = models.TextField(
        blank = True,
        null = True,
    )

    is_active = models.BooleanField(
        db_index = True,
        default = True,
        choices = user_constants.IS_TRUE,
    )

    def __str__(self):
        return self.accounts_name

