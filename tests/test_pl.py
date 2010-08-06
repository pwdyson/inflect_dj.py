
from nose.tools import eq_

from .. import inflect_dj

from ..inflect_dj import verbose_name_plural

def test_pl_verbose_name():

    @verbose_name_plural
    class category:
        class _meta:
            verbose_name = 'bacterium'
            pass
    eq_(category._meta.verbose_name_plural, 'bacteria')

#def test_pl_no_verbose_name():
#
#    @verbose_name_plural
#    class category:
#        class Meta:
#            pass
#    eq_(category._meta.verbose_name_plural, 'categories')

#def test_pl_no_meta():
#
#    @verbose_name_plural
#    class category:
#        pass
#    eq_(category._meta.verbose_name_plural, 'categories')
