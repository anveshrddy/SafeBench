''' 
Date: 2023-01-31 22:23:17
LastEditTime: 2023-03-22 16:32:04
Description: 
    Copyright (c) 2022-2023 Safebench Team

    This work is licensed under the terms of the MIT license.
    For a copy, see <https://opensource.org/licenses/MIT>
'''

# collect policy models from scenarios
from safebench.scenario.scenario_policy.dummy_policy import DummyPolicy
from safebench.scenario.scenario_policy.reinforce_continuous import REINFORCE
from safebench.scenario.scenario_policy.normalizing_flow_policy import NormalizingFlow
from safebench.scenario.scenario_policy.hardcode_policy import HardCodePolicy
from safebench.scenario.scenario_policy.adv_patch import ObjectDetection


SCENARIO_POLICY_LIST = {
    'standard': DummyPolicy,
    'ordinary': DummyPolicy,
    'scenic': DummyPolicy,
    'advsim': HardCodePolicy,
    'advtraj': HardCodePolicy,
    'lc': REINFORCE,
    'nf': NormalizingFlow,
    'od': ObjectDetection
}
