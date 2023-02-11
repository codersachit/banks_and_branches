from graphene import relay, ObjectType
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from .models import Bank, Branch

class BankNode(DjangoObjectType):
    class Meta:
        model = Bank
        filter_fields = ['id', 'name']
        interfaces = (relay.Node, )


class BranchNode(DjangoObjectType):
    class Meta:
        model = Branch
        filter_fields = ['ifsc','branch','address','city','district','state']
        interfaces = (relay.Node, )


class Query(ObjectType):
    bank = relay.Node.Field(BankNode)
    all_banks = DjangoFilterConnectionField(BankNode)

    branch = relay.Node.Field(BranchNode)
    all_branches = DjangoFilterConnectionField(BranchNode)