from enum import Enum

from astrbot.core.lang import t


class RstScene(Enum):
    GROUP_UNIQUE_ON = (
        "group_unique_on",
        t("builtin_stars-builtin_commands-commands-utils-rst_scene-group_unique_on"),
    )
    GROUP_UNIQUE_OFF = (
        "group_unique_off",
        t("builtin_stars-builtin_commands-commands-utils-rst_scene-group_unique_off"),
    )
    PRIVATE = (
        "private",
        t("builtin_stars-builtin_commands-commands-utils-rst_scene-private"),
    )

    @property
    def key(self) -> str:
        return self.value[0]

    @property
    def name(self) -> str:
        return self.value[1]

    @classmethod
    def from_index(cls, index: int) -> "RstScene":
        mapping = {1: cls.GROUP_UNIQUE_ON, 2: cls.GROUP_UNIQUE_OFF, 3: cls.PRIVATE}
        return mapping[index]

    @classmethod
    def get_scene(cls, is_group: bool, is_unique_session: bool) -> "RstScene":
        if is_group:
            return cls.GROUP_UNIQUE_ON if is_unique_session else cls.GROUP_UNIQUE_OFF
        return cls.PRIVATE
