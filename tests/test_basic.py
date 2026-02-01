import os

def test_project_files():
    """Проверяем существование файлов проекта"""
    files_to_check = ['curholeview.py', 'README.md']
    for file in files_to_check:
        assert os.path.exists(file), f"Missing: {file}"
    print("✓ Project files verified")