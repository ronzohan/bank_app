from lettuce import step
from nose.tools import assert_equal
from webtest import TestApp

@step(u'I visit the homepage')
def i_visit_the_homepage(step):
    assert True, 'This step must be implemented'