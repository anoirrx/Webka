from django.http.response import JsonResponse
from api.models import Company, Vacancy

def vacancies_list(request):
    vacancies = Vacancy.objects.all()
    vacancies_json = [vacancy.to_json() for vacancy in vacancies]
    return JsonResponse(vacancies_json, safe=False)


def vacancy_detail(request, vacancy_id):
    try:
        vacancy = Vacancy.objects.get(id=vacancy_id)
    except Vacancy.DoesNotExist as e:
        return JsonResponse({'message': str(e)}, status=400)

    return JsonResponse(vacancy.to_json())

def companies_list(request):
    companies = Company.objects.all()
    companies_json = [company.to_json() for company in companies]
    return JsonResponse(companies_json, safe=False)

def company_detail(request, company_id):
    try:
        company = Company.objects.get(id=company_id)
    except Company.DoesNotExist as c:
        return JsonResponse({'message': str(c)}, status=400)

    return JsonResponse(company.to_json())

def top(request):
    vacancies = list(Vacancy.objects.order_by('salary').reverse()[:10].values())
    return JsonResponse(vacancies, safe=False)

def coco(request, company_id):
    company = Company.objects.get(id=company_id)
    vacancies = list(company.vacancies.values())
    return JsonResponse(vacancies, safe=False)
