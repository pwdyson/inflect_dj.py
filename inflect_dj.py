
import re
import inflect


__ver_major__ = 0
__ver_minor__ = 1
__ver_patch__ = 0
__ver_sub__ = ""
__version__ = "%d.%d.%d%s" % (__ver_major__,__ver_minor__,
                              __ver_patch__,__ver_sub__)

p = inflect.engine()

def remove_camel_case(txt):
    '''
    change CamelCase into 'camel case'
    over ten times faster, and five times less readable, than the regex
    version in the django code
    '''
    if len(txt) > 1:
        ret = [txt[0]]
        for i in range(1, len(txt)-1):
            if txt[i].isupper() and (
                      txt[(i-1):i].islower() or
                      not txt[(i+1):(i+2)].isupper()):
                    ret.append(' ')
            ret.append(txt[i])
        ret.append(txt[-1])
        return (''.join(ret)).lower()
    else:
        return txt.lower()

def pl(cls):
    '''
    Automatically generate verbose_name_plural from 
    verbose_name (or the class name if verbose_name is not
    defined in the Meta class).

    Decorator for class Meta inside of django models.Model classes.

    USAGE:

    class mycategory(models.Model):
        @pl
        class Meta:
            verbose_name = 'category'
            [rest of the Meta class definition]

    The @pl decorator will set Meta.verbose_name_plural = 'categories'
    OR

    class category(models.Model):
        @pl
        class Meta:
            [class Meta definition]


    If Python version < 2.6:

    class mycategory(models.Model):
        class Meta:
            verbose_name = 'category'
            [rest of the Meta class definition]
        Meta = pl(Meta)

    '''
    try:
        cls.verbose_name_plural = p.pl(cls.verbose_name)
    except AttributeError:
        cls.verbose_name_plural = p.pl(remove_camel_case(cls.__name__))
    return cls

