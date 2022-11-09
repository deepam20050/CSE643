# forward chaining rule engine
# trying out durable rules engine
#
from durable.lang import *

with ruleset('preferences'):
    @when_all((m.type >= 5))
    def mathct(e):
        e.assert_fact({ 'subject': 'take DL theory course'})

    @when_all(+m.subject)
    def output(c):
        print('Fact: {0}'.format(c.m.subject))


# assert_fact('interests', { 'area': 'human-like-interactions', 'type': 'notheory' })
assert_fact('preferences', {'type' : 5})




