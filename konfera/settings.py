from django.utils.translation import ugettext_lazy as _
from django.conf import settings


GOOGLE_ANALYTICS = getattr(settings, 'GOOGLE_ANALYTICS', None)  # just define analytics code: 'UA-XXXXXXXX-X'

TALK_DURATION = getattr(settings, 'TALK_DURATION',
                        (
                            (5, _('5 min')),
                            (30, _('30 min')),
                            (45, _('45 min')),
                        ))

"""LANDING PAGE is a composite of two keywords: <timewise>_<event>
<timewise> can be: latest or earliest
<event> can be (at the moment): conference or meetup
possible combinations: latest_conference (DEFAULT), latest_meetup, earliest_conference, earliest_meetup
"""
LANDING_PAGE = getattr(settings, 'LANDING_PAGE', 'latest_conference')
