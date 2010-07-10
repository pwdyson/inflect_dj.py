=============
inflect_dj.py
=============


NAME
====
inflect_dj.py - Generate plurals for use with Django.

VERSION
=======

This document describes version 0.1.0a of inflect_dj.py

INSTALLATION
============

``pip install inflect_dj``

or

``easy_install inflect_dj``


DESCRIPTION
===========

@pl
---

Decorator for class ``Meta`` inside of Django ``models.Model`` classes.


Decorating the ``Meta`` class with ``@pl`` will ensure that the plural form
of the model name will be rendered correctly.

``@pl`` will set ``verbose_name_plural`` to the correct plural of the model
name or the correct plural of ``verbose_name`` if it is provided.

It uses the module ``inflect.py`` to determine the correct pluralisation.

USAGE
-----

 1. Using ``@pl`` when specifying a ``verbose_name`` for the model::

        from django.db import models
        from inflect_dj import pl

        class mycategory(models.Model):
            [definition of the model]
            @pl
            class Meta:
                verbose_name = 'category'
                [rest of the Meta class definition]

   The ``@pl`` decorator will set ``Meta.verbose_name_plural`` to
   ``'categories'``, ensuring the plural will be displayed correctly.

 2. Using ``@pl`` without specifying ``verbose_name``::

        from django.db import models
        from inflect_dj import pl

        class category(models.Model):
            [definition of the model]
            @pl
            class Meta:
                [class Meta definition]


    The ``@pl`` decorator will ``set Meta.verbose_name_plural`` to
    ``'categories'``, as this is the plural of the class name.

Earlier versions of Python
--------------------------

If you are using a Python version earlier than 2.6 you cannot use
class decorators and must explicitly redefine ``Meta`` with a call to
``pl()``::

 from django.db import models
 from inflect_dj import pl

 class mycategory(models.Model):
     [definition of the model]
     class Meta:
         verbose_name = 'category'
         [rest of the Meta class definition]
     Meta = pl(Meta)



AUTHOR
======

Paul Dyson (pwdyson@yahoo.com)


COPYRIGHT
=========

    Copyright (C) 2010 Paul Dyson

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU Affero General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU Affero General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.

    This module can be downloaded at http://pypi.python.org/pypi/inflect_dj

    This module can be installed via ``easy_install inflect_dj``

    Repository available at http://github.com/pwdyson/inflect_dj.py

