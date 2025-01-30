from enum import Enum

class MetricUnit(Enum):
    FRAMERATE = "FPS"
    FRAMERATE_LOW_1 = "FPS"
    FRAMERATE_LOW_01 = "FPS"
    CPU_USAGE = "%"
    GPU_USAGE = "%"
    RAM_USAGE = "MB"
    MEMORY_USAGE = "MB"

    @classmethod
    def get_unit(cls, metric: str) -> str:
        mapping = {
            "Framerate": cls.FRAMERATE,
            "Framerate 1% Low": cls.FRAMERATE_LOW_1,
            "Framerate 0.1% Low": cls.FRAMERATE_LOW_01,
            "CPU usage": cls.CPU_USAGE,
            "GPU usage": cls.GPU_USAGE,
            "RAM usage \\ process": cls.RAM_USAGE,
            "Memory usage \\ process": cls.MEMORY_USAGE,
        }
        return mapping.get(metric, "").value
