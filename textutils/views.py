from django.http import HttpResponse
from django.shortcuts import render


def  index (request):
    return (render(request,'index.html'))
   

def analyse(request):
    # POST the text
    djtext = request.POST.get('text', 'default')
    removepunc=request.POST.get('removepunc','off')
    capitalise=request.POST.get('capitalise','off')
    newlineremover=request.POST.get('newlineremover','off')
    print(djtext)

    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analysed = ""
        for char in djtext:
            if char not in punctuations:
                analysed = analysed + char

        djtext=analysed

        params = {'purpose': 'Removed Punctuations', 'analysed_text': analysed}
        # return (render(request, 'analyse.html', params))
        
    if capitalise=='on':
        analysed=""
        for char  in djtext:
            analysed+=char.upper()
        djtext=analysed
        parms={'purpose':'Fully Capitalised ','analysed_text':analysed}
        # return (render(request,'analyse.html',parms))
    
    if newlineremover =='on':
        analysed=""
        for char  in djtext:
            
            if char !="\n" and char!="\r":
                analysed+=char
        djtext=analysed
        parms={'purpose':'new line removed ','analysed_text':analysed}
        # return (render( request ,'analyse.html',parms))
    
    if (removepunc!="off" and capitalise!="off" and newlineremover!="off"):
        return(HttpResponse(request,"<br><br><br><br> You haven`t selected any of the Choices ......."))



    return (render( request ,'analyse.html',params))


