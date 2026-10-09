import os
import subprocess
import sys
from pathlib import Path

import pytest

EXEMPLES = Path(__file__).resolve().parents[2]  # dossier exemples/


@pytest.fixture
def lancer():
    """Execute un script depuis exemples/ et renvoie sa sortie standard."""

    def _lancer(*commande: str) -> str:
        env = {**os.environ, "PYTHONIOENCODING": "utf-8"}
        resultat = subprocess.run(
            list(commande), cwd=EXEMPLES, capture_output=True,
            text=True, encoding="utf-8", env=env,
        )
        assert resultat.returncode == 0, resultat.stderr
        return resultat.stdout

    return _lancer


@pytest.fixture
def python_exe():
    return sys.executable
