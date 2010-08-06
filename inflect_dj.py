
import re
import inflect


__ver_major__ = 0
__ver_minor__ = 2
__ver_patch__ = 0
__ver_sub__ = ""
__version__ = "%d.%d.%d%s" % (__ver_major__,__ver_minor__,
                              __ver_patch__,__ver_sub__)

p = inflect.engine()

def verbose_name_plural(cls):
    '''
    Automatically generate verbose_name_plural from 
    verbose_name (or the class name if verbose_name is not
    defined in the Meta class).

    Decorator for django models.Model classes.

    USAGE:

    @verbose_name_plural
    class mycategory(models.Model):
        class Meta:
            verbose_name = 'category'
            [rest of the Meta class definition]

    The @verbose_name_plural decorator will set Meta.verbose_name_plural = 'categories'
    OR

    @verbose_name_plural
    class category(models.Model):
        class Meta:
            [class Meta definition]


    If Python version < 2.6:

    class mycategory(models.Model):
        class Meta:
            verbose_name = 'category'
            [rest of the Meta class definition]
    mycategory = verbose_name_plural(mycategory)

    '''
    cls._meta.verbose_name_plural = p.plural(cls._meta.verbose_name)
    return cls

