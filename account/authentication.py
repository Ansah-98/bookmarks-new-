from django.contrib.auth.models import User 



class EmailAuthBackend:


    def authenticate(self,password = None,username = None):
        try :
            user = User.objects.get(email = username)
            if user.check_password(password):
                return user
        except User.DoesNotExist:
            return None
    
    def get_user(self,user_id):
        try:
            user = User.objects.get(pk = user_id)
            if user :
                return user
        except User.DoesNotExist:
            return None