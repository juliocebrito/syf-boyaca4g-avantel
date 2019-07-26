""" HARDWARE_STATE_CHOICES  """
WAREHOUSE = 'Warehouse'
SITE = 'Site'
FAILURE = 'Failure'
HARDWARE_STATE_CHOICES = (
    (WAREHOUSE, 'Warehouse'),
    (SITE, 'Site'),
    (FAILURE, 'Failure'),
)

""" UNITY_CHOICES  """
UND = 'und'
PCS = 'pcs'
MTS = 'mts'
UNITY_CHOICES = (
    ('', '---------'),
    (UND, 'und'),
    (PCS, 'pcs'),
    (MTS, 'mts'),
)
