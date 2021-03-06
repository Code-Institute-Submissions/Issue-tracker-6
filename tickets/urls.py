from django.conf.urls import url, include
from tickets.views import add_tickets , show_tickets, confrim, edit_tickets, delete_ticket, delete_comments, upvote_tickets, down_vote, edit_comments
urlpatterns = [
    url(r'^add_tickets/$',add_tickets, name='add_tickets'),
    url(r'^confrim/$',confrim, name='confrim'),
    url(r'^(?P<pk>\d+)/$',show_tickets, name='show_tickets'),
    url(r'^edit_tickets/(?P<id>\d+)$', edit_tickets, name="edit"),
    url(r'^delete/(?P<id>\d+)$', delete_ticket, name="delete"),
    url(r'^delete_comments/(?P<id>\d+)$', delete_comments, name="delete_comments"),
    url(r'^upvote_tickets/(?P<id>\d+)/$',upvote_tickets, name='upvote'),
    url(r'^down/(?P<id>\d+)/$',down_vote, name='dislike'),
    url(r'^edit_comment/(?P<id>\d+)/$',edit_comments, name='edit_comments'),
    ]