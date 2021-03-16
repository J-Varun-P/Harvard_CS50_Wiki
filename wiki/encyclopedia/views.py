from django.http import HttpResponse
from django.shortcuts import render
import markdown2

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def title(request, title):
    s1 = util.get_entry(title)
    if s1 == None:
        return HttpResponse("Requested page not available")
    s2 = s1.splitlines()
    s3 = markdown2.markdown(s1)
    #return HttpResponse(f"{s3}")
    s4 = s3.splitlines()
    #return HttpResponse(f"{s3}")
    return render(request, "encyclopedia/title.html", {
    "content": s4
    })
    # return HttpResponse(f"Hello, {title}")
    return HttpResponse(f"{s3}")
    """
    l = len(s2)
    i = 0
    while i < l:
        #if len(s2[i]) > 0:
            #j = "<p>" + s2[i] + "</p>"
            #s2.append(j)
            #s2.remove(s2[i])
        #else:
        if len(s2[i]) == 0:
            s2.remove(s2[i])
            i = i - 1
            l = l - 1
        i = i + 1
    l = len(s2)
    i = 0
    while i < l:
        s3 = "<p>" + s2[0] + "</p>"
        s2.append(s3)
        s2.remove(s2[0])
        i = i + 1
    """
    return render(request, "encyclopedia/title.html", {
    "content": s2, "title": title
    })
    return HttpResponse(f"{s2}")
    return HttpResponse(f"{util.get_entry(title)}")
    return render(request, "encyclopedia/title.html", {
    "content": util.get_entry(title), "title": title
    })
