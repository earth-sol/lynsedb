import builtins
import os
from lynse.core_components.fields_cache import IndexSchema
from lynse.core_components.fields_cache.index import Index


def test_load_schema_without_eval(monkeypatch, tmp_path):
    def fail_eval(*args, **kwargs):
        raise RuntimeError('eval should not be called')

    monkeypatch.setattr(builtins, 'eval', fail_eval)

    schema_dict = {'name': 'str', 'age': 'int'}
    schema = IndexSchema().load_from_dict(schema_dict)
    assert schema.indices == {'name': str, 'age': int}

    index = Index()
    for k, t in schema.indices.items():
        index.add_index(k, t)

    index.insert({'name': 'a', 'age': 1}, record_id=0)

    index_path = tmp_path / 'idx'
    index.save(index_path)

    new_index = Index().load(index_path)
    assert new_index.index_schema == {'name': str, 'age': int}
