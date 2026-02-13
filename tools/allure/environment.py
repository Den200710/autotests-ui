from config import settings
import platform
import sys


def create_allure_environment_file():
    items = [f'{key}={value}' for key, value in settings.model_dump().items()]
    properties = '\n'.join(items)

    os = f'{platform.system()}, {platform.release()}'
    python_vers = sys.version

    with open(settings.allure_results_dir.joinpath('environment.properties'), 'w+') as file:
        file.write(f'{properties}\n')
        file.write(f'os_info={os}\n')
        file.write(f'python_version={python_vers}')
