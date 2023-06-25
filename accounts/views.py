from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Account
from .serializers import AccountSerializer
import csv


class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer


@api_view(["POST"])
def import_accounts(request):
    csv_file = request.FILES["file"]
    data_set = csv_file.read().decode("UTF-8")
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter=",", quotechar="|"):
        _, created = Account.objects.update_or_create(
            id=column[0],
            balance=column[1],
        )
    return Response(status=201)


@api_view(["POST"])
def transfer(request):
    from_account = Account.objects.get(id=request.data["from"])
    to_account = Account.objects.get(id=request.data["to"])
    amount = Decimal(request.data["amount"])
    if from_account.balance < amount:
        return Response({"error": "Insufficient balance"}, status=400)
    from_account.balance -= amount
    to_account.balance += amount
    from_account.save()
    to_account.save()
    return Response(status=204)
