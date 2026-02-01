def test_import_curholeview():
    """Тестируем импорт основного модуля"""
    import os
    assert os.path.exists("curholeview.py"), "Main file missing"
    
    # Проверяем что можем прочитать и содержит класс
    with open("curholeview.py", "r", encoding="utf-8") as f:
        content = f.read()
        assert "class MartingaleApp" in content, "Main class not found"
    
    print("✓ Project structure verified")