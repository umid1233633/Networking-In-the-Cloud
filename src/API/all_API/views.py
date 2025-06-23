from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import *
from models_for_API import *
from API.permissions import *

class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializers
    queryset = Product.objects.all()
    permission_classes = [Is_Admin]

class UserGetViewSet(viewsets.ModelViewSet):
    serializer_class = UserListSerializer
    permission_classes = [Is_Admin]
    def get_queryset(self):
        return CustomUser.objects.filter(id=self.request.user.id)
class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    # permission_classes = [Is_Admin]


class InvoiceViewSet(viewsets.ModelViewSet):
    serializer_class = InvoiceSerializer
    queryset = Invoice.objects.all()
    # permission_classes = [Is_Admin]


class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
    # permission_classes = [Is_Admin]


class InfoViewSet(viewsets.ModelViewSet):
    serializer_class = InfoSerializer
    queryset = Info.objects.all()
    # permission_classes = [Is_Admin]



class CollaborationViewSet(viewsets.ModelViewSet):
    serializer_class = CollaborationSerializer
    queryset = Collaboration.objects.all()
    # permission_classes = [Is_Admin]


# class UserViewSet(viewsets.ModelViewSet):
#     serializer_class = UserSerializer
#     queryset = CustomUser.objects.all()
#     permission_classes = [Is_Admin]