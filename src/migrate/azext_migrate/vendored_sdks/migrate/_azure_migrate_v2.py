# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import TYPE_CHECKING

from azure.mgmt.core import ARMPipelineClient
from msrest import Deserializer, Serializer

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Optional

    from azure.core.credentials import TokenCredential

from ._configuration import AzureMigrateV2Configuration
from .operations import ProjectOperations
from .operations import MachineOperations
from .operations import GroupOperations
from .operations import AssessmentOperations
from .operations import AssessedMachineOperations
from .operations import HyperVCollectorOperations
from .operations import VMwareCollectorOperations
from .operations import OperationOperations
from . import models


class AzureMigrateV2(object):
    """Assess your workloads for Azure.

    :ivar project: ProjectOperations operations
    :vartype project: azure_migrate_v2.operations.ProjectOperations
    :ivar machine: MachineOperations operations
    :vartype machine: azure_migrate_v2.operations.MachineOperations
    :ivar group: GroupOperations operations
    :vartype group: azure_migrate_v2.operations.GroupOperations
    :ivar assessment: AssessmentOperations operations
    :vartype assessment: azure_migrate_v2.operations.AssessmentOperations
    :ivar assessed_machine: AssessedMachineOperations operations
    :vartype assessed_machine: azure_migrate_v2.operations.AssessedMachineOperations
    :ivar hyper_vcollector: HyperVCollectorOperations operations
    :vartype hyper_vcollector: azure_migrate_v2.operations.HyperVCollectorOperations
    :ivar vmware_collector: VMwareCollectorOperations operations
    :vartype vmware_collector: azure_migrate_v2.operations.VMwareCollectorOperations
    :ivar operation: OperationOperations operations
    :vartype operation: azure_migrate_v2.operations.OperationOperations
    :param credential: Credential needed for the client to connect to Azure.
    :type credential: ~azure.core.credentials.TokenCredential
    :param subscription_id: Azure Subscription Id in which project was created.
    :type subscription_id: str
    :param str base_url: Service URL
    """

    def __init__(
        self,
        credential,  # type: "TokenCredential"
        subscription_id,  # type: str
        base_url=None,  # type: Optional[str]
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        if not base_url:
            base_url = 'https://management.azure.com'
        self._config = AzureMigrateV2Configuration(credential, subscription_id, **kwargs)
        self._client = ARMPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.project = ProjectOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.machine = MachineOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.group = GroupOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.assessment = AssessmentOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.assessed_machine = AssessedMachineOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.hyper_vcollector = HyperVCollectorOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.vmware_collector = VMwareCollectorOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.operation = OperationOperations(
            self._client, self._config, self._serialize, self._deserialize)

    def close(self):
        # type: () -> None
        self._client.close()

    def __enter__(self):
        # type: () -> AzureMigrateV2
        self._client.__enter__()
        return self

    def __exit__(self, *exc_details):
        # type: (Any) -> None
        self._client.__exit__(*exc_details)
