from textSummarizer.logging import logger
from textSummarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline


#To run activate virtual env 
#Run .\env\Scripts\activate

STAGE_NAME = 'Data ingestion stage'

try:
    logger.info(f'>>>>>>> stage {STAGE_NAME} started >>>>>>>>>>>>>')
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f'<<<<<< stage {STAGE_NAME} completed <<<<<<<<')
except Exception as e:
    logger.exception(e)
    raise e
