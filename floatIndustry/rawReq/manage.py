from django.shortcuts import render_to_response
from django.core.context_processors import csrf

from rawReq import models

def index(request):
    a1 = models.rawMatLists.objects.create(listName='listName1', forColor='colorname1')
    a1.save()
    b2 = models.rawMat.objects.create(name='name11')
    b2.save()
    b2.rawMatList.add(a1)
    #b1 = models.rawMat()
    #b1.name = 'silica'
    #b1.save()
    #a1 = models.rawMatLists(listNAme='qwqw', forColor='qsaqas')
    #a1.save()
    #b1 = models.rawMat(name='police')
    #b1.save()
    if request.method == 'POST':
        number_fields = int(request.POST['numberOfFields']) - 1
        name_of_list = request.POST['name_of_list']
        color_of_glass = request.POST['color_of_glass']
        
        list_object = models.rawMatLists().createList(list_name=name_of_list, color_name=color_of_glass)
        
        context = {}
        rawMatNamesList = []
        
        for x in xrange(number_fields):
            if request.POST['rawMatName'+str(x+1)] != '':
                tempList = [request.POST['rawMatName'+str(x+1)], 'quantity'+request.POST['rawMatName'+str(x+1)]]
                rawMatNamesList.append(tempList)
                raw_material_object = models.rawMat().createRawMat(request.POST['rawMatName'+str(x+1)])
                raw_material_object.addList(list_object)
        
        context.update({'rawMatNames': rawMatNamesList})
        return render_to_response('createCurrentReq.html', context)
    else:
        context = {}
        context.update(csrf(request))
        return render_to_response('createRawMat.html', context)
