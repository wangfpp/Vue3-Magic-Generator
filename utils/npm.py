import os
import shutil
import subprocess
import sys

from config.npm_config import NODE_PATH, HOME_PATH


def run_cmd(command):
    process = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                               shell=True)
    process.communicate(b"\n")
    process.wait()
    while not process.stdout.closed:
        output = process.stdout.readline().decode("gbk")
        if output == '' and process.poll() is not None:
            break
        if output:
            print(output.strip())
    return process.poll()


def init_vue(project_name: str):
    run_cmd(
        rf'cd "{os.path.join(HOME_PATH, "vue")}" && "{NODE_PATH}\npx" --yes create-vite@latest "{project_name}" --template vue')
    shutil.copytree(os.path.join(HOME_PATH, "base_vue"), os.path.join(HOME_PATH, "vue", project_name),
                    dirs_exist_ok=True)
    run_cmd(rf'cd "{os.path.join(HOME_PATH, "vue", project_name)}" && "{NODE_PATH}\npm" install')
