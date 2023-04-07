from django.shortcuts import render
from django.http.response import  HttpResponse, JsonResponse
from django.http.request import HttpRequest

from api.models import Vacancy, Company

# Create your views here.
def vacancies_list(request):
    vacancies = Vacancy.objects.all()
    vacancies_json = [vacancy.to_json() for vacancy in vacancies]

    return JsonResponse(vacancies_json, safe=False)

def vacancy_detail(request, id):
    try:
        vacancy = Vacancy.objects.get(id=id)
    except Exception as e:
        return JsonResponse({'message': str(e)}, status=400)

    return JsonResponse(vacancy.to_json())

def companies_list(request):
    companies = Company.objects.all()
    companies_json = [company.to_json() for company in companies]
    response =  JsonResponse(companies_json, safe=False)
    response["Access-Control-Allow-Origin"] = "*"

    return response

def company_detail(request, id):
    try:
        company = Company.objects.get(id=id)
    except Exception as e:
        return JsonResponse({'message': str(e)}, status=400)

    return JsonResponse(company.to_json())

def vacancies_by_company(request, id):
    vacancies = Vacancy.objects.all()
    vacancies_by_company_json = []

    for vacancy in vacancies:
        if vacancy.company.id == id:
            vacancies_by_company_json.append(vacancy.to_json())

    return JsonResponse(vacancies_by_company_json, safe=False)

def topTen_vacancies(request):
    vacancies = Vacancy.objects.all().order_by('-salary','id')
    top_ten_json = [vacancy.to_json() for vacancy in vacancies]

    return JsonResponse(top_ten_json[:3], safe=False)