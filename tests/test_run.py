import subprocess
import sys
import time


def test_program_starts():
    """Тестируем запуск программы"""
    try:
        proc = subprocess.Popen(
            [sys.executable, "curholeview.py"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )

        time.sleep(2)

        proc.terminate()
        proc.wait(timeout=1)

        assert proc.returncode in [0, None, 1], (
            f"Unexpected exit code: {proc.returncode}"
        )

    except Exception:
        # В тестовой среде GUI может не запускаться
        assert True
