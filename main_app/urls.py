from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('records/', views.records_index, name='index'),
    path('records/<int:record_id>/', views.records_detail, name='detail'),
    path('records/create/',views.RecordCreate.as_view(), name='records_create'),
    path('records/<int:pk>/update/',views.RecordUpdate.as_view(), name='records_update'),
    path('records/<int:pk>/delete/',views.RecordDelete.as_view(), name='records_delete'),
    path('records/<int:record_id>/add_review', views.add_review, name='add_review'),
    path('records/<int:record_id>/assoc_crate/<int:crate_id>/', views.assoc_crate, name='assoc_crate'),
    path('crates/', views.CrateList.as_view(), name='crates_index'),
    path('crates/<int:pk>/', views.CrateDetail.as_view(), name='crates_detail'),
    path('crates/create/', views.CrateCreate.as_view(), name='crates_create'),
    path('crates/<int:pk>/update/', views.CrateUpdate.as_view(), name='crates_update'),
    path('crates/<int:pk>/delete/', views.CrateDelete.as_view(), name='crates_delete'),
]