import os
from pathlib import Path
from box.exceptions import BoxValueError
import yaml
from textSummarizer.logging import logger
from box import ConfigBox
from ensure import ensure_annotations
from typing import Any, Collection


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    Reads a YAML file and returns a ConfigBox object with the content.
        Args:
        path_to_yaml (Path): The path to the YAML file.
        
        Returns:
        ConfigBox: A ConfigBox object with the content of the YAML file.
    """
    try: 
        with open(path_to_yaml, 'r') as file:
            config = yaml.safe_load(file)
            logger.info(f"yaml file {path_to_yaml} loaded successfully ")
            return ConfigBox(config)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e
    
def create_directories(list_of_paths: Collection, verbose: bool=True) -> None:
    """
        Creates a list of directories
        Args: 
        path_to_directory (list): A list of paths to directories to be created.
    """
    for path in list_of_paths:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Directory {path} created successfully.")


@ensure_annotations
def get_size_file(path: Path) -> str:
    """
    Returns the size of a file in kb
    """

    size_in_kb = round(os.path.getsize(path)/1024)
    return f' {size_in_kb} KB'