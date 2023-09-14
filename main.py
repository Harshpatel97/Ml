from src.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from src.logging import logger


STAGE_NAME = 'Data Ingestion'

try:
    logger.info(f">>>>>>>{STAGE_NAME} started <<<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e
    
STAGE_NAME1 = 'Data Validation'

try:
    logger.info(f">>>>>>>{STAGE_NAME} started <<<<<<<")
    data_validation = DataValidationTrainingPipeline()
    data_validation.main()
    logger.info(f">>>>>> stage {STAGE_NAME1} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e