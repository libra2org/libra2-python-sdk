# Copyright © Aptos Foundation
# Copyright © Libra2 Research
# SPDX-License-Identifier: Apache-2.0

import os
import os.path

LIBRA2_CORE_PATH = os.getenv(
    "LIBRA2_CORE_PATH",
    os.path.abspath("./libra2-core"),
)
# :!:>section_1
FAUCET_URL = os.getenv(
    "LIBRA2_FAUCET_URL",
    "https://faucet.devnet.libra2.org",
)
FAUCET_AUTH_TOKEN = os.getenv("FAUCET_AUTH_TOKEN")
INDEXER_URL = os.getenv(
    "LIBRA2_INDEXER_URL",
    "https://api.devnet.libra2.org/v1/graphql",
)
NODE_URL = os.getenv("LIBRA2_NODE_URL", "https://api.devnet.libra2.org/v1")

API_KEY = os.getenv("API_KEY")
# <:!:section_1
