from openfisca_core.model_api import *
from openfisca_us.entities import *


class person_id(Variable):
    value_type = int
    entity = Person
    label = u"Unique reference for this person"
    definition_period = ETERNITY


class person_weight(Variable):
    value_type = float
    entity = Person
    label = u"Person weight"
    definition_period = YEAR


class is_tax_unit_head(Variable):
    value_type = bool
    entity = Person
    label = "Head of tax unit"
    definition_period = YEAR

    def formula(person, period, parameters):
        # Use order of input (first)
        return person.tax_unit.members_position == 0


class is_tax_unit_spouse(Variable):
    value_type = bool
    entity = Person
    label = "Spouse of tax unit"
    definition_period = YEAR

    def formula(person, period, parameters):
        # Use order of input (second)
        return person.tax_unit.members_position == 1


class age(Variable):
    value_type = int
    entity = Person
    label = u"Age"
    definition_period = YEAR