# gdal-gbdx-task
A docker GBDX task for doing arbitrary gdal operations on data within DigitalGlobe's GBDX platform


Intended to use with gbdxtools like this:

```python
from gbdxtools import Interface
gbdx = Interface()

gdaltask = gbdx.Task('gdal-task-name')
gdaltask.inputs.filetypes = 'tif'
gdaltask.inputs.cmd = 'gdal_translate -i $input -o $output -flags --args'

workflow = gbdx.Workflow([gdaltask])
workflow.savedata(gdaltask.outputs.data, location='my_output_folder')
```