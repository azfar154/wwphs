from sources import sources_gms,sources_hs
import json
r = json.dumps(sources_gms)
open('grover.json','w').write(str(r))
r = json.dumps(sources_hs)
open('wwphs.json','w').write(str(r))