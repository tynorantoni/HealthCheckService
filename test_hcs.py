import json

import pytest

from statuschecker import get_health_status


class TestClass:

    def test_get_health_status(self):
        responses = get_health_status()
        dict_of_responses = json.loads(responses)
        for response in dict_of_responses:
            assert dict_of_responses[response] == 'pong' or dict_of_responses[response] == 'dead'


if __name__ == '__main__':
    pytest.main()
