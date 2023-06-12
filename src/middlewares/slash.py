class RemoveSlashMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if 'admin' in request.path_info:
            return self.get_response(request)
        if len(request.path_info) > 1 and request.path_info[-1] == '/':
            request.path_info = request.path_info.rstrip('/')
        return self.get_response(request)
