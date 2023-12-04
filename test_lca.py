import pytest
from lca import GoalAndScopeDefinition, LifeCycleInventory


@pytest.fixture
def goal_and_scope_definition():
    return GoalAndScopeDefinition(
        study_name="Test Study",
        functional_unit="1 kg of product",
        target_audience=["Product developers", "Decision makers"],
        limitations={"Data availability": "Some data were unavailable"}
    )


def test_goal_and_scope_definition_init(goal_and_scope_definition):
    assert goal_and_scope_definition.phase_name == "Goal and Scope Definition"
    assert goal_and_scope_definition.study_name == "Test Study"
    assert goal_and_scope_definition.functional_unit == "1 kg of product"
    assert goal_and_scope_definition.target_audience == ["Product developers", "Decision makers"]
    assert goal_and_scope_definition.limitations == {
        "Data availability": "Some data were unavailable"
    }


def test_goal_and_scope_definition_get_phase_results(goal_and_scope_definition):
    phase_results = goal_and_scope_definition.get_phase_results()
    assert phase_results["phase_name"] == goal_and_scope_definition.phase_name
    assert phase_results["study_name"] == goal_and_scope_definition.study_name
    assert phase_results["functional_unit"] == goal_and_scope_definition.functional_unit
    assert phase_results["target_audience"] == goal_and_scope_definition.target_audience
    assert phase_results["limitations"] == goal_and_scope_definition.limitations


@pytest.fixture
def life_cycle_inventory():
    return LifeCycleInventory(
        unit_processes={
            "Process A": {"inputs": [], "outputs": []},
            "Process B": {"inputs": [], "outputs": []}
        },
        elementary_flows={
            "CO2": {"amount": 10, "unit": "kg"},
            "Water": {"amount": 50, "unit": "L"}
        }
    )


def test_life_cycle_inventory_init(life_cycle_inventory):
    assert life_cycle_inventory.phase_name == "Life Cycle Inventory"
    assert life_cycle_inventory.unit_processes == {
        "Process A": {"inputs": [], "outputs": []},
        "Process B": {"inputs": [], "outputs": []}
    }
    assert life_cycle_inventory.elementary_flows == {
        "CO2": {"amount": 10, "unit": "kg"},
        "Water": {"amount": 50, "unit": "L"}
    }


def test_life_cycle_inventory_get_phase_results(life_cycle_inventory):
    phase_results = life_cycle_inventory.get_phase_results()
    assert phase_results["phase_name"] == life_cycle_inventory.phase_name
    assert phase_results["unit_processes"] == life_cycle_inventory.unit_processes
    assert phase_results["elementary_flows"] == life_cycle_inventory.elementary_flows
