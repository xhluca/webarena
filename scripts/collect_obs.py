"""Simple script to quickly get the observation of a page"""

import json
import re
import time
from typing import Dict, Optional, Tuple, Type, Union, cast

import pytest
from playwright.sync_api import Page, expect

from browser_env import (
    ScriptBrowserEnv,
    create_id_based_action,
    create_key_press_action,
    create_playwright_action,
    create_scroll_action,
)
from browser_env.env_config import *

HEADLESS = False


def gen_tmp_storage_state() -> None:
    with open(f"scripts/tmp_storage_state.json", "w") as f:
        json.dump({"storage_state": ".auth/gitlab_state.json"}, f)


def get_observation(
    observation_type: str, current_viewport_only: bool
) -> None:
    env = ScriptBrowserEnv(
        observation_type=observation_type,
        current_viewport_only=current_viewport_only,
        headless=HEADLESS,
        sleep_after_execution=2.0,
    )
    env.reset(options={"config_file": f"scripts/tmp_storage_state.json"})
    s = f"""page.goto("http://ec2-3-131-244-37.us-east-2.compute.amazonaws.com:7770/3-pack-samsung-galaxy-s6-screen-protector-nearpow-tempered-glass-screen-protector-with-9h-hardness-crystal-clear-easy-bubble-free-installation-scratch-resist.html")
    page.get_by_role("link", name="12 Reviews").click()
    page.scroll(down)"""

    action_seq = s.split("\n")

    for action in action_seq:
        action = action.strip()
        obs, success, _, _, info = env.step(create_playwright_action(action))
        print(obs["text"])
        _ = input("Press enter to continue")


if __name__ == "__main__":
    gen_tmp_storage_state()
    obs_type = "accessibility_tree"
    current_viewport_only = True
    get_observation(obs_type, current_viewport_only)
