from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.home, name = 'blog'),
    path(r'sign_up', views.sign_up, name = "sign_up"),
    path(r'forgot', views.forgot, name = "forgot"),
    path(r'button', views.button, name = "button"),
    path(r'save_data', views.save_data, name = "save_data"),
    path(r'login', views.login, name = "login"),
    path(r'send_otp', views.send_otp, name = 'send_otp'),
    path(r'check_otp', views.check_otp, name = 'check_otp'),
    path(r'first_page', views.first_page, name = 'first_page'),
    path(r'profile', views.profile, name = 'profile'),
    path(r'update_data', views.update_data, name = 'update_data'),
    path(r'make_a_post', views.make_a_post, name = 'make_a_post'),
    path(r'hello', views.hello, name = 'hello'),
    path(r'hello_hello', views.hello_hello, name = 'hello_hello'),
    path(r'my_posts', views.my_posts, name = 'my_posts'),
    path(r'remove_post', views.remove_post, name = 'remove_post'),
    path(r'save_comment', views.save_comment, name = 'save_comment'),
    path(r'deactivate', views.deactivate, name = 'deactivate'),
    path(r'delete_account', views.delete_account, name = 'delete_account'),
    path(r'admin_login', views.admin_login, name = 'admin_login'),
    path(r'admin_requests_otp', views.admin_requests_otp, name = 'admin_requests_otp'),
    path(r'Admin_OTP_check', views.Admin_OTP_check, name = 'Admin_OTP_check'),
    path(r'Admin_welcome', views.Admin_welcome, name = 'Admin_welcome'),
    path(r'send_Admin_OTP', views.send_Admin_OTP, name = 'send_Admin_OTP'),
    path(r'admin_login_', views.admin_login_, name = 'admin_login_'),
    path(r'admin_post', views.admin_post, name = 'admin_post'),
    path(r'admin_removes_post', views.admin_removes_post, name = 'admin_removes_post'),
    path(r'ban_person', views.ban_person, name = 'ban_person'),
    path(r'remove_person', views.remove_person, name = 'remove_person'),
    path(r'send_mail_page', views.send_mail_page, name = 'send_mail_page'),
    path(r'send_email_to_person', views.send_email_to_person, name = 'send_email_to_person'),
    path(r'allow_person', views.allow_person, name = 'allow_person'),
    path(r'friends', views.friends, name = 'friends'),
    path(r'profile_of_person', views.profile_of_person, name = 'profile_of_person'),
    path(r'group_chat', views.group_chat, name = 'group_chat'),
    path(r'save_group_chat', views.save_group_chat, name = 'save_group_chat'),
    path(r'box_chat', views.box_chat, name = 'box_chat'),
    path(r'box_chat_save', views.box_chat_save, name = 'box_chat_save'),
    path(r'notify', views.notify, name = 'notify'),
    path(r'remove_notification', views.remove_notification, name = 'remove_notification'),
    path(r'notify_box_chat', views.notify_box_chat, name = 'notify_box_chat'),
    path(r'remove_all', views.remove_all, name = 'remove_all')
]
