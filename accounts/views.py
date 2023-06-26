from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from .models import Account
from .serializers import AccountSerializer
import csv
import io
from uuid import uuid4
from decimal import Decimal


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
        # print(column[0])
        obj, created = Account.objects.update_or_create(
            id=column[0],
            defaults={"name": column[1], "balance": Decimal(column[2])},
        )
        if created:
            obj.save()
        else:
            pass
            print(obj)
        accounts = Account.objects.all()
    return Response(data="importing completed!", status=201)


@api_view(["POST"])
def transfer(request):
    from_account = Account.objects.get(id=request.data["from"])
    to_account = Account.objects.get(id=request.data["to"])
    amount = Decimal(request.data["amount"])
    if from_account.balance < amount:
        return Response(
            {"error": "Insufficient balance"}, status=status.HTTP_402_PAYMENT_REQUIRED
        )
    print(from_account.balance)
    from_account.balance -= amount
    to_account.balance += amount
    from_account.save()
    to_account.save()
    print(from_account.balance)
    return Response(data="Transfer completed", status=204)
