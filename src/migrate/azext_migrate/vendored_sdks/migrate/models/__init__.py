# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

try:
    from ._models_py3 import AssessedDisk
    from ._models_py3 import AssessedMachine
    from ._models_py3 import AssessedMachineProperties
    from ._models_py3 import AssessedMachineResultList
    from ._models_py3 import AssessedNetworkAdapter
    from ._models_py3 import Assessment
    from ._models_py3 import AssessmentOptions
    from ._models_py3 import AssessmentOptionsProperties
    from ._models_py3 import AssessmentOptionsResultList
    from ._models_py3 import AssessmentResultList
    from ._models_py3 import CloudErrorBody
    from ._models_py3 import CollectorBodyAgentSpnProperties
    from ._models_py3 import Disk
    from ._models_py3 import DownloadUrl
    from ._models_py3 import Group
    from ._models_py3 import GroupBodyProperties
    from ._models_py3 import GroupProperties
    from ._models_py3 import GroupResultList
    from ._models_py3 import HyperVCollector
    from ._models_py3 import HyperVCollectorList
    from ._models_py3 import Machine
    from ._models_py3 import MachineProperties
    from ._models_py3 import MachineResultList
    from ._models_py3 import NetworkAdapter
    from ._models_py3 import Operation
    from ._models_py3 import OperationDisplay
    from ._models_py3 import OperationResultList
    from ._models_py3 import Project
    from ._models_py3 import ProjectProperties
    from ._models_py3 import ProjectResultList
    from ._models_py3 import UpdateGroupBody
    from ._models_py3 import VMwareCollector
    from ._models_py3 import VMwareCollectorList
    from ._models_py3 import VmFamily
    from ._models_py3 import VmUptime
except (SyntaxError, ImportError):
    from ._models import AssessedDisk  # type: ignore
    from ._models import AssessedMachine  # type: ignore
    from ._models import AssessedMachineProperties  # type: ignore
    from ._models import AssessedMachineResultList  # type: ignore
    from ._models import AssessedNetworkAdapter  # type: ignore
    from ._models import Assessment  # type: ignore
    from ._models import AssessmentOptions  # type: ignore
    from ._models import AssessmentOptionsProperties  # type: ignore
    from ._models import AssessmentOptionsResultList  # type: ignore
    from ._models import AssessmentResultList  # type: ignore
    from ._models import CloudErrorBody  # type: ignore
    from ._models import CollectorBodyAgentSpnProperties  # type: ignore
    from ._models import Disk  # type: ignore
    from ._models import DownloadUrl  # type: ignore
    from ._models import Group  # type: ignore
    from ._models import GroupBodyProperties  # type: ignore
    from ._models import GroupProperties  # type: ignore
    from ._models import GroupResultList  # type: ignore
    from ._models import HyperVCollector  # type: ignore
    from ._models import HyperVCollectorList  # type: ignore
    from ._models import Machine  # type: ignore
    from ._models import MachineProperties  # type: ignore
    from ._models import MachineResultList  # type: ignore
    from ._models import NetworkAdapter  # type: ignore
    from ._models import Operation  # type: ignore
    from ._models import OperationDisplay  # type: ignore
    from ._models import OperationResultList  # type: ignore
    from ._models import Project  # type: ignore
    from ._models import ProjectProperties  # type: ignore
    from ._models import ProjectResultList  # type: ignore
    from ._models import UpdateGroupBody  # type: ignore
    from ._models import VMwareCollector  # type: ignore
    from ._models import VMwareCollectorList  # type: ignore
    from ._models import VmFamily  # type: ignore
    from ._models import VmUptime  # type: ignore

from ._azure_migrate_v2_enums import (
    AssessmentSizingCriterion,
    AssessmentStage,
    AssessmentStatus,
    AzureDiskSize,
    AzureDiskSuitabilityDetail,
    AzureDiskSuitabilityExplanation,
    AzureDiskType,
    AzureHybridUseBenefit,
    AzureLocation,
    AzureNetworkAdapterSuitabilityDetail,
    AzureNetworkAdapterSuitabilityExplanation,
    AzureOfferCode,
    AzurePricingTier,
    AzureStorageRedundancy,
    AzureVmFamily,
    AzureVmSize,
    AzureVmSuitabilityDetail,
    AzureVmSuitabilityExplanation,
    CloudSuitability,
    Currency,
    GroupStatus,
    GroupUpdateOperation,
    MachineBootType,
    Percentile,
    ProjectStatus,
    ProvisioningState,
    ReservedInstance,
    TimeRange,
)

__all__ = [
    'AssessedDisk',
    'AssessedMachine',
    'AssessedMachineProperties',
    'AssessedMachineResultList',
    'AssessedNetworkAdapter',
    'Assessment',
    'AssessmentOptions',
    'AssessmentOptionsProperties',
    'AssessmentOptionsResultList',
    'AssessmentResultList',
    'CloudErrorBody',
    'CollectorBodyAgentSpnProperties',
    'Disk',
    'DownloadUrl',
    'Group',
    'GroupBodyProperties',
    'GroupProperties',
    'GroupResultList',
    'HyperVCollector',
    'HyperVCollectorList',
    'Machine',
    'MachineProperties',
    'MachineResultList',
    'NetworkAdapter',
    'Operation',
    'OperationDisplay',
    'OperationResultList',
    'Project',
    'ProjectProperties',
    'ProjectResultList',
    'UpdateGroupBody',
    'VMwareCollector',
    'VMwareCollectorList',
    'VmFamily',
    'VmUptime',
    'AssessmentSizingCriterion',
    'AssessmentStage',
    'AssessmentStatus',
    'AzureDiskSize',
    'AzureDiskSuitabilityDetail',
    'AzureDiskSuitabilityExplanation',
    'AzureDiskType',
    'AzureHybridUseBenefit',
    'AzureLocation',
    'AzureNetworkAdapterSuitabilityDetail',
    'AzureNetworkAdapterSuitabilityExplanation',
    'AzureOfferCode',
    'AzurePricingTier',
    'AzureStorageRedundancy',
    'AzureVmFamily',
    'AzureVmSize',
    'AzureVmSuitabilityDetail',
    'AzureVmSuitabilityExplanation',
    'CloudSuitability',
    'Currency',
    'GroupStatus',
    'GroupUpdateOperation',
    'MachineBootType',
    'Percentile',
    'ProjectStatus',
    'ProvisioningState',
    'ReservedInstance',
    'TimeRange',
]
