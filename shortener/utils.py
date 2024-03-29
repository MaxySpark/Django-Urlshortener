import random
import string
from django.conf import settings

SHORTCODE_MIN = getattr(settings, "SHORTCODE_MIN", 15)

def code_generator(size=SHORTCODE_MIN,chars=string.ascii_lowercase + string.digits) :
    return ''.join(random.choice(chars) for _ in range(size))

def create_shortcode(instance,size=SHORTCODE_MIN) :
    new_code = code_generator(size)
    print(instance)
    print(instance.__class__)
    print(instance.__class__.__name__)

    Klass = instance.__class__
    qs_exist = Klass.objects.filter(shortcode=new_code).exists()
    if qs_exist :
        return create_shortcode(size=size)
    return new_code 