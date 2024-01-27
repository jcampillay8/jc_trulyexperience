def index(request):
    return redirect('expenses')


@login_required(login_url='/authentication/login')
def search_expenses(request):
    search_val = json.loads(request.body).get('data')
    expenses = Expense.objects.filter(name__icontains=search_val, owner=request.user) | Expense.objects.filter(
        amount__startswith=search_val, owner=request.user) | Expense.objects.filter(
        date__icontains=search_val, owner=request.user) | Expense.objects.filter(
        category__icontains=search_val, owner=request.user)
    data = list(expenses.values())
    return JsonResponse(data, safe=False)


@login_required(login_url='/authentication/login')
def expenses(request):

    if not Setting.objects.filter(user=request.user).exists():
        messages.info(request, 'Please choose your preferred currency')
        return redirect('general-settings')
    categories = Category.objects.all()
    expenses = Expense.objects.filter(owner=request.user)
    paginator = Paginator(expenses, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    currency = Setting.objects.get(user=request.user).currency
    context = {
        'currency': currency.split('-')[0],
        'categories': categories,
        'expenses': expenses,
        'page_obj': page_obj,
    }
    return render(request=request, template_name='expenses/index.html', context=context)


@login_required(login_url='/authentication/login')
def expenses_add(request):
    categories = Category.objects.all()

    if not Setting.objects.filter(user=request.user).exists():
        messages.info(request, 'Please choose your preferred currency')

        return redirect('general-settings')

    if request.method == 'GET':
        context = {
            'categories': categories,
            'settings': Setting.objects.filter(user=request.user)[0] if Setting.objects.filter(user=request.user).exists() else {}
        }
        return render(request=request, template_name='expenses/new.html', context=context)
    context = {
        'values': request.POST,
        'categories': categories,
    }
    amount = request.POST['amount']
    name = request.POST['name']
    category = request.POST['category']
    date = request.POST['ex_date']
    if not amount:
        messages.error(request,  'Amount is required')
        return render(request=request, template_name='expenses/new.html', context=context)

    if not date:
        messages.error(request,  'Date is required')
        return render(request=request, template_name='expenses/new.html', context=context)
    if not category:
        messages.error(request,  'Expense Category is required')
        return render(request=request, template_name='expenses/new.html', context=context)
    expense = Expense.objects.create(
        amount=amount, name=name, date=date, category=category, owner=request.user)

    if expense:
        messages.success(request,  'Expense was submitted successfully')
        return redirect('expenses')

    return render(request=request, template_name='expenses/index.html')


@login_required(login_url='/authentication/login')
def expense_edit(request, id):
    expense = Expense.objects.get(pk=id)
    categories = Category.objects.all()
    data = []
    arr = []

    file = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    file_path = os.path.join(file, 'currencies.json')
    with open(file_path, 'r') as json_file:
        data = json.load(json_file)
        json_file.close()
    categories = Category.objects.all()
    context = {
        'values': request.POST,
        'categories': categories,
        'expense': expense
    }
    if request.method == 'GET':
        context = {
            'values': expense,
            'categories': categories,
            'expense': expense
        }
        return render(request, 'expenses/edit.html', context)
    amount = request.POST['amount']
    category = request.POST['category']
    name = request.POST['name']
    if not amount:
        messages.error(request,  'Amount is required')
        return render(request, 'expenses/edit.html', context)
    expense.amount = amount
    expense.name = name
    expense.category = category
    expense.save()
    messages.success(request,  'Expense updated successfully')
    return redirect('expenses')


@login_required(login_url='/authentication/login')
def expense_delete(request):
    expenses = Expense.objects.all_expenses()
    context = {
        'expenses': expenses
    }
    return render('expenses/index.html', context)