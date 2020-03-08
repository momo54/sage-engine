# bgp_interface_test.py
# Author: Thomas MINIER - MIT License 2017-2018
import pytest
from sage.http_server.server import run_app
from starlette.testclient import TestClient
from tests.http.utils import post_sparql


# fixutre format: query, expected graph content
fixtures = [
    (
        """INSERT DATA { <http://donald> <http://isa> "prof"} """,
        [
            ("http://donald","http://isa","\"prof\"")
        ]
    ),
    (
        """ INSERT { ?z <http://source> 'rennes' }
            WHERE {
                BIND(<http://example.org/rowid>(<http://donald>, <http://isa>, 'prof') as ?z)
            }
        """,
        [
            ("http://610075ea5e32c4cb26724c31aa5de3c5","http://source","\"rennes\"")
        ]
    ),
    (
    """
    INSERT {
        ?z <http://source> 'rennes'.
        ?w <http://source> 'rennes'
    } WHERE {
        BIND(<http://example.org/rowid>(<http://donald>, <http://isa>, 'duck') as ?z)
        BIND(<http://example.org/rowid>(<http://trump>, <http://isa>, 'dick') as ?w)
    }
    """,
        [
            ("http://4bef678a25576879b56a4e3a5aa8d1cd","http://source","\"rennes\""),
            ("http://c2fa74d2d092e3519266a8eb34824559","http://source","\"rennes\"")
        ]
    )
]


class TestInsertDataInterface(object):
    @classmethod
    def setup_method(self):
        self._app = run_app('tests/update/config.yaml')
        self._client = TestClient(self._app)

    @classmethod
    def teardown_method(self):
        pass

    @pytest.mark.parametrize("query,expected_content", fixtures)
    def test_insert_interface(self, query, expected_content):
        # insert data
        response = post_sparql(self._client, query, None, 'http://testserver/sparql/update-test')
        assert response.status_code == 200
        # fetch graph content to assert that data was inserted
        fetch_query = "SELECT * WHERE {?s ?p ?o}"
        has_next = True
        next_link = None
        results = list()
        while has_next:
            response = post_sparql(self._client, fetch_query, next_link, 'http://testserver/sparql/update-test')
            assert response.status_code == 200
            response = response.json()
            print(response)
            has_next = response['hasNext']
            next_link = response['next']
            results += response['bindings']
        print(results)
        assert len(results) == len(expected_content)
        for b in results:
            assert (b['?s'], b['?p'], b['?o']) in expected_content
