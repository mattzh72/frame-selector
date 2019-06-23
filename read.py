import turicreate
from turicreate import SFrame

sf = turicreate.load_sframe('sample.sframe')

print(sf[0]['id'])