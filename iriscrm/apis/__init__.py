
# flake8: noqa

# Import all APIs into this package.
# If you have many APIs here with many many models used in each API this may
# raise a `RecursionError`.
# In order to avoid this, import only the API that you directly need like:
#
#   from iriscrm.api.e_signature_api import ESignatureApi
#
# or import this package, but before doing it, use:
#
#   import sys
#   sys.setrecursionlimit(n)

# Import APIs into API package:
from iriscrm.api.e_signature_api import ESignatureApi
from iriscrm.api.leads_api import LeadsApi
