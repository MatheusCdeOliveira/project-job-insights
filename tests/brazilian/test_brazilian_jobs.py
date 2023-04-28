from src.pre_built.brazilian_jobs import read_brazilian_file


def test_brazilian_jobs():
    teste = read_brazilian_file("tests/mocks/brazilians_jobs.csv")
    assert "titulo" not in teste[0]
    assert "salario" not in teste[0]
    assert "tipo" not in teste[0]
    assert "title" in teste[0]
    assert "salary" in teste[0]
    assert "type" in teste[0]
