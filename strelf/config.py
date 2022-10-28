import os
import dotenv
from collections import UserDict


class ConfigStripe(UserDict):
    _key_map = {
        'src.live': 'STRIPE_SRC_KEY_LIVE',
        'src.test': 'STRIPE_SRC_KEY_TEST',
        'dst.live': 'STRIPE_DST_KEY_LIVE',
        'dst.test': 'STRIPE_DST_KEY_TEST'
    }

    def __init__(self):
        dotenv.load_dotenv()
        super().__init__()
        self.update(
            {k: os.environ[v] for k, v in self._key_map.items()
                if v in os.environ}
        )
