# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# pylint: disable=too-many-lines
# pylint: disable=too-many-statements

from knack.arguments import CLIArgumentType
from azure.cli.core.commands.parameters import (
    tags_type,
    resource_group_name_type,
    get_location_type
)
from azext_devops.action import (
    AddOrganization,
    AddProject
)


def load_arguments(self, _):

    with self.argument_context('devops pipeline-template-definition list') as c:
        pass

    with self.argument_context('devops pipeline list') as c:
        c.argument('resource_group_name', resource_group_name_type, help='Name of the resource group within the Azure s'
                   'ubscription.')

    with self.argument_context('devops pipeline show') as c:
        c.argument('resource_group_name', resource_group_name_type, help='Name of the resource group within the Azure s'
                   'ubscription.')
        c.argument('pipeline_name', help='The name of the Azure Pipeline resource in ARM.')

    with self.argument_context('devops pipeline create') as c:
        c.argument('resource_group_name', resource_group_name_type, help='Name of the resource group within the Azure s'
                   'ubscription.')
        c.argument('pipeline_name', help='The name of the Azure Pipeline resource in ARM.')
        c.argument('tags', tags_type, help='Resource Tags')
        c.argument('location', arg_type=get_location_type(self.cli_ctx), help='Resource Location')
        c.argument('organization', action=AddOrganization, nargs='+', help='Reference to the Azure DevOps Organization '
                   'containing the Pipeline.')
        c.argument('project', action=AddProject, nargs='+', help='Reference to the Azure DevOps Project containing the '
                   'Pipeline.')
        c.argument('bootstrap_configuration', arg_type=CLIArgumentType(options_list=['--bootstrap-configuration'],
                   help='Configuration used to bootstrap the Pipeline.'))

    with self.argument_context('devops pipeline update') as c:
        c.argument('resource_group_name', resource_group_name_type, help='Name of the resource group within the Azure s'
                   'ubscription.')
        c.argument('pipeline_name', help='The name of the Azure Pipeline resource.')
        c.argument('tags', tags_type, help='Dictionary of key-value pairs to be set as tags on the Azure Pipeline. This'
                   ' will overwrite any existing tags.')

    with self.argument_context('devops pipeline delete') as c:
        c.argument('resource_group_name', resource_group_name_type, help='Name of the resource group within the Azure s'
                   'ubscription.')
        c.argument('pipeline_name', help='The name of the Azure Pipeline resource.')
