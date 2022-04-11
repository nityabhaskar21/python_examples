def install_and_import(package):
    import importlib
    try:
        importlib.import_module(package)
        print("imported")
    except ImportError:
        import pip
        pip.main(['install', package])
    finally:
        globals()[package] = importlib.import_module(package)


install_and_import('python-dotenv')