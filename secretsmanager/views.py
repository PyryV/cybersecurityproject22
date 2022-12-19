from django.shortcuts import render

from secretsmanager.models import Secret, UserClearanceLevel

def getSecrets(user):
    clearance_level = UserClearanceLevel.objects.get(user_id=user.id)['clearance_level']
    if clearance_level == 'TOP_SECRET':
        return Secret.objects.all()
    elif clearance_level == 'CLASSIFIED':
        return Secret.objects.exclude(classification='TOP_SECRET')
    else:
        return Secret.objects.filter(classification='PUBLIC')

def secretView(request):
    if request.method == 'GET':
        secret_title = request.GET.get('title')
        secret = Secret.objects.get(title=secret_title)
        context = {'secret': secret}
    return render(request, 'ui/secret.html', context)

def homePageView(request):
    if request.method == 'GET':
        user = request.user
        secrets = getSecrets(user)
        context = {'secrets': secrets}
    return render(request, 'ui/index.html', context)