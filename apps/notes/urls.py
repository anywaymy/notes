from django.urls import path, include
from . views import NoteListCreateView, NoteDetailView

app_name = 'notes'


urlpatterns = [
    path('notes/', NoteListCreateView.as_view(), name="note-list-create"),
    path('notes/<int:pk>', NoteDetailView.as_view(), name="note-detail"),
    # path('api/v1', include('apps.notes.urls'))
]