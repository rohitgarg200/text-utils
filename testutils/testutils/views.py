from django.http import HttpResponse
from django.shortcuts import render


# def index(request):
#    return HttpResponse("hello about")
def index(request):
    return render(request, 'index.html')

def analyze(request):
    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    fullcap = request.POST.get('fullcap', 'off')
    newlineremover = request.POST.get('newlineremover','off')
    charcounter = request.POST.get('charcounter','off')
    if removepunc == "on":
        punctuations = '''[][!"#$%&'()*+,./:;<=>?@\^_`|{}~-]'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed+char
        params = {'purpose' : 'Removed Punctuations' , 'analyzed_text' : analyzed }
        djtext = analyzed
    if fullcap == "on":
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'UPPERCASE', 'analyzed_text': analyzed}
        djtext = analyzed
    if newlineremover == "on":
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char

        params = {'purpose': 'NewLineRemover1', 'analyzed_text': analyzed}
        djtext = analyzed
    if charcounter == "on":
        analyzed = 0
        for char in djtext:
            if ( char >='a'and char <= 'z' ) or ( char >= 'A' and char <= 'Z' ):
                analyzed = analyzed+1
        y = "your number of characters are - "
        analyzed = y + str(analyzed)
        params = {'purpose': 'Number of char are ', 'analyzed_text': analyzed}
    if(removepunc != "on" and charcounter != "on" and newlineremover != "on" and fullcap != "on"):
        error = "error"
        params = {'purpose': 'select atleast one function','analyzed_text': error}
    return render(request, 'analyze.html', params)