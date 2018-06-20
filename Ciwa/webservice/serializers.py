from flask_restplus import fields
from Ciwa.webservice.api import api

entity = api.model('Resource', {
    'name': fields.String(description="Name of the entity"),
    'type': fields.String(description="Type of the entity"),
    'value': fields.String(description="Value of the entity")
})

conversation_content = api.model('Conversation', {
    'conversation_id': fields.String(description="Conversation identification code"),
    'count': fields.Integer(description="Count of conversations under of conversation_id"),
    'request_id': fields.String(description="Request ID"),
    'client_txt': fields.String(description="Text message give by the user"),
    'response_id': fields.String(description="Response ID"),
    'response_txt': fields.String(description="Text message given as the response"),
})

conversation = api.inherit('Conversation Model', conversation_content, {
    'entities_identified': fields.List(fields.Nested(entity))
})

#
# blog_post = api.model('Blog post', {
#     'id': fields.Integer(readOnly=True, description='The unique identifier of a blog post'),
#     'title': fields.String(required=True, description='Article title'),
#     'body': fields.String(required=True, description='Article content'),
#     'pub_date': fields.DateTime,
#     'category_id': fields.Integer(attribute='category.id'),
#     'category': fields.String(attribute='category.id'),
# })
#
# pagination = api.model('A page of results', {
#     'page': fields.Integer(description='Number of this page of results'),
#     'pages': fields.Integer(description='Total number of pages of results'),
#     'per_page': fields.Integer(description='Number of items per page of results'),
#     'total': fields.Integer(description='Total number of results'),
# })
#
# page_of_blog_posts = api.inherit('Page of blog posts', pagination, {
#     'items': fields.List(fields.Nested(blog_post))
# })
#
# category = api.model('Blog category', {
#     'id': fields.Integer(readOnly=True, description='The unique identifier of a blog category'),
#     'name': fields.String(required=True, description='Category name'),
# })
#
# category_with_posts = api.inherit('Blog category with posts', category, {
#     'posts': fields.List(fields.Nested(blog_post))
# })
