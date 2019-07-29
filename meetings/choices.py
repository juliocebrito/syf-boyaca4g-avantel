""" TYPE_MEETINGS_CHOICES  """
DAILY = 'daily'
WEEKLY = 'weekly'
MONTHLY = 'monthly'
TYPE_MEETINGS_CHOICES = (
    ('', '---------'),
    (DAILY, 'daily'),
    (WEEKLY, 'weekly'),
    (MONTHLY, 'monthly'),
)

""" STATE_POINT_CHOICES  """
PENDING = 'pending'
EXECUTED = 'executed'
STATE_POINT_CHOICES = (
    (PENDING, 'pending'),
    (EXECUTED, 'executed'),
)