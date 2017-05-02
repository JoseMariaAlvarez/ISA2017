# -*- encoding: utf-8 -*-
from django.contrib import admin
from .models import Comentario, PacienteClinica, Diagnostico, Medicacion, Visita


"""class AuthDBModelAdmin(admin.ModelAdmin):
	# Customized DBModel for multi-db compatibility

    using = 'Auth'


    def save_model(self, request, obj, form, change):
    	# save_model to database Auth
        obj.save(using=self.using)

    def delete_model(self, request, obj):
    	# delete_model from database Auth
        obj.delete(using=self.using)

    def get_queryset(self, request):
    	# query to Auth
        return super(AuthDBModelAdmin, self).get_queryset(request).using(self.using)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
    	# Populate foreignkeys using a query
        return super(AuthDBModelAdmin, self).formfield_for_foreignkey(db_field, request, using=self.using, **kwargs)

    def formfield_for_manytomany(self, db_field, request, **kwargs):
    	# Populate M2M widgets using a query
        return super(AuthDBModelAdmin, self).formfield_for_manytomany(db_field, request, using=self.using, **kwargs)
"""

## Añadimos los modelos para ser modificados desde el panel de administrador (/admin/)
## Si queremos acceder al panel, debemos crear un superusuario antes.
admin.site.register(Comentario)
admin.site.register(PacienteClinica)
admin.site.register(Diagnostico)
admin.site.register(Medicacion)
admin.site.register(Visita)
