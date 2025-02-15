# scan_test.py
# Author: Thomas MINIER - MIT License 2017-2020
import pytest
import asyncio

from rdflib.plugins.sparql.algebra import translateQuery, translateUpdate
from rdflib.plugins.sparql.parser import parseQuery, parseUpdate
from sage.query_engine.sage_engine import SageEngine
from sage.database.hdt.connector import HDTFileConnector
from sage.query_engine.optimizer.query_parser import parse_query
from tests.utils import DummyDataset

hdtDoc = HDTFileConnector('tests/data/context.hdt')
dataset = DummyDataset(hdtDoc, 'context')
engine = SageEngine()


queries = [
    ("""
        select ?md5 where {
          ?s <http://isa> ?o
          BIND(URI(CONCAT("http://",MD5(CONCAT(STR(?s),STR(<http://isa>),STR(?o))))) as ?md5)
        }
    """, 5),
    ("""
         select ?o1 where {
           ?s <http://isa> ?o
           BIND(URI(CONCAT("http://",MD5(CONCAT(STR(?s),STR(<http://isa>),STR(?o))))) as ?md5)
           ?md5 <http://source> ?o1
         }
    """, 5),
        ("""
        select ?md5 where {
        BIND(URI(CONCAT("http://",MD5(CONCAT(STR(<http://donald>),STR(<http://isa>),STR("jerk"))))) as ?md5)
        }
        """, 1)
    ]

@pytest.mark.asyncio
@pytest.mark.parametrize("query,cardinality", queries)
async def test_parse_rowid(query, cardinality):
    iterator,cards = parse_query(query, dataset, 'context')
    print("pipeline:")
    print(iterator)
    assert len(cards) >= 0
    assert iterator is not None

#loop = asyncio.get_event_loop()
#loop.run_until_complete(test_parse_query0())
#loop.run_until_complete(test_parse_query1())
#loop.close()
