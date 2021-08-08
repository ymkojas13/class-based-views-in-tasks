from django.contrib.auth.signals import user_logged_in, user_logged_out, user_login_failed
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import pre_init, pre_save, pre_delete, post_init, post_save, post_delete, pre_migrate, post_migrate
from django.core.signals import request_started, request_finished, got_request_exception
from django.db.backends.signals import connection_created

@receiver(user_logged_in, sender=User)
def login_su(sender, request, user, **kwargs):
 print("login successfully")
#user_logged_in.connect(login_su, sender=User)

@receiver(user_logged_out, sender=User)
def log_out(sender, request, user, **kwargs):
 print("logout success")
# user_logged_out.connect(log_out, sender=User)

@receiver(user_login_failed)
def login_failed(sender, credentials, request, **kwargs):
    print("login failed")

@receiver(pre_save, sender=User)
def at_beginning_save(sender, instance, **kwargs):
    print("saved at ending")

@receiver(post_save, sender=User)
def at_ending_save(sender, instance, created, **kwargs):
 if created:
  print("created")
 else:
  print("post siganl")

@receiver(pre_delete, sender=User)
def at_beginning_delete(sender, instance, **kwargs):
 print("-----------------------------------------")
 print("Pre Delete Signal......")
 print('Sender:', sender)
 print('Instance:', instance)
 print(f'Kwargs: {kwargs}')
# pre_delete.connect(at_beginning_delete, sender=User)

@receiver(post_delete, sender=User)
def at_ending_delete(sender, instance, **kwargs):
 print("post delete")

@receiver(pre_init, sender=User)
def at_beginning_init(sender, *args, **kwargs):
    print("pre signal")

@receiver(post_init, sender=User)
def at_ending_init(sender, *args, **kwargs):
 print("post init")

@receiver(request_started)
def at_beginning_request(sender, environ, **kwargs):
 print("request started")

@receiver(request_finished)
def at_ending_request(sender, **kwargs):
 print("request finished")

@receiver(got_request_exception)
def at_req_exception(sender, request, **kwargs):
 print("request exception")

@receiver(pre_migrate)
def before_install_app(sender, app_config, verbosity, interactive, using, plan, apps, **kwargs):
 print("pre migration")

@receiver(post_migrate)
def at_end_migrate_flush(sender, app_config, verbosity, interactive, using, plan, apps, **kwargs):
 print("post migration")

@receiver(connection_created)
def conn_db(sender, connection, **kwargs):
    print("connection created")