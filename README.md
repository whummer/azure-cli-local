# Azure CLI for LocalStack

This project provides `azlocal`, a simple wrapper script for using the Azure command line
interface (CLI) with [LocalStack](https://github.com/localstack/localstack).

## Quick Installation

The `azlocal` command line is published as a `pip` library:
```
pip install azure-cli-local
```

## Configurations

The following environment variables can be configured:

* `PORT_AZURE`: Port under which the LocalStack Azure edge service is accessible (default: `12121`)
* `LOCALSTACK_HOSTNAME`: Target host under which LocalStack Azure edge service is accessible (default: `localhost`)

## License

The AWS CDK is distributed under the [Apache License, Version 2.0](https://www.apache.org/licenses/LICENSE-2.0).
