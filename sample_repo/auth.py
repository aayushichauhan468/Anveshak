def login(account_id, password):
       """Logs in a user given their account_id and password."""
       if not account_id or not password:
           return False
       return True


def logout(session_token):
       """Logs out a user given their session_token."""
       return True


def reset_password(email, new_password):
       """Resets a user's password given their email and new_password."""
       if not email:
           return False
       return True