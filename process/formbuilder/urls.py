from django.urls import path

from process.formbuilder import views

urlpatterns = [
    path('org/<int:organization_id>/create/', views.CreateFormView.as_view()),
    path('org/<int:organization_id>/update/<int:form_id>/', views.UpdateFormView.as_view()),
    path('org/<int:organization_id>/view/<int:form_id>/', views.ViewForm.as_view()),
    path('test/', views.TestFormView.as_view()),
]
