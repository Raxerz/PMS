from django.contrib import admin

# Register your models here.
from .models import Studentinfo
from .models import Studcontact
from .models import Studemail
from .models import Profinfo
from .models import Profemail
from .models import Profcontact
from .models import Projprofcom


admin.site.register(Studentinfo)
admin.site.register(Studcontact)
admin.site.register(Studemail)
admin.site.register(Profinfo)
admin.site.register(Profemail)
admin.site.register(Profcontact)
admin.site.register(Projprofcom)


