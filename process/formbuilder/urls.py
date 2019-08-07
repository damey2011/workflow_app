from django.urls import path

from process.formbuilder import views

urlpatterns = [
    path('org/<int:organization_id>/create/', views.CreateFormView.as_view()),
    path('org/<int:organization_id>/update/<int:form_id>/', views.UpdateFormView.as_view()),
    path('org/<int:organization_id>/view/<int:form_id>/', views.ViewForm.as_view()),
    path('org/<int:organization_id>/view/<int:form_id>/responses/', views.ViewFormResponses.as_view()),
    path('org/<int:organization_id>/view/<int:form_id>/responses/<int:response_id>/', views.ViewFormResponse.as_view()),
    path('test/', views.TestFormView.as_view()),
]
