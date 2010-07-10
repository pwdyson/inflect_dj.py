
import re
import inflect
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
            if txt[i].isupper() and (txt[(i-1):i].islower() or not txt[(i+1):(i+2)].isupper()):
                    ret.append(' ')
            ret.append(txt[i])
        ret.append(txt[-1])
        return (''.join(ret)).lower()
    else:
        return txt.lower()


def pl(cls):
    try:
        cls.verbose_name_plural = p.pl(cls.verbose_name)
    except AttributeError:
        cls.verbose_name_plural = p.pl(remove_camel_case(cls.__name__))
    return cls

