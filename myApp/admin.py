from django.contrib import admin
from .models import I_do,Portfolio,Skill,Blog,Award,Profile
# Register your models here.
class whatDoAdmin(admin.ModelAdmin):
    list_display=['job_name','icons']
admin.site.register(I_do,whatDoAdmin)


class PortAdmin(admin.ModelAdmin):
    list_display=['title']
admin.site.register(Portfolio,PortAdmin)


class SkillAdmin(admin.ModelAdmin):
    list_display=['name_work_skill']
admin.site.register(Skill,SkillAdmin)


class BlogAdmin(admin.ModelAdmin):
    list_display=['name_blog']
admin.site.register(Blog,BlogAdmin)


class AwardAdmin(admin.ModelAdmin):
    list_display=['award_title']
admin.site.register(Award,AwardAdmin)


class ProfileAdmin(admin.ModelAdmin):
    list_display=['name']
admin.site.register(Profile,ProfileAdmin)