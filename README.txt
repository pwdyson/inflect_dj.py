=============
inflect_dj.py
=============


NAME
====
inflect_dj.py - Generate plurals for use with Django.

VERSION
=======

This document describes version 0.2.0 of inflect_dj.py

INSTALLATION
============

``pip install inflect_dj``

or

``easy_install inflect_dj``


DESCRIPTION
===========

@verbose_name_plural
---

Decorator for the Django ``models.Model`` classes.


Decorating a child class of ``model.Model`` with ``@verbose_name_plural`` will ensure that
the plural form of the model name will be rendered correctly.

It uses the module ``inflect.py`` to determine the correct pluralisation.

USAGE
-----

 1. Using ``@verbose_name_plural`` when specifying a ``verbose_name`` for the model::

        from django.db import models
        from inflect_dj import verbose_name_plural

        @verbose_name_plural
        class mycategory(models.Model):
            [definition of the model]
            class Meta:
                verbose_name = 'category'
                [rest of the Meta class definition]

   The plural will be displayed correctly as ``categories``.

 2. Using ``@verbose_name_plural`` without specifying ``verbose_name``::

        from django.db import models
        from inflect_dj import verbose_name_plural

        @verbose_name_plural
        class category(models.Model):
            [definition of the model]
            class Meta:
                [class Meta definition]


   The plural will be displayed correctly as ``categories``, as this
   is the plural of the class name.

Earlier versions of Python
--------------------------

If you are using a Python version earlier than 2.6 you cannot use
class decorators and must explicitly redefine the class with a call to
``verbose_name_plural()``::

 from django.db import models
 from inflect_dj import verbose_name_plural

 class mycategory(models.Model):
     [definition of the model]
     class Meta:
         verbose_name = 'category'
         [rest of the Meta class definition]
 mycategory = verbose_name_plural(mycategory)



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

