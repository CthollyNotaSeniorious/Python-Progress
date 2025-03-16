import tempfile
from pathlib import Path

import pytest


@pytest.fixture
def source(file_content):
    with tempfile.NamedTemporaryFile(suffix=".txt") as tmp_file:
        source_path = Path(tmp_file.name)
        source_path.write_text(file_content)
        yield source_path
