from django.http import HttpResponse
from django.shortcuts import render
import markdown2
from django import forms
from django.urls import reverse
from django.http import HttpResponseRedirect
from . import util
import random

class Title(forms.Form):
    title = forms.CharField()
    pagecontent = forms.CharField()

class Search(forms.Form):
    q = forms.CharField()

class Textarea(forms.Form):
    title = forms.CharField()
    pagecontent = forms.CharField(widget=forms.Textarea)

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def title(request, title):
        s1 = util.get_entry(title)
        if s1 == None:
            return render(request, "encyclopedia/pagenotfound.html")
        s2 = s1.splitlines()
        s3 = markdown2.markdown(s1)
        s4 = s3.splitlines()
        #form = Title(initial={'pagecontent': s1})
        form = Textarea(initial={'title': title, 'pagecontent': s1})
        #form = Title(initial={'pagecontent': s1})
        return render(request, "encyclopedia/title.html", {
        "content": s4, "title": title, "pagecontent": s2, "form": form
        })


def addpage(request):
    if request.method == "POST":
        print("Hello")
        form = Title(request.POST)
        abcd = form.is_valid()
        if form.is_valid():
            print("I'm Here, look at me!!!!!!!!!!!!!!!!")
            title = form.cleaned_data["title"]
            pagecontent = form.cleaned_data["pagecontent"]
            print(title, util.get_entry(title))
            if util.get_entry(title) != None:
                return render(request, "encyclopedia/newtitlefail.html")
            else:
                util.save_entry(title,pagecontent)
                return render(request, "encyclopedia/index.html", {
                    "entries": util.list_entries()
                })
    else:
        return render(request, "encyclopedia/addpage.html")


def randompage(request):
    entries = util.list_entries()
    n = random.randint(0, len(entries) - 1)
    print(f"{entries[n]}")
    s1 = util.get_entry(entries[n])
    s2 = s1.splitlines()
    s3 = markdown2.markdown(s1)
    s4 = s3.splitlines()
    return render(request, "encyclopedia/title.html", {
    "content": s4
    })
    return HttpResponse(f"{entries[n]}")


def editpage(request):
    formedit = Textarea(request.POST)
    if formedit.is_valid():
        title = formedit.cleaned_data["title"]
        pagecontent = formedit.cleaned_data["pagecontent"]
        return render(request, "encyclopedia/edittitle.html", {
        "form": formedit, "title": title, "pagecontent": pagecontent
        })
        return HttpResponse("I hope this works")


def search(request):
    formsearch = Search(request.POST)
    if formsearch.is_valid():
        q = formsearch.cleaned_data["q"]
    return HttpResponseRedirect(f"{q}")
