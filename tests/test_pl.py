
from nose.tools import eq_

from inflect_dj import pl

def test_pl_no_verbose_name():

    @pl
    class category:
        class Meta:
            pass
    eq_(category.Meta.verbose_name_plural, 'categories')

def test_pl_verbose_name():

    @pl
    class category:
        class Meta:
            verbose_name = 'bacterium'
            pass
    eq_(category.Meta.verbose_name_plural, 'bacteria')

def test_pl_no_meta():

    @pl
    class category:
        pass
    eq_(category.Meta.verbose_name_plural, 'categories')
