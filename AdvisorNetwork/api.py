from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from Advisors.serializers import AdvisorsSerializer


# Register API
class AddAdvisor(generics.GenericAPIView):
    serializer_class = AdvisorsSerializer
    permission_classes = (AllowAny,)

    @csrf_exempt
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        advisor = serializer.save()
        return Response({
            "user": AdvisorsSerializer(advisor, context=self.get_serializer_context()).data,
            "message": "Advisor Created Successfully.",
        })
