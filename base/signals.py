from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.dispatch import receiver
import logging

logger = logging.getLogger(__name__)

# Log user login
@receiver(user_logged_in)
def log_user_login(sender, request, user, **kwargs):
    logger.info(f'User {user.username} logged in.')

# Log user logout
@receiver(user_logged_out)
def log_user_logout(sender, request, user, **kwargs):
    logger.info(f'User {user.username} logged out.')
