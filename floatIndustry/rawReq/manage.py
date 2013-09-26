from django.shortcuts import render_to_response
from django.core.context_processors import csrf

from rawReq import models

def listDetails(request, list_id):
    context = {}
    rawMatList = []
    list_object = models.rawMatLists.objects.get(id=list_id)
    for rawMaterials in models.rawMat.objects.filter(rawMatList=list_object):
        querySet = models.rawMatAttrib.objects.filter(rawMatList=list_object, rawMat=rawMaterials)
        rawMatList.append([rawMaterials.name, querySet[0].quantity])
    context.update({'list_rawMatDetails': rawMatList})
    context.update({'list_listDetails': [list_object.listName, list_object.forColor, list_object.currentCapacity]})
    return render_to_response('listDetails.html', context)

def listAll(request):
    context = {}
    listList = []
    for listObj in models.rawMatLists.objects.all():
        listList.append([listObj.listName, listObj.forColor, listObj.currentCapacity, listObj.id])
    context.update({'lists': listList})
    return render_to_response('listAllLists.html', context)

def index(request):
    if request.method == 'POST':
        number_fields = int(request.POST['numberOfFields']) - 1
        name_of_list = request.POST['name_of_list']
        color_of_glass = request.POST['color_of_glass']
        current_production_capacity = request.POST['capacity']
        
        list_object = createList(name_of_list, color_of_glass, current_production_capacity)
        
        context = {}
        
        for x in xrange(number_fields):
            if request.POST['rawMatName'+str(x+1)] != '':
                raw_material_object = createRawMatObject(request.POST['rawMatName'+str(x+1)])
                addRawMatObjToList(raw_material_object[0], list_object[0])
                addQuantity(request.POST['quantity'+str(x+1)], raw_material_object[0], list_object[0])
        
        return render_to_response('createCurrentReq.html', context)
    else:
        context = {}
        context.update(csrf(request))
        return render_to_response('createRawMat.html', context)

def createList(name_of_list, color_of_glass, current_production_capacity):
    return models.rawMatLists.objects.get_or_create(listName=name_of_list, forColor=color_of_glass, currentCapacity=current_production_capacity)

def createRawMatObject(name):
    return models.rawMat.objects.get_or_create(name=name)

def addRawMatObjToList(rawMatObject, listObj):
    rawMatObject.rawMatList.add(listObj)

def addQuantity(quantity, rawMatObj, listObj):
    models.rawMatAttrib.objects.get_or_create(rawMatList=listObj, rawMat=rawMatObj, quantity=quantity)
