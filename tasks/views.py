from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import authenticate, login as dj_login, logout as dj_logout
from django.views.decorators.cache import cache_page
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
import logging
logger = logging.getLogger('tms')

from .models import Task, Contractor, Employer
from .forms import SignupForm
PAGINATION_PER_PAGE = 2


# @cache_page(60 * 5)
@csrf_exempt
def index(request):
    logger.info('index page request received')
    # page number
    if request.GET.get("page"):
        page_number = int(request.GET.get("page"))
    elif request.COOKIES.get("page_number"):
        page_number = int(request.COOKIES.get("page_number"))
    else:
        page_number = 1

    tasks = Task.objects.all().order_by("-created_at")
    paginator = Paginator(tasks, PAGINATION_PER_PAGE)
    page = paginator.get_page(page_number)
    context = {
        "task_page": page,
        "user": request.user,
        "form": SignupForm(),
        "user_type": "کارفرما" if hasattr(request.user, "employer") else "پیمانکار",
        "is_employer": hasattr(request.user, "employer"),
    }

    response = render(request, "index.html", context)
    response.set_cookie("page_number", str(page_number))
    return response


@csrf_exempt
@login_required(login_url="/tasks/login-required/")
def detail(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    context = {
        "task": task,
        "user": request.user,
        "is_employer": hasattr(request.user, "employer"),
    }
    return render(request, "details.html", context=context)


@csrf_exempt
@permission_required("tasks.add_task", raise_exception=True)
def new_task(request):
    from .forms import TaskForm
    if request.method == "GET":
        context = {
            "form": TaskForm(),
        }
        return render(request, "new_task.html", context)
    elif request.method == "POST":
        form = TaskForm(request.POST)
        print(request.POST)
        if not form.is_valid():
            return HttpResponse(str(form.errors))

        print(form.instance)
        form.instance.owner = request.user.employer
        form.save()
        return HttpResponseRedirect(reverse("index"))


@csrf_exempt
def assign_task(request, task_id):
    task = Task.objects.get(pk=task_id)
    contractor = Contractor.objects.get(user=request.user)
    task.assigned_contractor = contractor
    task.save()
    return HttpResponseRedirect(reverse("index"))


@csrf_exempt
def register(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if not form.is_valid():
            return HttpResponse(str(form.errors))

        user = form.save()

        from django.contrib.auth.models import Permission
        if form.cleaned_data.get("user_type") == "employer":
            permission = Permission.objects.get(name='Can add task')
            user.user_permissions.add(permission)
            Employer.objects.create(user=user)
        else:
            Contractor.objects.create(user=user)

        dj_login(request, user)
        return HttpResponseRedirect(reverse("index"))


@csrf_exempt
def login_required_error(request):
    return HttpResponse("لطفا ابتدا ورود کنید")


@csrf_exempt
def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)
        if user:
            dj_login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return HttpResponse("Wrong inputs", status=400)


@csrf_exempt
def logout(request):
    dj_logout(request)
    return HttpResponseRedirect(reverse("index"))
