from django.shortcuts import render_to_response
from django.core.context_processors import csrf

from rawReq import models

def index(request):
    #a1 = models.rawMatLists.objects.create(listNAme='listName1', forColor='colorname1')
    #a1.save()
    #b2 = models.rawMAt.objects.create(name='name11')
    #b2.save()
    #b2.rawMatList.add(a1)
    #b1 = models.rawMat()
    #b1.name = 'silica'
    #b1.save()
    #a1 = models.rawMatLists(listNAme='qwqw', forColor='qsaqas')
    #a1.save()
    #b1 = models.rawMat(name='police')
    #b1.save()
    if request.method == 'POST':
        number_fields = int(request.POST['numberOfFields']) - 1
        context = {}
        rawMatNamesList = []
        for x in xrange(number_fields):
            if request.POST['rawMatName'+str(x+1)] != '':
                tempList = [request.POST['rawMatName'+str(x+1)], 'quantity'+request.POST['rawMatName'+str(x+1)]]
                rawMatNamesList.append(tempList)
        context.update({'rawMatNames': rawMatNamesList})
        return render_to_response('createCurrentReq.html', context)
    else:
        context = {}
        context.update(csrf(request))
        return render_to_response('createRawMat.html', context)
