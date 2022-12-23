import sqlite3
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from secretsmanager.models import Secret, UserClearanceLevel

def getSecrets(user):
    print(user.id)
    clearance_level = UserClearanceLevel.objects.get(user_id=str(user.id))['clearancelevel']
    clearance_level = 'TOP_SECRET'
    if clearance_level == 'TOP_SECRET':
        return Secret.objects.all()
    elif clearance_level == 'CLASSIFIED':
        return Secret.objects.exclude(classification='TOP_SECRET')
    else:
        return Secret.objects.filter(classification='PUBLIC')

def addSecret(request):
    if request.method == 'POST':
        new_secret = Secret(
            title = request.POST.get('title'),
            classification = request.POST.get('classification'),
            secret = request.POST.get('secret')
        )
        new_secret.save()
    return redirect('/secretsmanager/')

def secretView(request, id):
    if request.method == 'GET':
        #secret = Secret.objects.get(id=id)
        #context = {'secret': secret}
        conn = sqlite3.connect('db.sqlite3')
        cursor = conn.cursor()
        sql = 'SELECT * FROM secretsmanager_secret WHERE id='+str(id)+';'
        r = cursor.execute(sql).fetchall()[0]
        secret_object = Secret(
            title = r[0],
            classification = r[1],
            secret = r[2]
        )
        context = {'secret': secret_object}
    return render(request, 'secret.html', context)

def newSecretView(request):
    return render(request, 'newSecret.html')

def logoutView(request):
    logout(request)
    return redirect('/secretsmanager/')

def loginView(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/secretsmanager/')
        else:
            return redirect('/secretsmanager/')


@login_required(login_url='/secretsmanager/login/')
def homePageView(request):
    if request.method == 'GET':
        user = request.user
        secrets = getSecrets(user)
        context = {'secrets': secrets}
    return render(request, 'index.html', context)