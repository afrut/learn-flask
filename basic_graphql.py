import graphene
from flask import Flask, request
from flask_graphql import GraphQLView

app = Flask(__name__)


class Query(graphene.ObjectType):
    hello = graphene.String()
    ask = graphene.String(name=graphene.String(default_value="anyone"))
    add = graphene.Int(number=graphene.Int(required=True))

    def resolve_hello(root, info):
        return "Hello"

    def resolve_ask(root, info, name):
        return f"Asking {name}"

    def resolve_add(root, info, number):
        return number + 1


schema = graphene.Schema(query=Query)
app.add_url_rule("/graphql", view_func=GraphQLView.as_view("graphql", schema=schema, graphiql=True))
