# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(CustomerCare)
admin.site.register(CustomerCondition)
admin.site.register(CustomerInfo)
admin.site.register(CustomerLinkman)
admin.site.register(CustomerLinkreord)
admin.site.register(CustomerSource)
admin.site.register(CustomerType)
admin.site.register(DepartmentInfo)
admin.site.register(DjangoMigrations)
admin.site.register(EmailInfo)
admin.site.register(HouseInfo)
admin.site.register(HouseType)
admin.site.register(NoticeInfo)
admin.site.register(UserInfo)
admin.site.register(UserRole)