from django.http import JsonResponse


def home(request):
    return JsonResponse({
        'message': '欢迎使用卡路里管理系统 API',
        'version': '1.0.0',
        'endpoints': {
            'auth': '/api/auth/',
            'users': '/api/',
            'articles': '/api/articles/',
            'uploads': '/api/uploads/',
            'markdown': '/api/markdown/',
            'admin': '/admin/',
            'health': '/health/'
        }
    })
