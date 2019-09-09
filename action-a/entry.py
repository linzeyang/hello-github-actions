import os

import django


print(f"Hello World! I'm {os.environ.get('MY_NAME')}")
print(f"Django version is {django.get_version()}")
