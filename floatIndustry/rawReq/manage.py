from django.shortcuts import render_to_response
from django.core.context_processors import csrf

from rawReq import models

def index(request):
    if request.method == 'POST':
        number_fields = int(request.POST['numberOfFields']) - 1
        name_of_list = request.POST['name_of_list']
        color_of_glass = request.POST['color_of_glass']
        
        list_object = models.rawMatLists.objects.get_or_create(listName=name_of_list, forColor=color_of_glass)
        
        context = {}
        rawMatNamesList = []
        
        for x in xrange(number_fields):
            if request.POST['rawMatName'+str(x+1)] != '':
                tempList = [request.POST['rawMatName'+str(x+1)], 'quantity'+request.POST['quantity'+str(x+1)]]
                rawMatNamesList.append(tempList)
                raw_material_object = models.rawMat.objects.get_or_create(name=request.POST['rawMatName'+str(x+1)])
                raw_material_object[0].rawMatList.add(list_object[0])
        
        list1 = models.rawMatLists.objects.get(listName = name_of_list)
        components = models.rawMat.objects.filter(rawMatList = list1)
        print(list1.listName)
        print(list1.forColor)
        for component in components:
            print(component.name)

        context.update({'rawMatNames': rawMatNamesList})
        return render_to_response('createCurrentReq.html', context)
    else:
        context = {}
        context.update(csrf(request))
        return render_to_response('createRawMat.html', context)
