from datetime import datetime
from django.shortcuts import render_to_response
from blog.models import BlogPost

def archive(request):
    post = BlogPost(title='mocktitle', body='mockbody',
        timestamp=datetime.now())
    return render_to_response('archive.html', {'posts': [post]})