from django.conf.urls.defaults import *
from views import *

urlpatterns = patterns(
    '',
    (r'^version$', version),
    (r'^plots$', route(GET=get_plot_list, POST=create_plot_optional_tree)),
    (r'^plots/(?P<plot_id>\d+)/tree/photo/(?P<photo_id>\d+)', get_tree_image),
    (r'^locations/(?P<lat>-{0,1}\d+(\.\d+){0,1}),(?P<lon>-{0,1}\d+(\.\d+){0,1})/plots', plots_closest_to_point),

    (r'^addresses/(?P<address>.+)', geocode_address),

    (r'^login/reset_password$', reset_password),
    (r'^login$', verify_auth),

    (r'^user/$', route(POST=register)),
    (r'^user/(?P<user_id>\d+)/photo/(?P<title>.+)$', add_profile_photo),  
    (r'^user/(?P<user_id>\d+)/password$', update_password),  
    (r'^user/(?P<user_id>\d+)/edits$', recent_edits),  

    (r'^tiles',  get_trees_in_tile),
)