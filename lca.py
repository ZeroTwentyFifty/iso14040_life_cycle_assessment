from abc import ABC, abstractmethod
from typing import Dict, List


class LCAPhase(ABC):
    def __init__(self, phase_name: str):
        self.phase_name = phase_name

    @abstractmethod
    def get_phase_results(self) -> Dict:
        pass


class GoalAndScopeDefinition(LCAPhase):
    def __init__(self, study_name: str, functional_unit: str,
                 target_audience: List[str], limitations: Dict[str, str]):
        super().__init__(phase_name="Goal and Scope Definition")
        self.study_name = study_name
        self.functional_unit = functional_unit
        self.target_audience = target_audience
        self.limitations = limitations

    def get_phase_results(self) -> Dict:
        return {
            "phase_name": self.phase_name,
            "study_name": self.study_name,
            "functional_unit": self.functional_unit,
            "target_audience": self.target_audience,
            "limitations": self.limitations,
        }


class LifeCycleInventory(LCAPhase):
    def __init__(self, unit_processes: Dict[str, dict], elementary_flows: Dict[str, dict]):
        super().__init__(phase_name="Life Cycle Inventory")
        self.unit_processes = unit_processes
        self.elementary_flows = elementary_flows

    def get_phase_results(self) -> Dict:
        return {
            "phase_name": self.phase_name,
            "unit_processes": self.unit_processes,
            "elementary_flows": self.elementary_flows,
        }


class LifeCycleImpactAssessment(LCAPhase):
    def __init__(self, impact_categories: Dict[str, str],
                 characterization_factors: Dict[str, dict],
                 normalization_factors: Dict[str, float],
                 impact_results: Dict[str, float]):
        super().__init__(phase_name="Life Cycle Impact Assessment")
        self.impact_categories = impact_categories
        self.characterization_factors = characterization_factors
        self.normalization_factors = normalization_factors
        self.impact_results = impact_results

    def get_phase_results(self) -> Dict:
        return {
            "phase_name": self.phase_name,
            "impact_categories": self.impact_categories,
            "characterization_factors": self.characterization_factors,
            "normalization_factors": self.normalization_factors,
            "impact_results": self.impact_results,
        }


class Interpretation(LCAPhase):
    def __init__(self, conclusions: str, recommendations: List[str],
                 uncertainty_analysis: Dict[str, str]):
        super().__init__(phase_name="Interpretation")
        self.conclusions = conclusions
        self.recommendations = recommendations
        self.uncertainty_analysis = uncertainty_analysis

    def get_phase_results(self) -> Dict:
        return {
            "phase_name": self.phase_name,
            "conclusions": self.conclusions,
            "recommendations": self.recommendations,
            "uncertainty_analysis": self.uncertainty_analysis,
        }


class LifeCycleAssessment:
    def __init__(self,
                 goal_and_scope: GoalAndScopeDefinition,
                 inventory: LifeCycleInventory,
                 impact_assessment: LifeCycleImpactAssessment,
                 interpretation: Interpretation):
        self._goal_and_scope = goal_and_scope
        self._inventory = inventory
        self._impact_assessment = impact_assessment
        self._interpretation = interpretation

    @property
    def goal_and_scope(self) -> GoalAndScopeDefinition:
        return self._goal_and_scope

    @property
    def inventory(self) -> LifeCycleInventory:
        return self._inventory

    @property
    def impact_assessment(self) -> LifeCycleImpactAssessment:
        return self._impact_assessment

    @property
    def interpretation(self) -> Interpretation:
        return self._interpretation

    def get_all_phase_results(self) -> Dict:
        return {
            "Goal and Scope Definition": self.goal_and_scope.get_phase_results(),
            "Life Cycle Inventory": self.inventory.get_phase_results(),
            "Life Cycle Impact Assessment": self.impact_assessment.get_phase_results(),
            "Interpretation": self.interpretation.get_phase_results(),
        }