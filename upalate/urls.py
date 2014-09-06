

""""
urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^account/login/$', views.user_login, name='login'),
    url(r'^account/register/$', views.user_register, name='register'),
    url(r'^account/logout/$', views.user_logout, name='logout'),
    url(r'^transaction/(?P<transaction_id>\d+)/$', views.detail, name='detail'),
    url(r'^category/(?P<category_id>\d+)/$', views.category, name='category'),
)

"""