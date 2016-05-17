# gdal-gbdx-task
A docker GBDX task for doing arbitrary gdal operations on data within DigitalGlobe's GBDX platform


Intended to use with gbdxtools like this:

```python
from gbdxtools import Interface
gbdx = Interface()

gdaltask = gbdx.Task('gdal-task-name')
gdaltask.inputs.filetypes = 'tif'
gdaltask.inputs.command = 'gdal_translate -i $input -o $output -flags --args'
gdaltask.inputs.data = 's3://path/to/my/data'

workflow = gbdx.Workflow([gdaltask])
workflow.savedata(gdaltask.outputs.data, location='my_output_folder')
```


Current Substitutions:

* $input - absolute input path to a file found
* $output - absolute output path to be written (filename is the same as input filename)

More Substitutions we could use:

* $output_directory
* $output_filename
* $output_file_no_extension
* $output_file_extension
