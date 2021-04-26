"""
Serialization Operators
=======================
"""
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs, _modify_output_spec_with_one_type
from ansys.dpf.core.operators.specification import PinSpecification, Specification

"""Operators from Ans.Dpf.Native.dll plugin, from "serialization" category
"""

#internal name: serializer
#scripting name: serializer
class _InputsSerializer(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(serializer._spec().inputs, op)
        self.file_path = Input(serializer._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.file_path)
        self.any_input1 = Input(serializer._spec().input_pin(1), 1, op, 0) 
        self._inputs.append(self.any_input1)
        self.any_input2 = Input(serializer._spec().input_pin(2), 2, op, 1) 
        self._inputs.append(self.any_input2)

class _OutputsSerializer(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(serializer._spec().outputs, op)
        self.file_path = Output(serializer._spec().output_pin(0), 0, op) 
        self._outputs.append(self.file_path)

class serializer(Operator):
    """Take any input and serialize them in a file.

      available inputs:
         file_path (str)
         any_input1 (Any)
         any_input2 (Any)

      available outputs:
         file_path (str)

      Examples
      --------
      >>> op = operators.serialization.serializer()

    """
    def __init__(self, file_path=None, any_input1=None, any_input2=None, config=None, server=None):
        super().__init__(name="serializer", config = config, server = server)
        self.inputs = _InputsSerializer(self)
        self.outputs = _OutputsSerializer(self)
        if file_path !=None:
            self.inputs.file_path.connect(file_path)
        if any_input1 !=None:
            self.inputs.any_input1.connect(any_input1)
        if any_input2 !=None:
            self.inputs.any_input2.connect(any_input2)

    @staticmethod
    def _spec():
        spec = Specification(description="""Take any input and serialize them in a file.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "file_path", type_names=["string"], optional=False, document=""""""), 
                                 1 : PinSpecification(name = "any_input", type_names=["any"], optional=False, document="""any input"""), 
                                 2 : PinSpecification(name = "any_input", type_names=["any"], optional=False, document="""any input""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "file_path", type_names=["string"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "serializer")

#internal name: mechanical_csv_to_field
#scripting name: mechanical_csv_to_field
class _InputsMechanicalCsvToField(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(mechanical_csv_to_field._spec().inputs, op)
        self.mesh = Input(mechanical_csv_to_field._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.mesh)
        self.data_sources = Input(mechanical_csv_to_field._spec().input_pin(4), 4, op, -1) 
        self._inputs.append(self.data_sources)
        self.requested_location = Input(mechanical_csv_to_field._spec().input_pin(9), 9, op, -1) 
        self._inputs.append(self.requested_location)

class _OutputsMechanicalCsvToField(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(mechanical_csv_to_field._spec().outputs, op)
        self.field = Output(mechanical_csv_to_field._spec().output_pin(0), 0, op) 
        self._outputs.append(self.field)

class mechanical_csv_to_field(Operator):
    """Reads mechanical exported csv file

      available inputs:
         unit ()
         mesh (MeshedRegion) (optional)
         data_sources (DataSources)
         requested_location (str, FieldDefinition)

      available outputs:
         field (Field)

      Examples
      --------
      >>> op = operators.serialization.mechanical_csv_to_field()

    """
    def __init__(self, mesh=None, data_sources=None, requested_location=None, config=None, server=None):
        super().__init__(name="mechanical_csv_to_field", config = config, server = server)
        self.inputs = _InputsMechanicalCsvToField(self)
        self.outputs = _OutputsMechanicalCsvToField(self)
        if mesh !=None:
            self.inputs.mesh.connect(mesh)
        if data_sources !=None:
            self.inputs.data_sources.connect(data_sources)
        if requested_location !=None:
            self.inputs.requested_location.connect(requested_location)

    @staticmethod
    def _spec():
        spec = Specification(description="""Reads mechanical exported csv file""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "unit", type_names=[], optional=False, document=""""""), 
                                 1 : PinSpecification(name = "mesh", type_names=["abstract_meshed_region"], optional=True, document=""""""), 
                                 4 : PinSpecification(name = "data_sources", type_names=["data_sources"], optional=False, document=""""""), 
                                 9 : PinSpecification(name = "requested_location", type_names=["string","field_definition"], optional=False, document="""""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "field", type_names=["field"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "mechanical_csv_to_field")

#internal name: field_to_csv
#scripting name: field_to_csv
class _InputsFieldToCsv(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(field_to_csv._spec().inputs, op)
        self.field_or_fields_container = Input(field_to_csv._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.field_or_fields_container)
        self.file_path = Input(field_to_csv._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.file_path)
        self.storage_type = Input(field_to_csv._spec().input_pin(2), 2, op, -1) 
        self._inputs.append(self.storage_type)

class _OutputsFieldToCsv(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(field_to_csv._spec().outputs, op)
        pass 

class field_to_csv(Operator):
    """Exports a field or a fields container into a csv file

      available inputs:
         field_or_fields_container (FieldsContainer, Field)
         file_path (str)
         storage_type (int) (optional)

      available outputs:


      Examples
      --------
      >>> op = operators.serialization.field_to_csv()

    """
    def __init__(self, field_or_fields_container=None, file_path=None, storage_type=None, config=None, server=None):
        super().__init__(name="field_to_csv", config = config, server = server)
        self.inputs = _InputsFieldToCsv(self)
        self.outputs = _OutputsFieldToCsv(self)
        if field_or_fields_container !=None:
            self.inputs.field_or_fields_container.connect(field_or_fields_container)
        if file_path !=None:
            self.inputs.file_path.connect(file_path)
        if storage_type !=None:
            self.inputs.storage_type.connect(storage_type)

    @staticmethod
    def _spec():
        spec = Specification(description="""Exports a field or a fields container into a csv file""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "field_or_fields_container", type_names=["fields_container","field"], optional=False, document="""field_or_fields_container"""), 
                                 1 : PinSpecification(name = "file_path", type_names=["string"], optional=False, document=""""""), 
                                 2 : PinSpecification(name = "storage_type", type_names=["int32"], optional=True, document="""storage type : if matrices (without any particularity) are included in the fields container, the storage format can be chosen. 0 : flat/line format, 1 : ranked format. If 1 is chosen, the csv can not be read by "csv to field" operator anymore. Default : 0.""")},
                             map_output_pin_spec={
})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "field_to_csv")

#internal name: deserializer
#scripting name: deserializer
class _InputsDeserializer(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(deserializer._spec().inputs, op)
        self.file_path = Input(deserializer._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.file_path)

class _OutputsDeserializer(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(deserializer._spec().outputs, op)
        pass 

class deserializer(Operator):
    """Takes a file generated by the serializer and deserializes it into DPF's entities.

      available inputs:
         file_path (str)

      available outputs:
         any_output1 ()
         any_output2 ()

      Examples
      --------
      >>> op = operators.serialization.deserializer()

    """
    def __init__(self, file_path=None, config=None, server=None):
        super().__init__(name="deserializer", config = config, server = server)
        self.inputs = _InputsDeserializer(self)
        self.outputs = _OutputsDeserializer(self)
        if file_path !=None:
            self.inputs.file_path.connect(file_path)

    @staticmethod
    def _spec():
        spec = Specification(description="""Takes a file generated by the serializer and deserializes it into DPF's entities.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "file_path", type_names=["string"], optional=False, document="""file path""")},
                             map_output_pin_spec={
                                 1 : PinSpecification(name = "any_output", type_names=[], optional=False, document="""number and types of outputs corresponding of the inputs used in the serialization"""), 
                                 2 : PinSpecification(name = "any_output", type_names=[], optional=False, document="""number and types of outputs corresponding of the inputs used in the serialization""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "deserializer")

#internal name: csv_to_field
#scripting name: csv_to_field
class _InputsCsvToField(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(csv_to_field._spec().inputs, op)
        self.time_scoping = Input(csv_to_field._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.time_scoping)
        self.data_sources = Input(csv_to_field._spec().input_pin(4), 4, op, -1) 
        self._inputs.append(self.data_sources)

class _OutputsCsvToField(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(csv_to_field._spec().outputs, op)
        self.fields_container = Output(csv_to_field._spec().output_pin(0), 0, op) 
        self._outputs.append(self.fields_container)

class csv_to_field(Operator):
    """transform csv file to a field or fields container

      available inputs:
         time_scoping (Scoping) (optional)
         data_sources (DataSources)

      available outputs:
         fields_container (FieldsContainer)

      Examples
      --------
      >>> op = operators.serialization.csv_to_field()

    """
    def __init__(self, time_scoping=None, data_sources=None, config=None, server=None):
        super().__init__(name="csv_to_field", config = config, server = server)
        self.inputs = _InputsCsvToField(self)
        self.outputs = _OutputsCsvToField(self)
        if time_scoping !=None:
            self.inputs.time_scoping.connect(time_scoping)
        if data_sources !=None:
            self.inputs.data_sources.connect(data_sources)

    @staticmethod
    def _spec():
        spec = Specification(description="""transform csv file to a field or fields container""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "time_scoping", type_names=["scoping"], optional=True, document=""""""), 
                                 4 : PinSpecification(name = "data_sources", type_names=["data_sources"], optional=False, document="""data sources containing a file with csv extension""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "csv_to_field")

"""
Serialization Operators
=======================
"""
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs, _modify_output_spec_with_one_type
from ansys.dpf.core.operators.specification import PinSpecification, Specification

"""Operators from meshOperatorsCore.dll plugin, from "serialization" category
"""

#internal name: vtk_export
#scripting name: vtk_export
class _InputsVtkExport(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(vtk_export._spec().inputs, op)
        self.file_path = Input(vtk_export._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.file_path)
        self.mesh = Input(vtk_export._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self.mesh)
        self.fields1 = Input(vtk_export._spec().input_pin(2), 2, op, 0) 
        self._inputs.append(self.fields1)
        self.fields2 = Input(vtk_export._spec().input_pin(3), 3, op, 1) 
        self._inputs.append(self.fields2)

class _OutputsVtkExport(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(vtk_export._spec().outputs, op)
        pass 

class vtk_export(Operator):
    """Write the input field and fields container into a given vtk path

      available inputs:
         file_path (str)
         mesh (MeshedRegion) (optional)
         fields1 (FieldsContainer, Field)
         fields2 (FieldsContainer, Field)

      available outputs:


      Examples
      --------
      >>> op = operators.serialization.vtk_export()

    """
    def __init__(self, file_path=None, mesh=None, fields1=None, fields2=None, config=None, server=None):
        super().__init__(name="vtk_export", config = config, server = server)
        self.inputs = _InputsVtkExport(self)
        self.outputs = _OutputsVtkExport(self)
        if file_path !=None:
            self.inputs.file_path.connect(file_path)
        if mesh !=None:
            self.inputs.mesh.connect(mesh)
        if fields1 !=None:
            self.inputs.fields1.connect(fields1)
        if fields2 !=None:
            self.inputs.fields2.connect(fields2)

    @staticmethod
    def _spec():
        spec = Specification(description="""Write the input field and fields container into a given vtk path""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "file_path", type_names=["string"], optional=False, document="""path with vtk extension were the export occurs"""), 
                                 1 : PinSpecification(name = "mesh", type_names=["abstract_meshed_region"], optional=True, document="""necessary if the first field or fields container don't have a mesh in their support"""), 
                                 2 : PinSpecification(name = "fields", type_names=["fields_container","field"], optional=False, document="""fields exported"""), 
                                 3 : PinSpecification(name = "fields", type_names=["fields_container","field"], optional=False, document="""fields exported""")},
                             map_output_pin_spec={
})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "vtk_export")

#internal name: vtk::vtk::FieldProvider
#scripting name: vtk_to_fields
class _InputsVtkToFields(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(vtk_to_fields._spec().inputs, op)
        self.field_name = Input(vtk_to_fields._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.field_name)
        self.streams = Input(vtk_to_fields._spec().input_pin(3), 3, op, -1) 
        self._inputs.append(self.streams)
        self.data_sources = Input(vtk_to_fields._spec().input_pin(4), 4, op, -1) 
        self._inputs.append(self.data_sources)

class _OutputsVtkToFields(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(vtk_to_fields._spec().outputs, op)
        self.fields_container = Output(vtk_to_fields._spec().output_pin(0), 0, op) 
        self._outputs.append(self.fields_container)

class vtk_to_fields(Operator):
    """Write a field based on a vtk file.

      available inputs:
         field_name (str) (optional)
         streams (StreamsContainer) (optional)
         data_sources (DataSources)

      available outputs:
         fields_container (FieldsContainer)

      Examples
      --------
      >>> op = operators.serialization.vtk_to_fields()

    """
    def __init__(self, field_name=None, streams=None, data_sources=None, config=None, server=None):
        super().__init__(name="vtk::vtk::FieldProvider", config = config, server = server)
        self.inputs = _InputsVtkToFields(self)
        self.outputs = _OutputsVtkToFields(self)
        if field_name !=None:
            self.inputs.field_name.connect(field_name)
        if streams !=None:
            self.inputs.streams.connect(streams)
        if data_sources !=None:
            self.inputs.data_sources.connect(data_sources)

    @staticmethod
    def _spec():
        spec = Specification(description="""Write a field based on a vtk file.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "field_name", type_names=["string"], optional=True, document="""name of the field in the vtk file"""), 
                                 3 : PinSpecification(name = "streams", type_names=["streams_container"], optional=True, document=""""""), 
                                 4 : PinSpecification(name = "data_sources", type_names=["data_sources"], optional=False, document="""""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""fields_container""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "vtk::vtk::FieldProvider")

#internal name: vtk::migrate_file
#scripting name: migrate_file_to_vtk
class _InputsMigrateFileToVtk(_Inputs):
    def __init__(self, op: Operator):
        super().__init__(migrate_file_to_vtk._spec().inputs, op)
        self.output_filename = Input(migrate_file_to_vtk._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self.output_filename)
        self.streams_container = Input(migrate_file_to_vtk._spec().input_pin(3), 3, op, -1) 
        self._inputs.append(self.streams_container)
        self.data_sources = Input(migrate_file_to_vtk._spec().input_pin(4), 4, op, -1) 
        self._inputs.append(self.data_sources)

class _OutputsMigrateFileToVtk(_Outputs):
    def __init__(self, op: Operator):
        super().__init__(migrate_file_to_vtk._spec().outputs, op)
        self.data_sources = Output(migrate_file_to_vtk._spec().output_pin(0), 0, op) 
        self._outputs.append(self.data_sources)

class migrate_file_to_vtk(Operator):
    """Take an input data sources or streams and convert as much data as possible to vtk.

      available inputs:
         output_filename (str) (optional)
         streams_container (StreamsContainer) (optional)
         data_sources (DataSources) (optional)

      available outputs:
         data_sources (DataSources)

      Examples
      --------
      >>> op = operators.serialization.migrate_file_to_vtk()

    """
    def __init__(self, output_filename=None, streams_container=None, data_sources=None, config=None, server=None):
        super().__init__(name="vtk::migrate_file", config = config, server = server)
        self.inputs = _InputsMigrateFileToVtk(self)
        self.outputs = _OutputsMigrateFileToVtk(self)
        if output_filename !=None:
            self.inputs.output_filename.connect(output_filename)
        if streams_container !=None:
            self.inputs.streams_container.connect(streams_container)
        if data_sources !=None:
            self.inputs.data_sources.connect(data_sources)

    @staticmethod
    def _spec():
        spec = Specification(description="""Take an input data sources or streams and convert as much data as possible to vtk.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "output_filename", type_names=["string"], optional=True, document=""""""), 
                                 3 : PinSpecification(name = "streams_container", type_names=["streams_container"], optional=True, document=""""""), 
                                 4 : PinSpecification(name = "data_sources", type_names=["data_sources"], optional=True, document="""""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "data_sources", type_names=["data_sources"], optional=False, document="""Generated output vtk file""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "vtk::migrate_file")

