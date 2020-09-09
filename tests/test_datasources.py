import os
from ansys import dpf


if 'AWP_UNIT_TEST_FILES' in os.environ:
    unit_test_files = os.environ['AWP_UNIT_TEST_FILES']
else:
    raise KeyError('Please add the location of the DataProcessing '
                   'test files "AWP_UNIT_TEST_FILES" to your env')


if not dpf.has_local_server():
    dpf.start_local_server()


test_file_path = os.path.join(unit_test_files, 'DataProcessing', 'rst_operators',
                              'allKindOfComplexity.rst')


def test_create_data_sources():
    data_sources = dpf.DataSources()
    assert data_sources._message.id != 0


def test_create_with_resultpath_data_sources():
    data_sources = dpf.DataSources(test_file_path)
    assert data_sources._message.id != 0


def test_setresultpath_data_sources():
    data_sources = dpf.DataSources()
    try:
        data_sources.set_result_file_path(test_file_path)
        assert True
    except:
        assert False


def test_addpath_data_sources():
    data_sources = dpf.DataSources()
    try:
        data_sources.add_file_path(test_file_path)
        assert True
    except:
        assert False
        
def test_addupstream_data_sources():
    data_sources = dpf.DataSources()
    data_sources2 = dpf.DataSources()
    try:
        data_sources.add_upstream(data_sources2)
        assert True
    except:
        assert False

def test_delete_data_sources():
    data_sources = dpf.DataSources()
    try:
        data_sources.set_result_file_path(test_file_path)
        assert False
    except :
        assert True

def test_print_data_sources():
    data_sources = dpf.DataSources()
    data_sources.set_result_file_path(test_file_path)
    print(data_sources)
    assert data_sources.result_key=="rst"
    assert data_sources.result_files ==[test_file_path]

def test_delete_auto_data_sources():
    data_sources = dpf.DataSources()
    data_sources2 = dpf.DataSources(data_sources=data_sources)
    del data_sources
    try:
        data_sources2.set_result_file_path(test_file_path)
        assert False
    except:
        assert True
