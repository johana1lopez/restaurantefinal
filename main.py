import pandas as pd
from data.platos import platosPopulares
from data.creartabla import crearTabla

tablaPlatos=pd.DataFrame(platosPopulares)
print(tablaPlatos)

crearTabla(tablaPlatos,"tablaplatospopulares")