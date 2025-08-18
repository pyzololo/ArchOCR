from .engines.dummy import DummyEngine
# from .engines.trocr import TrOcrEngine  # utwórz później, na razie zostaw sam Dummy

ENGINE_REGISTRY = {
    DummyEngine.name: DummyEngine,
    # TrOcrEngine.name: TrOcrEngine,  # odkomentujesz gdy zaimplementujesz
}

DEFAULT_ENGINE = DummyEngine.name

def available_model_names():
    return list(ENGINE_REGISTRY.keys())
