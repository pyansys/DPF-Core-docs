"""
extend_to_mid_nodes
===================
"""
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs, _modify_output_spec_with_one_type
from ansys.dpf.core.operators.specification import PinSpecification, Specification

"""Operators from Ans.Dpf.FEMutils plugin, from "averaging" category
"""

class extend_to_mid_nodes(Operator):
    """Extends ElementalNodal field defined on corner nodes to a ElementalNodal field defined also on the mid nodes.

      available inputs:
        - field (Field, FieldsContainer)
        - mesh (MeshedRegion) (optional)

      available outputs:
        - field (Field)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.averaging.extend_to_mid_nodes()

      >>> # Make input connections
      >>> my_field = dpf.Field()
      >>> op.inputs.field.connect(my_field)
      >>> my_mesh = dpf.MeshedRegion()
      >>> op.inputs.mesh.connect(my_mesh)

      >>> # Instantiate operator and connect inputs in one line
      >>> op = dpf.operators.averaging.extend_to_mid_nodes(field=my_field,mesh=my_mesh)

      >>> # Get output data
      >>> result_field = op.outputs.field()"""
    def __init__(self, field=None, mesh=None, config=None, server=None):
        super().__init__(name="extend_to_mid_nodes", config = config, server = server)
        self._inputs = InputsExtendToMidNodes(self)
        self._outputs = OutputsExtendToMidNodes(self)
        if field !=None:
            self.inputs.field.connect(field)
        if mesh !=None:
            self.inputs.mesh.connect(mesh)

    @staticmethod
    def _spec():
        spec = Specification(description="""Extends ElementalNodal field defined on corner nodes to a ElementalNodal field defined also on the mid nodes.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "field", type_names=["field","fields_container"], optional=False, document="""field or fields container with only one field is expected"""), 
                                 7 : PinSpecification(name = "mesh", type_names=["abstract_meshed_region"], optional=True, document="""""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "field", type_names=["field"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "extend_to_mid_nodes")

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsExtendToMidNodes 
        """
        return super().inputs


    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it

        Returns
        --------
        outputs : OutputsExtendToMidNodes 
        """
        return super().outputs


#internal name: extend_to_mid_nodes
#scripting name: extend_to_mid_nodes
class InputsExtendToMidNodes(_Inputs):
    """Intermediate class used to connect user inputs to extend_to_mid_nodes operator

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.averaging.extend_to_mid_nodes()
      >>> my_field = dpf.Field()
      >>> op.inputs.field.connect(my_field)
      >>> my_mesh = dpf.MeshedRegion()
      >>> op.inputs.mesh.connect(my_mesh)
    """
    def __init__(self, op: Operator):
        super().__init__(extend_to_mid_nodes._spec().inputs, op)
        self._field = Input(extend_to_mid_nodes._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self._field)
        self._mesh = Input(extend_to_mid_nodes._spec().input_pin(7), 7, op, -1) 
        self._inputs.append(self._mesh)

    @property
    def field(self):
        """Allows to connect field input to the operator

        - pindoc: field or fields container with only one field is expected

        Parameters
        ----------
        my_field : Field, FieldsContainer, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.averaging.extend_to_mid_nodes()
        >>> op.inputs.field.connect(my_field)
        >>> #or
        >>> op.inputs.field(my_field)

        """
        return self._field

    @property
    def mesh(self):
        """Allows to connect mesh input to the operator

        Parameters
        ----------
        my_mesh : MeshedRegion, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.averaging.extend_to_mid_nodes()
        >>> op.inputs.mesh.connect(my_mesh)
        >>> #or
        >>> op.inputs.mesh(my_mesh)

        """
        return self._mesh

class OutputsExtendToMidNodes(_Outputs):
    """Intermediate class used to get outputs from extend_to_mid_nodes operator
      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.averaging.extend_to_mid_nodes()
      >>> # Connect inputs : op.inputs. ...
      >>> result_field = op.outputs.field()
    """
    def __init__(self, op: Operator):
        super().__init__(extend_to_mid_nodes._spec().outputs, op)
        self._field = Output(extend_to_mid_nodes._spec().output_pin(0), 0, op) 
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

        >>> op = dpf.operators.averaging.extend_to_mid_nodes()
        >>> # Connect inputs : op.inputs. ...
        >>> result_field = op.outputs.field() 
        """
        return self._field

