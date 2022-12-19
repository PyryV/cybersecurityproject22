from django.shortcuts import redirect, render

from secretsmanager.models import Secret, UserClearanceLevel

def getSecrets(user):
    print(user.id)
    ##clearance_level = UserClearanceLevel.objects.get(user_id=str(user.id))['clearancelevel']
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
    return redirect('secretsmanager/')

def secretView(request, id):
    if request.method == 'GET':
        secret = Secret.objects.get(id=id)
        context = {'secret': secret}
    return render(request, 'secret.html', context)

def newSecretView(request):
    return render(request, 'newSecret.html')

def homePageView(request):
    if request.method == 'GET':
        user = request.user
        secrets = getSecrets(user)
        context = {'secrets': secrets}
    return render(request, 'index.html', context)