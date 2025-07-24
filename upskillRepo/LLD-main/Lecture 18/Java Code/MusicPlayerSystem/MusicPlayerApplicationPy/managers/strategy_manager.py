from strategies.sequential_play_strategy import SequentialPlayStrategy
from strategies.random_play_strategy import RandomPlayStrategy
from strategies.custom_queue_strategy import CustomQueueStrategy
from enums.play_strategy_type import PlayStrategyType

class StrategyManager:
    _instance = None
    def __init__(self):
        self.sequential_strategy = SequentialPlayStrategy()
        self.random_strategy = RandomPlayStrategy()
        self.custom_queue_strategy = CustomQueueStrategy()
    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = StrategyManager()
        return cls._instance
    def get_strategy(self, type_):
        if type_ == PlayStrategyType.SEQUENTIAL:
            return self.sequential_strategy
        elif type_ == PlayStrategyType.RANDOM:
            return self.random_strategy
        else:
            return self.custom_queue_strategy
