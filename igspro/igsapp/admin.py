from django.contrib import admin

# Register your models here.
from .models import ContactData,Service,FeedbackData,ImageData,GraphData

admin.site.register(ContactData)

admin.site.register(Service)

admin.site.register(ImageData)
admin.site.register(GraphData)




admin.site.register(FeedbackData)
# admin.site.register(Passenger)