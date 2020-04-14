# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------


def cf_devops(cli_ctx, *_):
    from azure.cli.core.commands.client_factory import get_mgmt_service_client
    from ..vendored_sdks.devops import AzureDevOps
    return get_mgmt_service_client(cli_ctx, AzureDevOps)


def cf_pipeline_template_definition(cli_ctx, *_):
    return cf_devops(cli_ctx).pipeline_template_definition


def cf_pipeline(cli_ctx, *_):
    return cf_devops(cli_ctx).pipeline
