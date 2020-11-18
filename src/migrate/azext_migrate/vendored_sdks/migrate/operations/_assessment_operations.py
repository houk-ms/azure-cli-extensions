# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import TYPE_CHECKING
import warnings

from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.paging import ItemPaged
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpRequest, HttpResponse
from azure.mgmt.core.exceptions import ARMErrorFormat

from .. import models

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Callable, Dict, Generic, Iterable, List, Optional, TypeVar, Union

    T = TypeVar('T')
    ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

class AssessmentOperations(object):
    """AssessmentOperations operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~azure_migrate_v2.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = models

    def __init__(self, client, config, serializer, deserializer):
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    def list_by_group(
        self,
        resource_group_name,  # type: str
        project_name,  # type: str
        group_name,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> Iterable["models.AssessmentResultList"]
        """Get all assessments created for the specified group.

        Get all assessments created for the specified group.

        Returns a json array of objects of type 'assessment' as specified in Models section.

        :param resource_group_name: Name of the Azure Resource Group that project is part of.
        :type resource_group_name: str
        :param project_name: Name of the Azure Migrate project.
        :type project_name: str
        :param group_name: Unique name of a group within a project.
        :type group_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either AssessmentResultList or the result of cls(response)
        :rtype: ~azure.core.paging.ItemPaged[~azure_migrate_v2.models.AssessmentResultList]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.AssessmentResultList"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2019-10-01"
        accept = "application/json"

        def prepare_request(next_link=None):
            # Construct headers
            header_parameters = {}  # type: Dict[str, Any]
            header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

            if not next_link:
                # Construct URL
                url = self.list_by_group.metadata['url']  # type: ignore
                path_format_arguments = {
                    'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
                    'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
                    'projectName': self._serialize.url("project_name", project_name, 'str'),
                    'groupName': self._serialize.url("group_name", group_name, 'str'),
                }
                url = self._client.format_url(url, **path_format_arguments)
                # Construct parameters
                query_parameters = {}  # type: Dict[str, Any]
                query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

                request = self._client.get(url, query_parameters, header_parameters)
            else:
                url = next_link
                query_parameters = {}  # type: Dict[str, Any]
                request = self._client.get(url, query_parameters, header_parameters)
            return request

        def extract_data(pipeline_response):
            deserialized = self._deserialize('AssessmentResultList', pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return None, iter(list_of_elem)

        def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response, error_format=ARMErrorFormat)

            return pipeline_response

        return ItemPaged(
            get_next, extract_data
        )
    list_by_group.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Migrate/assessmentProjects/{projectName}/groups/{groupName}/assessments'}  # type: ignore

    def list_by_project(
        self,
        resource_group_name,  # type: str
        project_name,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> Iterable["models.AssessmentResultList"]
        """Get all assessments created in the project.

        Get all assessments created in the project.

        Returns a json array of objects of type 'assessment' as specified in Models section.

        :param resource_group_name: Name of the Azure Resource Group that project is part of.
        :type resource_group_name: str
        :param project_name: Name of the Azure Migrate project.
        :type project_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either AssessmentResultList or the result of cls(response)
        :rtype: ~azure.core.paging.ItemPaged[~azure_migrate_v2.models.AssessmentResultList]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.AssessmentResultList"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2019-10-01"
        accept = "application/json"

        def prepare_request(next_link=None):
            # Construct headers
            header_parameters = {}  # type: Dict[str, Any]
            header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

            if not next_link:
                # Construct URL
                url = self.list_by_project.metadata['url']  # type: ignore
                path_format_arguments = {
                    'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
                    'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
                    'projectName': self._serialize.url("project_name", project_name, 'str'),
                }
                url = self._client.format_url(url, **path_format_arguments)
                # Construct parameters
                query_parameters = {}  # type: Dict[str, Any]
                query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

                request = self._client.get(url, query_parameters, header_parameters)
            else:
                url = next_link
                query_parameters = {}  # type: Dict[str, Any]
                request = self._client.get(url, query_parameters, header_parameters)
            return request

        def extract_data(pipeline_response):
            deserialized = self._deserialize('AssessmentResultList', pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return None, iter(list_of_elem)

        def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response, error_format=ARMErrorFormat)

            return pipeline_response

        return ItemPaged(
            get_next, extract_data
        )
    list_by_project.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Migrate/assessmentProjects/{projectName}/assessments'}  # type: ignore

    def get(
        self,
        resource_group_name,  # type: str
        project_name,  # type: str
        group_name,  # type: str
        assessment_name,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.Assessment"
        """Get an assessment.

        Get an existing assessment with the specified name. Returns a json object of type 'assessment'
        as specified in Models section.

        :param resource_group_name: Name of the Azure Resource Group that project is part of.
        :type resource_group_name: str
        :param project_name: Name of the Azure Migrate project.
        :type project_name: str
        :param group_name: Unique name of a group within a project.
        :type group_name: str
        :param assessment_name: Unique name of an assessment within a project.
        :type assessment_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: Assessment, or the result of cls(response)
        :rtype: ~azure_migrate_v2.models.Assessment
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.Assessment"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2019-10-01"
        accept = "application/json"

        # Construct URL
        url = self.get.metadata['url']  # type: ignore
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'projectName': self._serialize.url("project_name", project_name, 'str'),
            'groupName': self._serialize.url("group_name", group_name, 'str'),
            'assessmentName': self._serialize.url("assessment_name", assessment_name, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        response_headers = {}
        response_headers['x-ms-request-id']=self._deserialize('str', response.headers.get('x-ms-request-id'))
        deserialized = self._deserialize('Assessment', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, response_headers)

        return deserialized
    get.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Migrate/assessmentProjects/{projectName}/groups/{groupName}/assessments/{assessmentName}'}  # type: ignore

    def create(
        self,
        resource_group_name,  # type: str
        project_name,  # type: str
        group_name,  # type: str
        assessment_name,  # type: str
        e_tag=None,  # type: Optional[str]
        azure_location=None,  # type: Optional[Union[str, "models.AzureLocation"]]
        azure_offer_code=None,  # type: Optional[Union[str, "models.AzureOfferCode"]]
        azure_pricing_tier=None,  # type: Optional[Union[str, "models.AzurePricingTier"]]
        azure_storage_redundancy=None,  # type: Optional[Union[str, "models.AzureStorageRedundancy"]]
        scaling_factor=None,  # type: Optional[float]
        percentile=None,  # type: Optional[Union[str, "models.Percentile"]]
        time_range=None,  # type: Optional[Union[str, "models.TimeRange"]]
        stage=None,  # type: Optional[Union[str, "models.AssessmentStage"]]
        currency=None,  # type: Optional[Union[str, "models.Currency"]]
        azure_hybrid_use_benefit=None,  # type: Optional[Union[str, "models.AzureHybridUseBenefit"]]
        discount_percentage=None,  # type: Optional[float]
        sizing_criterion=None,  # type: Optional[Union[str, "models.AssessmentSizingCriterion"]]
        reserved_instance=None,  # type: Optional[Union[str, "models.ReservedInstance"]]
        azure_vm_families=None,  # type: Optional[List[Union[str, "models.AzureVmFamily"]]]
        azure_disk_type=None,  # type: Optional[Union[str, "models.AzureDiskType"]]
        vm_uptime=None,  # type: Optional["models.VmUptime"]
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.Assessment"
        """Create or Update assessment.

        Create a new assessment with the given name and the specified settings. Since name of an
        assessment in a project is a unique identifier, if an assessment with the name provided already
        exists, then the existing assessment is updated.

        Any PUT operation, resulting in either create or update on an assessment, will cause the
        assessment to go in a "InProgress" state. This will be indicated by the field
        'computationState' on the Assessment object. During this time no other PUT operation will be
        allowed on that assessment object, nor will a Delete operation. Once the computation for the
        assessment is complete, the field 'computationState' will be updated to 'Ready', and then other
        PUT or DELETE operations can happen on the assessment.

        When assessment is under computation, any PUT will lead to a 400 - Bad Request error.

        :param resource_group_name: Name of the Azure Resource Group that project is part of.
        :type resource_group_name: str
        :param project_name: Name of the Azure Migrate project.
        :type project_name: str
        :param group_name: Unique name of a group within a project.
        :type group_name: str
        :param assessment_name: Unique name of an assessment within a project.
        :type assessment_name: str
        :param e_tag: For optimistic concurrency control.
        :type e_tag: str
        :param azure_location: Target Azure location for which the machines should be assessed. These
         enums are the same as used by Compute API.
        :type azure_location: str or ~azure_migrate_v2.models.AzureLocation
        :param azure_offer_code: Offer code according to which cost estimation is done.
        :type azure_offer_code: str or ~azure_migrate_v2.models.AzureOfferCode
        :param azure_pricing_tier: Pricing tier for Size evaluation.
        :type azure_pricing_tier: str or ~azure_migrate_v2.models.AzurePricingTier
        :param azure_storage_redundancy: Storage Redundancy type offered by Azure.
        :type azure_storage_redundancy: str or ~azure_migrate_v2.models.AzureStorageRedundancy
        :param scaling_factor: Scaling factor used over utilization data to add a performance buffer
         for new machines to be created in Azure. Min Value = 1.0, Max value = 1.9, Default = 1.3.
        :type scaling_factor: float
        :param percentile: Percentile of performance data used to recommend Azure size.
        :type percentile: str or ~azure_migrate_v2.models.Percentile
        :param time_range: Time range of performance data used to recommend a size.
        :type time_range: str or ~azure_migrate_v2.models.TimeRange
        :param stage: User configurable setting that describes the status of the assessment.
        :type stage: str or ~azure_migrate_v2.models.AssessmentStage
        :param currency: Currency to report prices in.
        :type currency: str or ~azure_migrate_v2.models.Currency
        :param azure_hybrid_use_benefit: AHUB discount on windows virtual machines.
        :type azure_hybrid_use_benefit: str or ~azure_migrate_v2.models.AzureHybridUseBenefit
        :param discount_percentage: Custom discount percentage to be applied on final costs. Can be in
         the range [0, 100].
        :type discount_percentage: float
        :param sizing_criterion: Assessment sizing criterion.
        :type sizing_criterion: str or ~azure_migrate_v2.models.AssessmentSizingCriterion
        :param reserved_instance: Azure reserved instance.
        :type reserved_instance: str or ~azure_migrate_v2.models.ReservedInstance
        :param azure_vm_families: List of azure VM families.
        :type azure_vm_families: list[str or ~azure_migrate_v2.models.AzureVmFamily]
        :param azure_disk_type: Storage type selected for this disk.
        :type azure_disk_type: str or ~azure_migrate_v2.models.AzureDiskType
        :param vm_uptime: Specify the duration for which the VMs are up in the on-premises environment.
        :type vm_uptime: ~azure_migrate_v2.models.VmUptime
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: Assessment, or the result of cls(response)
        :rtype: ~azure_migrate_v2.models.Assessment
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.Assessment"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        assessment = models.Assessment(e_tag=e_tag, azure_location=azure_location, azure_offer_code=azure_offer_code, azure_pricing_tier=azure_pricing_tier, azure_storage_redundancy=azure_storage_redundancy, scaling_factor=scaling_factor, percentile=percentile, time_range=time_range, stage=stage, currency=currency, azure_hybrid_use_benefit=azure_hybrid_use_benefit, discount_percentage=discount_percentage, sizing_criterion=sizing_criterion, reserved_instance=reserved_instance, azure_vm_families=azure_vm_families, azure_disk_type=azure_disk_type, vm_uptime=vm_uptime)
        api_version = "2019-10-01"
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json"

        # Construct URL
        url = self.create.metadata['url']  # type: ignore
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'projectName': self._serialize.url("project_name", project_name, 'str'),
            'groupName': self._serialize.url("group_name", group_name, 'str'),
            'assessmentName': self._serialize.url("assessment_name", assessment_name, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        if assessment is not None:
            body_content = self._serialize.body(assessment, 'Assessment')
        else:
            body_content = None
        body_content_kwargs['content'] = body_content
        request = self._client.put(url, query_parameters, header_parameters, **body_content_kwargs)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        response_headers = {}
        if response.status_code == 200:
            response_headers['x-ms-request-id']=self._deserialize('str', response.headers.get('x-ms-request-id'))
            deserialized = self._deserialize('Assessment', pipeline_response)

        if response.status_code == 201:
            response_headers['x-ms-request-id']=self._deserialize('str', response.headers.get('x-ms-request-id'))
            deserialized = self._deserialize('Assessment', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, response_headers)

        return deserialized
    create.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Migrate/assessmentProjects/{projectName}/groups/{groupName}/assessments/{assessmentName}'}  # type: ignore

    def delete(
        self,
        resource_group_name,  # type: str
        project_name,  # type: str
        group_name,  # type: str
        assessment_name,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Deletes an assessment from the project.

        Delete an assessment from the project. The machines remain in the assessment. Deleting a non-
        existent assessment results in a no-operation.

        When an assessment is under computation, as indicated by the 'computationState' field, it
        cannot be deleted. Any such attempt will return a 400 - Bad Request.

        :param resource_group_name: Name of the Azure Resource Group that project is part of.
        :type resource_group_name: str
        :param project_name: Name of the Azure Migrate project.
        :type project_name: str
        :param group_name: Unique name of a group within a project.
        :type group_name: str
        :param assessment_name: Unique name of an assessment within a project.
        :type assessment_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2019-10-01"
        accept = "application/json"

        # Construct URL
        url = self.delete.metadata['url']  # type: ignore
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'projectName': self._serialize.url("project_name", project_name, 'str'),
            'groupName': self._serialize.url("group_name", group_name, 'str'),
            'assessmentName': self._serialize.url("assessment_name", assessment_name, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        request = self._client.delete(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        response_headers = {}
        if response.status_code == 200:
            response_headers['x-ms-request-id']=self._deserialize('str', response.headers.get('x-ms-request-id'))

        if cls:
            return cls(pipeline_response, None, response_headers)

    delete.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Migrate/assessmentProjects/{projectName}/groups/{groupName}/assessments/{assessmentName}'}  # type: ignore

    def get_report_download_url(
        self,
        resource_group_name,  # type: str
        project_name,  # type: str
        group_name,  # type: str
        assessment_name,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.DownloadUrl"
        """Get download URL for the assessment report.

        Get the URL for downloading the assessment in a report format.

        :param resource_group_name: Name of the Azure Resource Group that project is part of.
        :type resource_group_name: str
        :param project_name: Name of the Azure Migrate project.
        :type project_name: str
        :param group_name: Unique name of a group within a project.
        :type group_name: str
        :param assessment_name: Unique name of an assessment within a project.
        :type assessment_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: DownloadUrl, or the result of cls(response)
        :rtype: ~azure_migrate_v2.models.DownloadUrl
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.DownloadUrl"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2019-10-01"
        accept = "application/json"

        # Construct URL
        url = self.get_report_download_url.metadata['url']  # type: ignore
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'projectName': self._serialize.url("project_name", project_name, 'str'),
            'groupName': self._serialize.url("group_name", group_name, 'str'),
            'assessmentName': self._serialize.url("assessment_name", assessment_name, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        request = self._client.post(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        response_headers = {}
        response_headers['x-ms-request-id']=self._deserialize('str', response.headers.get('x-ms-request-id'))
        deserialized = self._deserialize('DownloadUrl', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, response_headers)

        return deserialized
    get_report_download_url.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Migrate/assessmentProjects/{projectName}/groups/{groupName}/assessments/{assessmentName}/downloadUrl'}  # type: ignore
