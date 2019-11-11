# VisualStudio

> see https://aka.ms/autorest

This is the AutoRest configuration file for VisualStudio.


The App service RP comprises of services where each service has its own tag.
Hence, each sub-service has its own swagger spec.

All of them are tied together using this configuration and are packaged together into one compute client library.
This makes it easier for customers to download one (NuGet/npm/pip/maven/gem) compute client library package rather than installing individual packages for each sub service.


---
## Getting Started
To build the SDK for VisualStudio, simply [Install AutoRest](https://aka.ms/autorest/install) and in this folder, run:

> `autorest`

To see additional help and options, run:

> `autorest --help`
---

## Configuration



### Basic Information
These are the global settings for the VisualStudio API.

``` yaml
openapi-type: arm
tag: package-2014-04-preview
```


### Tag: package-2014-04-preview

These settings apply only when `--tag=package-2014-04-preview` is specified on the command line.

``` yaml $(tag) == 'package-2014-04-preview'
input-file:
- Microsoft.VisualStudio/preview/2014-04-01-preview/Csm.json
```


---
## Code Generation


## Swagger to SDK

This section describes what SDK should be generated by the automatic system.
This is not used by Autorest itself.

``` yaml $(swagger-to-sdk)
swagger-to-sdk:
  - repo: azure-sdk-for-go
  - repo: azure-sdk-for-node
  - repo: azure-sdk-for-js
```

## Go

See configuration in [readme.go.md](./readme.go.md)

## Java

These settings apply only when `--java` is specified on the command line.
Please also specify `--azure-libraries-for-java-folder=<path to the root directory of your azure-libraries-for-java clone>`.

``` yaml $(java)
azure-arm: true
fluent: true
namespace: com.microsoft.azure.management.visualstudio
license-header: MICROSOFT_MIT_NO_CODEGEN
payload-flattening-threshold: 1
output-folder: $(azure-libraries-for-java-folder)/azure-mgmt-visualstudio
```

### Java multi-api

``` yaml $(java) && $(multiapi)
batch:
  - tag: package-2014-04-preview
```

### Tag: package-2014-04-preview and java

These settings apply only when `--tag=package-2014-04-preview --java` is specified on the command line.
Please also specify `--azure-libraries-for-java=<path to the root directory of your azure-sdk-for-java clone>`.

``` yaml $(tag) == 'package-2014-04-preview' && $(java) && $(multiapi)
java:
  namespace: com.microsoft.azure.management.visualstudio.v2014_04_01_preview
  output-folder: $(azure-libraries-for-java-folder)/visualstudio/resource-manager/v2014_04_01_preview
regenerate-manager: true
generate-interface: true
```



## Multi-API/Profile support for AutoRest v3 generators 

AutoRest V3 generators require the use of `--tag=all-api-versions` to select api files.

This block is updated by an automatic script. Edits may be lost!

``` yaml $(tag) == 'all-api-versions' /* autogenerated */
# include the azure profile definitions from the standard location
require: $(this-folder)/../../../profiles/readme.md

# all the input files across all versions
input-file:
  - $(this-folder)/Microsoft.VisualStudio/preview/2014-04-01-preview/Csm.json

```

If there are files that should not be in the `all-api-versions` set, 
uncomment the  `exclude-file` section below and add the file paths.

``` yaml $(tag) == 'all-api-versions'
#exclude-file: 
#  - $(this-folder)/Microsoft.Example/stable/2010-01-01/somefile.json
```
