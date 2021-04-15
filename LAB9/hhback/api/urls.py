from django.urls import path
from api.views import vacancies_list, vacancy_detail, company_detail, companies_list, top, coco

urlpatterns = [
    path('vacancies/', vacancies_list),
    path('vacancies/<int:vacancy_id>/', vacancy_detail),
    path('companies/', companies_list),
    path('companies/<int:company_id>/', company_detail),
    path('vacancies/top_ten', top),
    path('companies/<int:company_id>/vacancies', coco)
]
