from django.contrib import admin
from .models import footerAdmin, ostanha, shahrha, maghtaTahsili, reshteTahsili, modaresin,sliderImage,advertise,pagecunter



class advertiseShow(admin.ModelAdmin):
    list_display = ('hru', 'hlu','hrd','hld','fru','flu','frd','fld')
   

admin.site.register(advertise, advertiseShow)
    

admin.site.register(sliderImage)


class pagecuntershow(admin.ModelAdmin):
    list_display = ('counter',)

admin.site.register(pagecunter, pagecuntershow)    

class FooterAdminShow(admin.ModelAdmin):
    list_display = ('mail', 'whatsapp','instagram')

admin.site.register(footerAdmin, FooterAdminShow)
    
 
    
admin.site.register(ostanha)


class ShahrShow(admin.ModelAdmin):
    list_display = ('ostanNamefkey', 'shahrNames')
    
admin.site.register(shahrha, ShahrShow)

    
admin.site.register(maghtaTahsili)


class reshteTahsiliShow(admin.ModelAdmin):
    list_display = ('maghtafkey', 'reshte')
   
admin.site.register(reshteTahsili, reshteTahsiliShow)



class modaresinshow(admin.ModelAdmin):
    list_display = ('modares', 'email_modares')
   
admin.site.register(modaresin, modaresinshow)