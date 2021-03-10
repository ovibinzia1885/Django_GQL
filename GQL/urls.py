
from django.contrib import admin
from django.urls import path
from graphene_django.views import GraphQLView
from GQL.schema import schema
from graphql_jwt.decorators import jwt_cookie

urlpatterns = [
    path('admin/', admin.site.urls),
    path('graphql/',jwt_cookie( GraphQLView.as_view(graphiql=True))),
]
