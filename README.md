# Libra2 Python SDK
[![Discord][discord-image]][discord-url]
[![PyPI Package Version][pypi-image-version]][pypi-url]
[![PyPI Package Downloads][pypi-image-downloads]][pypi-url]

This provides basic functionalities to interact with [Libra2](https://libra2.org).

Currently, this is still in development and may not be suitable for production purposes.

Note: The sync client is deprecated, please only start new projects using the async client. Feature contributions to the sync client will be rejected.

## Requirements
This SDK uses [Poetry](https://python-poetry.org/docs/#installation) for packaging and dependency management:

```
curl -sSL https://install.python-poetry.org | python3 -
poetry install
```

## Unit testing
```bash
make test
```

## E2E testing and Using the Libra2 CLI

* Download and install the Libra2 CLI.
* Set the environment variable `LIBRA2_CLI_PATH` to the full path of the CLI.
* Retrieve the Libra2 Core Github Repo if you plan to run the Move examples locally.
* Set the environment variable `LIBRA2_CORE_REPO` to the full path of the Repository.
* `make integration_test`

You can do this a bit more manually by:

First, run a local testnet (run this from the root of the Libra2 core checkout):

```bash
libra2 node run-local-testnet --force-restart --assume-yes --with-indexer-api
```

Next, tell the end-to-end tests to talk to this locally running testnet:

```bash
export LIBRA2_CORE_REPO="/path/to/repo"
export LIBRA2_FAUCET_URL="http://127.0.0.1:8081"
export LIBRA2_INDEXER_URL="http://127.0.0.1:8090/v1/graphql"
export LIBRA2_NODE_URL="http://127.0.0.1:8080/v1"
```

Finally run the tests:

```bash
make examples
```

Integration Testing Using the Libra2 CLI:

```bash
make integration_test
```

> [!NOTE]
> The Python SDK does not require the Indexer, if you would prefer to test without it, unset or do not set the environmental variable `LIBRA2_INDEXER_URL` and exclude `--with-indexer-api` from running the Libra2 node software.

## Autoformatting
```bash
make fmt
```

## Autolinting
```bash
make lint
```

## Package Publishing

* Download the Libra2 CLI.
* Set the environment variable `LIBRA2_CLI_PATH` to the full path of the CLI.
* `poetry run python -m libra2_sdk.cli` and set the appropriate command-line parameters

## Semantic versioning
This project follows [semver](https://semver.org/) as closely as possible

[repo]: https://github.com/libra2org/libra2-python-sdk
[pypi-image-version]: https://img.shields.io/pypi/v/libra2-sdk.svg
[pypi-image-downloads]: https://img.shields.io/pypi/dm/libra2-sdk.svg
[pypi-url]: https://pypi.org/project/libra2-sdk
[discord-image]: https://img.shields.io/discord/945856774056083548?label=Discord&logo=discord&style=flat~~~~
[discord-url]: https://discord.gg/aptosnetwork
