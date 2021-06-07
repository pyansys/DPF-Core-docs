"""
normals
=======
"""
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs, _modify_output_spec_with_one_type
from ansys.dpf.core.operators.specification import PinSpecification, Specification

"""Operators from meshOperatorsCore plugin, from "geo" category
"""

class normals(Operator):
    """compute the normals at the given nodes or element scoping based on the given mesh (first version, the element normal is only handled on the shell elements)

      available inputs:
        - mesh (MeshedRegion) (optional)
        - mesh_scoping (Scoping) (optional)
        - field (Field) (optional)

      available outputs:
        - field (Field)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.geo.normals()

      >>> # Make input connections
      >>> my_mesh = dpf.MeshedRegion()
      >>> op.inputs.mesh.connect(my_mesh)
      >>> my_mesh_scoping = dpf.Scoping()
      >>> op.inputs.mesh_scoping.connect(my_mesh_scoping)
      >>> my_field = dpf.Field()
      >>> op.inputs.field.connect(my_field)

      >>> # Instantiate operator and connect inputs in one line
      >>> op = dpf.operators.geo.normals(mesh=my_mesh,mesh_scoping=my_mesh_scoping,field=my_field)

      >>> # Get output data
      >>> result_field = op.outputs.field()"""
    def __init__(self, mesh=None, mesh_scoping=None, field=None, config=None, server=None):
        super().__init__(name="normals_provider", config = config, server = server)
        self._inputs = InputsNormals(self)
        self._outputs = OutputsNormals(self)
        if mesh !=None:
            self.inputs.mesh.connect(mesh)
        if mesh_scoping !=None:
            self.inputs.mesh_scoping.connect(mesh_scoping)
        if field !=None:
            self.inputs.field.connect(field)

    @staticmethod
    def _spec():
        spec = Specification(description="""compute the normals at the given nodes or element scoping based on the given mesh (first version, the element normal is only handled on the shell elements)""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "mesh", type_names=["abstract_meshed_region"], optional=True, document=""""""), 
                                 1 : PinSpecification(name = "mesh_scoping", type_names=["scoping"], optional=True, document=""""""), 
                                 3 : PinSpecification(name = "field", type_names=["field"], optional=True, document="""""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "field", type_names=["field"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "normals_provider")

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsNormals 
        """
        return super().inputs


    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it

        Returns
        --------
        outputs : OutputsNormals 
        """
        return super().outputs


#internal name: normals_provider
#scripting name: normals
class InputsNormals(_Inputs):
    """Intermediate class used to connect user inputs to normals operator

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.geo.normals()
      >>> my_mesh = dpf.MeshedRegion()
      >>> op.inputs.mesh.connect(my_mesh)
      >>> my_mesh_scoping = dpf.Scoping()
      >>> op.inputs.mesh_scoping.connect(my_mesh_scoping)
      >>> my_field = dpf.Field()
      >>> op.inputs.field.connect(my_field)
    """
    def __init__(self, op: Operator):
        super().__init__(normals._spec().inputs, op)
        self._mesh = Input(normals._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self._mesh)
        self._mesh_scoping = Input(normals._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self._mesh_scoping)
        self._field = Input(normals._spec().input_pin(3), 3, op, -1) 
        self._inputs.append(self._field)

    @property
    def mesh(self):
        """Allows to connect mesh input to the operator

        Parameters
        ----------
        my_mesh : MeshedRegion, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.geo.normals()
        >>> op.inputs.mesh.connect(my_mesh)
        >>> #or
        >>> op.inputs.mesh(my_mesh)

        """
        return self._mesh

    @property
    def mesh_scoping(self):
        """Allows to connect mesh_scoping input to the operator

        Parameters
        ----------
        my_mesh_scoping : Scoping, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.geo.normals()
        >>> op.inputs.mesh_scoping.connect(my_mesh_scoping)
        >>> #or
        >>> op.inputs.mesh_scoping(my_mesh_scoping)

        """
        return self._mesh_scoping

    @property
    def field(self):
        """Allows to connect field input to the operator

        Parameters
        ----------
        my_field : Field, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.geo.normals()
        >>> op.inputs.field.connect(my_field)
        >>> #or
        >>> op.inputs.field(my_field)

        """
        return self._field

class OutputsNormals(_Outputs):
    """Intermediate class used to get outputs from normals operator
      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.geo.normals()
      >>> # Connect inputs : op.inputs. ...
      >>> result_field = op.outputs.field()
    """
    def __init__(self, op: Operator):
        super().__init__(normals._spec().outputs, op)
        self._field = Output(normals._spec().output_pin(0), 0, op) 
        self._outputs.append(self._field)

    @property
    def field(self):
        """Allows to get field output of the operator


        Returns
        ----------
        my_field : Field, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.geo.normals()
        >>> # Connect inputs : op.inputs. ...
        >>> result_field = op.outputs.field() 
        """
        return self._field

