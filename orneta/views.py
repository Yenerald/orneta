from django.shortcuts import render
def post_list(request):
    return render(request, 'orneta/post_list.html', {})
