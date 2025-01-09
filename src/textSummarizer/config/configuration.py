from textSummarizer.constants import *
from textSummarizer.utils.common import create_directories, read_yaml
from textSummarizer.entity import (DataIngestionConfig)


class ConfigurationManager:
    def __init__(
            self,
            config_file_path: Path = CONFIG_FILE_PATH,
            params_file_path: Path = PARAMS_FILE_PATH
    ):
        self.config = read_yaml(config_file_path)
        self.params = read_yaml(params_file_path)
        
        create_directories(list_of_paths=[self.config.artifacts_root])
    
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion

        create_directories(list_of_paths=[config.root_dir])

        data_integration_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir          
        )
        return data_integration_config