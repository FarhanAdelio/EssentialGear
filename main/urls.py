from django.urls import path
from main.views import show_main, create_gear_entry,show_xml,show_json, show_xml_by_id, show_json_by_id
from main.views import register
from main.views import login_user
from main.views import logout_user
from main.views import edit_gear
from main.views import delete_gear
from main.views import add_gear_entry_ajax
from main.views import create_gear_flutter

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-gear-entry', create_gear_entry, name='create_gear_entry'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:id>/', show_json_by_id, name='show_json_by_id'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('edit-gear/<uuid:id>', edit_gear, name='edit_gear'),
    path('delete/<uuid:id>', delete_gear, name='delete_gear'), # sesuaikan dengan nama fungsi yang dibuat
    path('create-gear-entry-ajax', add_gear_entry_ajax, name='add_gear_entry_ajax'),
    path('create-flutter/', create_gear_flutter, name='create_gear_flutter'),


]