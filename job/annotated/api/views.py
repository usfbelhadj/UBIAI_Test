from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import AnnoSeri
from ..models import Annotated

@api_view(['GET', 'PUT',])
def annotate_list(request):
    new = ""
    qs = Annotated.objects.all()
    sni = Annotated.objects.get(pk=qs[0].id)
    print(sni)
    if request.method == 'GET':
        serializer = AnnoSeri(qs, many=True)
        
        return Response(serializer.data)
    elif  request.method == 'PUT':
        print(sni.annotations)
        print(request.data["annotations"])
        new = str(sni.annotations) + ', ' + str(request.data["annotations"])
        new.replace("\\", "")
        print(new)
        serializer = AnnoSeri(sni, {"annotations" : new})
        #print(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

